import requests
import time
import json
import re
import configparser

# 判断页面是否登陆正确返回json
def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError:
        return False
    return True

def checkin(myCookie,myId):
    callbackParam1 = 'jQuery183048434872539258844_' + str(int(round(time.time() * 1000)))
    callbackParam2 = str(int(round(time.time() * 1000)))
    url_signlist = 'https://club.lenovo.com.cn/signlist'
    url_userinfo = 'https://i.lenovo.com.cn/mcenter/getUserNameAndUserLevel.jhtml?lenovoId=' + myId + '&sts=e40e7004-4c8a-4963-8564-31271a8337d8&callback=' + callbackParam1 + '&_=' + callbackParam2
    url_checkin = 'https://club.lenovo.com.cn/sign'
    signlist = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': myCookie,
        'referer': 'https://club.lenovo.com.cn/thread-1814833-1-1.html',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-length': '47',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': myCookie,
        'origin': 'https://club.lenovo.com.cn',
        'referer': 'https://club.lenovo.com.cn/signlist',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }

    #headersdata=json.dumps(headers)  # 如遇特殊符号（:authority: club.lenovo.com.cn，:scheme: https） 需字典数据转为json，需要使用json.dumps
    session = requests.session()
    response_userinfo = session.get(url_userinfo,headers=signlist,verify=True)
    response_signlist = session.get(url_signlist,headers=signlist,verify=True)
    token_utf8 = response_signlist.content.decode("utf-8")
    result_token = re.search('CONFIG.token\s=\s"(\\w{40})',token_utf8) #获取随机token 
    myToken = result_token.group()[-40:]
    result_userinfo = json.loads(response_userinfo.text.replace(callbackParam1, '')[1:-1])

    data = {
        '_token': myToken
    }

    response = session.post(url_checkin, headers=headers, data=data) #json=headers 转为json解决headers特殊符号':authority': 'club.lenovo.com.cn',':path': '/sign',':scheme': 'https',
    result = response.content.decode("unicode_escape")# unicode编码转换为汉字
    try:
        result_checkin = json.loads(result)
        if result_checkin['code'] == 100000 :
            print('用户名:'+ str(result_userinfo['data']['username']))
            print('用户id:'+ myId)
            print('签到成功，本次获得' + str(result_checkin['data']['data']['add_yb_tip']))
            print('已持续签到' + str(result_checkin['data']['signCal']['continue_count']) + '天')
            print('已累计获得延保' + str(result_checkin['data']['signCal']['user_yanbao_score']) + '天')
        elif result_checkin['code'] == 100001 :
            print('用户名:'+ str(result_userinfo['data']['username']))
            print('用户id:'+ myId)
            print(str(result_checkin['msg']))
        else:
            print ('签到失败')
    except ValueError:
        print ('网页打开失败，非json')