import requests
import re
import time
import os
import sched
from bs4 import BeautifulSoup
class Click(object):
    def __init__(self):
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                      'Referer':'http://bbs.uestc.edu.cn/member.php?mod=logging&action=login',
                      'Content-Length':'155'}
        self.session=requests.session()
        self.schedule=sched.scheduler(time.time,time.sleep)
    def time_exe(self,username,password,inc,cmd):
        self.schedule.enter(inc,0,cmd,(username,password))
        self.schedule.run()
    def scarpy(self,username,password,referer='http://bbs.uestc.edu.cn/',loginfield='username',questionid='0',answer=""):
        login_url='http://bbs.uestc.edu.cn/member.php?mod=logging&action=login'
        r = self.session.get(login_url)
        loginhtml = r.text
        list = re.findall(r'formhash=(.+?)\'\,', loginhtml)
        formhash=list[0]
        data={'formhash':formhash,'referer':referer,'loginfield':loginfield,'username':username,'password':password,'questionid':questionid,'answer':answer}
        posturl='http://bbs.uestc.edu.cn/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=Lmqqj&inajax=1'
        post=self.session.post(posturl,data=data,headers=self.headers,verify=False)
        count=1
        for i in range(1,1956):
            pageurl='http://bbs.uestc.edu.cn/forum.php?mod=forumdisplay&fid=61&page='+str(i)
            pagehtml = self.session.get(pageurl).text
            soup=BeautifulSoup(pagehtml,"html.parser")
            titles=soup.findAll('a',attrs={'class':'s xst'})
            with open('ysl.txt','a',encoding='utf-8') as f:
                for title in titles:
                    print("抓取%d条"%count)
                    count=count+1
                    f.write("\n")
                    f.write(title.string)
    def autorespones(self,username,password,referer='http://bbs.uestc.edu.cn/',loginfield='username',questionid='0',answer=""):
        login_url = 'http://bbs.uestc.edu.cn/member.php?mod=logging&action=login'
        r = self.session.get(login_url)
        loginhtml = r.text
        list = re.findall(r'formhash=(.+?)\'\,', loginhtml)
        formhash = list[0]
        data = {'formhash': formhash, 'referer': referer, 'loginfield': loginfield, 'username': username,
                'password': password, 'questionid': questionid, 'answer': answer}
        posturl = 'http://bbs.uestc.edu.cn/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=Lmqqj&inajax=1'
        post = self.session.post(posturl, data=data, headers=self.headers, verify=False)
        for page in range(1,3):
            pageurl = 'http://bbs.uestc.edu.cn/forum.php?mod=forumdisplay&fid=61&page='+str(page)
            pagehtml=self.session.get(pageurl).text
            thread=re.findall(r'id="normalthread_(.+?)\"',pagehtml)
            for i in thread:
               print(i)
               titleurl="http://bbs.uestc.edu.cn/forum.php?mod=viewthread&tid="+i+"&extra=page%3D1"
               titlehtml=self.session.get(titleurl).text
               form=re.findall(r'formhash=(.+?)\"',titlehtml)
               timing=re.findall(r'id="posttime" value="(.+?)\"',titlehtml)
               aimurl='http://bbs.uestc.edu.cn/forum.php?mod=post&action=reply&fid=61&tid='+i+'&extra=page%3D1&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1'
               autoresponsedata={'message':'','posttime':timing[0],'formhash':form[0],'usesig':'1','subject':''}
               print(autoresponsedata)
               response=self.session.post(aimurl,data=autoresponsedata,headers=self.headers,verify=False)
               time.sleep(0.1)
if __name__=='__main__':
    username=""
    password=""
    c=Click()
    c.scarpy(username,password)




