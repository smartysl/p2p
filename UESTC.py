import requests
import re
from bs4 import BeautifulSoup
session=requests.session()
headers={'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64) AppleWebKit/537.36(KHTML,likeGecko)Chrome/63.0.3239.132Safari/537.36'
}
html=session.get("http://idas.uestc.edu.cn/authserver/login?service=http%3A%2F%2Fportal.uestc.edu.cn%2F").text
ITlist=re.findall(r'LT-(.+?)-cas',html)
IT="LT-"+ITlist[0]+"-cas"
data={'username':'','password':'','lt':IT,'dllt':'userNamePasswordLogin','execution':'e1s1','_eventId':'submit','rmShown':'1'}
print(data)
post=session.post("http://idas.uestc.edu.cn/authserver/login?service=http://portal.uestc.edu.cn/index.portal",data=data)
session.get("http://eams.uestc.edu.cn/eams/home.action")
session.get("http://eams.uestc.edu.cn/eams/courseTableForStd!courseTable.action")
data1={ 'ignoreHead':1,
    'setting.kind':'std',
    'startWeek':1,
    'semester.id':183,
    'ids':148821}
course=session.post("http://eams.uestc.edu.cn/eams/courseTableForStd!courseTable.action",data=data1).text
soup=BeautifulSoup(course,"html.parser")
courses=soup.find("tbody").children
for i in courses:
     print(i)
session.get("http://eams.uestc.edu.cn/eams/logout.action?jsdEkingstar=1&redirect=http%3A%2F%2Fportal.uestc.edu.cn%2Flogout.portal")

