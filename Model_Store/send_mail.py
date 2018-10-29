#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText

_user = "13160112@qq.com"
_pwd  = "qpmddxlkgishbhea"
_toList = ["liuxiaohuan@ppdai.com","13160112@qq.com"]

msg = MIMEText("multisending test")
msg["Subject"] = "multisending test"
msg["From"]    = _user
msg["To"] = ';'.join(_toList)


try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, _toList, msg.as_string())
    s.quit()
except smtplib.SMTPException,e:
    print "Falied,%s"%e

