import requests
import time
import json
import configparser

# 判断页面是否登陆正确返回json
def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError:
        return False
    return True

def checkin(myCookie,myToken):
    url_checkin = 'https://club.lenovo.com.cn/sign'
    headers = {
        'origin': 'https://club.lenovo.com.cn',
        'Referer': 'https://club.lenovo.com.cn/signlist',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        ':authority': 'club.lenovo.com.cn',
        ':path': '/sign',
        ':scheme': 'https',
        'cache-control': 'max-age=0',
        'x-requested-with': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Cookie': myCookie
    }

    data = {
        '_token': myToken
    }
    
    #headersdata=json.dumps(headers)  # 如遇特殊符号（:authority: club.lenovo.com.cn，:scheme: https） 需字典数据转为json，需要使用json.dumps
    session = requests.session()
    response = session.post(url_checkin, json=headers, data=data, verify=True) #json=data 转为json解决headers特殊符号
    if is_json(response.text) == "True":
        #response.content.decode("unicode_escape") # 编码转换为汉字
        result = json.loads(response.text)
        if result['code'] == 100000 :
            print('联想社区签到成功，累计获得延保' + str(result['msg'],result['data']['signCal']['user_yanbao_score']) + '天')
        elif result['code'] == 100001 :
            print('签到失败:' + str(result['msg']))
        else:
            print('签到失败:' + str(result['msg']))
    else:
        print('签到失败:非Json格式')