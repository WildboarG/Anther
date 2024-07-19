from __init__ import *

host = "https://bbs.ai-thinker.com"
um ="/forum.php"
plugin ="/plugin.php"
home = host + um
loginindex= host+"/member.php?mod=logging&action=login&infloat=yes&handlekey=login&inajax=1&ajaxtarget=fwin_content_login"
loginurl = host+plugin+"?id=one_sms:api&action=user&inajax=1"
urlid =host+plugin+"?id=one_sms&action=user_login&referer=https%3A%2F%2Fbbs.ai-thinker.com%2Fforum.php&infloat=yes&handlekey=login&inajax=1&ajaxtarget=fwin_content_login"    
signhome = host+plugin+"?id=dc_signin:sign&infloat=yes&handlekey=sign&inajax=1&ajaxtarget=fwin_content_sign"
signrequest = host+plugin+"?id=dc_signin:sign&inajax=1"
sendurl = host+um+"?mod=post&action=reply&fid=179&tid=45019&extra=&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1"
urlhuo = host+um+"?mod=viewthread&tid=45019"

Username = "xxxxxxx"
Password = "xxxxxxx"
uid= "xxxxx"

## re
reformhash = '<input type="hidden" name="formhash" value="(.*?)" />'
resaltkey = "cRkY_2132_saltkey=(.*?);"
relastvisit = "cRkY_2132_lastvisit=(.*?);"
resid = "cRkY_2132_sid=(.*?);"
restact = "cRkY_2132_lastact=(.*?);"
rephp ="PHPSESSID=(.*?);"
howpage = '<span title="共 (.*?) 页">'
lastuser = '<a href="(.*?)" target="_blank" c="1" class="xi2">.*?</a>'


### range msg
msg =[
    "祝安信可社区一周年快乐:victory:",
    "祝大家一周年快乐！",
    "祝安信可社区一周年快乐! 一路相伴",
    "祝安信可社区一周年快乐! 大家一起学习",
    "祝安信可社区一周年快乐:lol",
    "安信可社区一周年快乐! 大佬们带带我",
    "安信可社区一周年快乐! 啦啦啦啦啦",
    "祝安信可社区一周年快乐！感谢社区大佬们",
    "祝安信可社区一周年快乐，祝安信可社区一周年快乐！",
    "祝安信可社区一周年快乐！祝大家一周年快乐！",
    "祝安信可社区一周年快乐！我又来板砖了",
    "祝安信可社区一周年快乐！我胡汉三又回来了"
]