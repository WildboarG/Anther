from __init__ import *

host = "https://bbs.ai-thinker.com"
um ="/forum.php"
plugin ="/plugin.php"
home = host + um
loginurl = host+plugin+"?id=one_sms:api&action=user&inajax=1"
signhome = host+plugin+"?id=dc_signin:sign&infloat=yes&handlekey=sign&inajax=1&ajaxtarget=fwin_content_sign"
signrequest = host+plugin+"?id=dc_signin:sign&inajax=1"
sendaddr = home+"?mod=post&action=reply&fid=179&tid=45019&extra=&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1"
urlhuo = home+"?mod=viewthread&tid=45019&_dsign=707f90f0"


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
    "祝安信可社区一周年快乐:victory:"
]
