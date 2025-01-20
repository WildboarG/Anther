from  __init__ import *
import requests
import re
import time
import random
import os

def login(Username,Password :str) -> str:
    res = requests.get(home)
    rheader = res.headers["Set-Cookie"]
    formhash = re.findall(reformhash, res.text)[0]
    if formhash == "":
        return "login error"
    data = {
        "formhash": formhash,
        "ident": "user_login",
        "referer": home,
        "username":Username,
        "password": Password
    }
    saltkey = re.findall(resaltkey, rheader)[0]
    lastvisit = re.findall(relastvisit, rheader)[0]
    sid = re.findall(resid, rheader)[0]
    lastact = re.findall(restact, rheader)[0]
    ## 构建登录请求cookie
    cookie = "cRkY_2132_saltkey={}; \
            cRkY_2132_lastvisit={}; \
            cRkY_2132_sendmail=1; \
            cRkY_2132_sid={}; \
            cRkY_2132_lastact={}" \
    .format(saltkey,lastvisit,sid,lastact)

    headers = {
        "Cookie":cookie,
    }
    res = requests.post(url=loginurl,data=data,headers=headers)
    try:
        print(res.json()["message"])
        rheader = res.headers["Set-Cookie"]

        ulastactivity = re.findall("cRkY_2132_ulastactivity=(.*?);",rheader)[0]
        auth = re.findall("cRkY_2132_auth=(.*?);",rheader)[0]

        lastcheckfeed = re.findall("cRkY_2132_lastcheckfeed=(.*?);",rheader)[0]
        checkfollow = re.findall("cRkY_2132_checkfollow=(.*?);",rheader)[0]
    except:
        print("登录失败")
        return 
    
    ## 登陆成功
    print("-------------------")
    myhome = requests.get(home,headers=headers)
    rheader = myhome.headers["Set-Cookie"]
    try:
        PHPSESSID = re.findall(rephp,rheader)[0]
        #print("ph:",PHPSESSID)
        sid = re.findall(resid,rheader)[0]
        lastact = re.findall(restact,rheader)[0]

        cook = "PHPSESSID={}; \
        cRkY_2132_sid={}; \
        cRkY_2132_saltkey={}; \
        cRkY_2132_lastvisit={}; \
        cRkY_2132_ulastactivity={}; \
        cRkY_2132_auth={}; \
        cRkY_2132_lastcheckfeed={}; \
        cRkY_2132_checkfollow={}; \
        cRkY_2132_nofavfid=1; \
        cRkY_2132_sendmail=1; \
        cRkY_2132_checkpm=1; \
        cRkY_2132_lastact={}"\
        .format(PHPSESSID,sid,saltkey,lastvisit,ulastactivity,auth,lastcheckfeed,checkfollow,lastact)
        headers = {
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Cookie":cook
        }
        #print(headers)
        return headers
    except:
        print("登录失败")
        return

def Oneyear(uid, headers : dict): 
    getpage = requests.get(url=urlhuo,headers=headers)
    #print(getpage.text)
    lastpage = re.findall(howpage,getpage.text)
    page = "&extra=&page="+ lastpage[0]
    urldong = urlhuo+page

    res = requests.get(url=urldong,headers=headers)
    #print(res.text)
    lastdemo = re.findall(lastuser,res.text)
    formhash = re.findall(reformhash,res.text)
    lastpage = re.findall(howpage,res.text)
    print("LastPage:",lastpage[0])
    
    urldong = urlhuo +"&extra=&page="+lastpage[0]

    datenow = str(int(time.time()))

    ## 判断最后两个用户有自己吗？
    if (lastdemo != []): 
        try:
            if((lastdemo[-1][-5:] != uid) and (lastdemo[-2][-5:]!= uid)):
                print("Userid  :",lastdemo[-1][-5:],lastdemo[-2][-5:])
                sendmsg = random.choice(msg)
                datas = {
                        "file":"", 
                        "message": sendmsg,
                        "posttime": datenow,
                        "formhash": formhash[0],
                        "usesig": "1",
                        "subject":""
                } 
                res = requests.post(url=sendaddr,headers=headers,data=datas)
                print(sendmsg)
                ##print(res.text)  
            else:
                print("别发！")
        except:
            print("发不了")
    else:
        print("ok")

def Registration(arg : list): ## 签到
   
    header = arg
    res = requests.get(signhome,headers=header)

    print("####################")

    formhash = re.findall(reformhash, res.text)
    if formhash != []:
        print("new#####:",formhash)  
        data2 = {
        "formhash": formhash,
        "signsubmit": "yes",
        "handlekey": "signin",
        "emotid": "1",
        "referer": host+um,
        "content": "记上一笔，hold住我的快乐！"
        }
        response = requests.post(url=signrequest,headers=header,data=data2)
        print("签到成功！")
        #print(response.text)

    else:
        print("今天已经签到过了！明天在来吧")

if __name__ == '__main__':
    credentials = os.getenv('Anthinker')  # 青龙环境变量
    if credentials:
        Username, Password = credentials.split(':')  # 使用 : 分隔用户名和密码[用户名:密码]
    else:
        pass
    token = login(Username,Password)
    Registration(token)






