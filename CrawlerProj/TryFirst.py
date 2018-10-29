# -*- coding: utf-8 -*-

import urllib2
import urllib
import re
import thread
import time
import DataInsert

class Douban_Model:
    def __init__(self):
        #self.page = 1
        #self.pages = []
        #self.enable = False
        pass

    def GetPage(self,begin_num,count_num):

        currentPage = begin_num

        aa = DataInsert.DataInsert()

        for i in range(begin_num,begin_num+count_num+1):
            currentURL="http://book.douban.com/subject/" + str(currentPage) +"/?from=tag"   #拼装当前要分析的URL
            myUrl = currentURL
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            headers = { 'User-Agent' : user_agent }

            try:
                req = urllib2.Request(myUrl, headers = headers)
                myResponse = urllib2.urlopen(req)
                myPage = myResponse.read()

                #encode的作用是将unicode编码转换成其他编码的字符串
                #decode的作用是将其他编码的字符串转换成unicode编码
                #unicodePage = myPage.decode("utf-8")
                unicodePage = myPage

                #BookName = re.search("(?<=<span property=\"v:itemreviewed\">)(.*)(?=</span>)",unicodePage,re.M)
                BookName = re.search("(?<=<title>)(.*)(?=</title>)",unicodePage,re.M)
                if BookName is None:
                    BookName = re.search("(?<=<title>)\s+(.*)\s+(?=</title>)",unicodePage,re.M)

                BookVote = re.search("(?<=<span property=\"v:votes\">)(.*)(?=</span>)",unicodePage,re.M)
                BookAvg = re.search("(?<=<strong class=\"ll rating_num \" property=\"v:average\">)\s+(.*)\s+(?=</strong>)",unicodePage,re.M)

                #传参变量置空
                bookName = ''
                bookVote = 0
                bookAvg = 0


                #Print结果
                print "CurrentPage is :", currentPage

                if BookName is None:
                    print "BookName is None"
                else:
                    print "BookName is :", re.sub(r'\s+','',BookName.group())
                    bookName = re.sub(r'\s+','',BookName.group())

                if BookVote is None:
                    print "BookVote is None"
                else:
                    print "BookVote is :", re.sub(r'\s+','',BookVote.group())
                    bookVote = re.sub(r'\s+','',BookVote.group())

                if BookAvg is None:
                    print "BookAvg is None"
                else:
                    a = re.sub(r'\s+','',BookAvg.group())
                    print "BookAvg is :", a
                    if a=='':
                        bookAvg=0
                    else:
                        bookAvg = a
                try:
                    #DataInsert.DataInsert.execute(26582558,'电影制作手册（第4版)',20,2.7)
                    aa.execute(currentPage,bookName,bookVote,bookAvg)
                except IOError:
                    print IOError
            except:
                pass


            print "当前编号: " + str(currentPage)
            currentPage += 1
            print "sleeping now"
            time.sleep(2)
            print "awake"




print "Let's begin..."
myCraw = Douban_Model()

myCraw.GetPage(1040000,100000)


