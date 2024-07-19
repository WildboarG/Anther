from  __init__ import *
import requests
import re
import time
import random

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
    saltkey1 = re.findall(resaltkey, rheader)[0]
    lastvisit1 = re.findall(relastvisit, rheader)[0]
    sid = re.findall(resid, rheader)[0]
    lastact = re.findall(restact, rheader)[0]

    cookie = "cRkY_2132_saltkey={}; \
            cRkY_2132_lastvisit={}; \
            cRkY_2132_sendmail=1; \
            cRkY_2132_sid={}; \
            cRkY_2132_lastact={}" \
    .format(saltkey1,lastvisit1,sid,lastact[:13]+"plugin.php%09")

    headers = {
        "Cookie":cookie,
    }
    res = requests.get(url=loginindex,headers=headers)
    rheader = res.headers["Set-Cookie"]

    sid2 = re.findall(resid,rheader)[0]
    last2 = re.findall(restact,rheader)[0]

    cookie = "cRkY_2132_saltkey={}; \
            cRkY_2132_lastvisit={}; \
            cRkY_2132_sendmail=1; \
            cRkY_2132_sid={}; \
            cRkY_2132_lastact={}" \
            .format(saltkey1,lastvisit1,sid2,last2)

    headers["Cookie"] = cookie

    res = requests.get(urlid, headers=headers)

    rheader = res.headers["Set-Cookie"]

    sid3 = re.findall(resid,rheader)[0] 
    last3 = re.findall(restact,rheader)[0]

    cookie = "cRkY_2132_saltkey={}; \
            cRkY_2132_lastvisit={}; \
            cRkY_2132_sendmail=1; \
            cRkY_2132_sid={}; \
            cRkY_2132_lastact={}" \
            .format(saltkey1,lastvisit1,sid3,last3)


    headers["Cookie"] = cookie
    res = requests.post(url=loginurl,data=data,headers=headers)
    rheader = res.headers["Set-Cookie"]

    sid4 = re.findall(resid,rheader)[0]
    last4 = re.findall(restact,rheader)[0]
    ulastactivity = re.findall("cRkY_2132_ulastactivity=(.*?);",rheader)[0]
    auth = re.findall("cRkY_2132_auth=(.*?);",rheader)[0]
    loginuser = re.findall("cRkY_2132_loginuser=(.*?);",rheader)[0]
    activationauth = re.findall("cRkY_2132_activationauth=(.*?);",rheader)[0]
    pmnum = re.findall("cRkY_2132_pmnum=(.*?);",rheader)[0]
    lastcheckfeed = re.findall("cRkY_2132_lastcheckfeed=(.*?);",rheader)[0]
    checkfollow = re.findall("cRkY_2132_checkfollow=(.*?);",rheader)[0]

    print(res.json()["message"])
    ## 登陆成功
    myhome = requests.get(home,headers=headers)
    rheader = myhome.headers["Set-Cookie"]
    print("-------------------")
    PHPSESSID = re.findall(rephp,rheader)[0]
    #print("ph:",PHPSESSID)
    sid5 = re.findall(resid,rheader)[0]
    last5 = re.findall(restact,rheader)[0]

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
    .format(PHPSESSID,sid5,saltkey1,lastvisit1,ulastactivity,auth,lastcheckfeed,checkfollow,last5)
    headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Cookie":cook
    }
    return headers,PHPSESSID,saltkey1,lastvisit1,sid5,ulastactivity,auth,lastcheckfeed,checkfollow

def Oneyear(uid, headers : dict): ## 一周年活动
    getpage = requests.get(url=urlhuo,headers=headers)
    lastpage = re.findall(howpage,getpage.text)
    page = "&extra=&page="+lastpage[0]
    urldong = urlhuo+page

    res = requests.get(url=urldong,headers=headers)
    #print(res.text)
    lastdemo = re.findall(lastuser,res.text)
    formhash = re.findall(reformhash,res.text)
    lastpage = re.findall(howpage,res.text)
    #print("LastPage:",lastpage[0])
    
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
                res = requests.post(url=sendurl,headers=headers,data=datas)
                print(sendmsg)
                #print(res.text)  
            else:
                print("别发啦，小心被园长抓住！")
        except:
            print("发不了，会被园长抓住的！")
    else:
        print("ok")

def Registration(arg : list): ## 签到
    
    header = arg[0]
    res = requests.get(signhome,headers=header)
    rheader = res.headers["Set-Cookie"]
    lasta = re.findall(restact,rheader)[0]
    print("####################")

    cooks = "PHPSESSID={}; \
    cRkY_2132_saltkey={}; \
    cRkY_2132_lastvisit={}; \
    cRkY_2132_sid={}; \
    cRkY_2132_ulastactivity={}; \
    cRkY_2132_auth={}; \
    cRkY_2132_lastcheckfeed={}; \
    cRkY_2132_sendmail=1; \
    cRkY_2132_lastact={}"\
    .format(arg[1],arg[2],arg[3],\
            arg[4],arg[5],arg[6],arg[7],lasta)
    # .format(PHPSESSID,saltkey1,lastvisit1,sid5,ulastactivity,auth,lastcheckfeed,lasta)
    

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
        headers6 = {
            "Cookie":cooks,
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        }
        response = requests.post(url=signrequest,headers=header,data=data2)
        print("签到成功！")

    else:
        print("今天已经签到过了！明天在来吧")

if __name__ == '__main__':
    somthing = login(Username,Password)
    header = somthing[0]
    Oneyear(uid,header)  
    Registration(somthing)






