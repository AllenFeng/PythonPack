import hashlib
import json
import requests
import time


def getChallenge(session):
    url = 'https://passport.ch.com/Login/initValidate?t=' + str(long(time.time()*1000))
    content = session.get(url,verify=False).content
    root  = json.loads(json.loads(content))
    if root['success'] != 1:
        raise Exception('get gt failed')
    gt = root['gt']
    challenge = root['challenge']
    return (gt,challenge)

def hackCapcha(session,gt,challenge):
    product = 'embed'
    referer = 'https://passport.ch.com/?pn=9C00211312241938530009'
    appid = 'geetest'
    appkey = 'geetest'

    params = 'appid=%s&challenge=%s&gt=%s&product=%s&referer=%s&' %(appid,challenge,gt,product,referer)
    raw = params+appkey

    m = hashlib.md5()
    m.update(raw)
    signinfo = m.hexdigest()

    url = 'http://dev.cleverli.cn:8310/api/captcha/geetest?'+params+'signinfo=%s' %signinfo
    content = session.get(url).content
    print content
    root = json.loads(content)
    validate = root['validate']
    challenge = root['challenge']
    seccode = validate+'|jordan'

    return (validate,challenge,seccode)


def login(session,user,pwd,challenge,validate,seccode):
    url = 'https://passport.ch.com/login/check'
    session.headers['Content-type'] = 'application/x-www-form-urlencoded'
    session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'
    session.headers['Referer'] = 'https://passport.ch.com/LoginFrame?pn=9C00211312241938530009&return_url=http://www.ch.com/Sso/Login&lang=zh-CN'
    session.headers['Accept'] = '*/*'
    session.headers['Accept-Encoding'] = 'gzip, deflate, br'

    data = {
        'u':user,
        'p':pwd,
        'geetest_challenge':challenge,
        'geetest_validate':validate,
        'geetest_seccode':seccode,
    }
    print json.dumps(data)

    data = 'u=%s&p=%s&geetest_challenge=%s&geetest_validate=%s&geetest_seccode=%s' %(user,pwd,challenge,validate,seccode)
    content = session.post(url,data).content
    print content
    root = json.loads(content)
    return root['Code']

session = requests.session()
session.get('https://passport.ch.com/LoginFrame')
(gt,challenge) = getChallenge(session)
print gt,challenge
(validate,newchallenge,seccode) = hackCapcha(session,gt,challenge)
print login(session,'xxxxxx','bbbbbb',newchallenge,validate,seccode)