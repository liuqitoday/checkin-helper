import requests
import time
import json
import configparser


def checkin(myCookie):
    callbackParam1 = 'jQuery112400443448018717687_' + str(int(round(time.time() * 1000)))
    callbackParam2 = str(int(round(time.time() * 1000)))
    callbackParam3 = 'jQuery1124011488749104352869_' + str(int(round(time.time() * 1000)))
    url_checkin = 'https://zhiyou.smzdm.com/user/checkin/jsonp_checkin?callback=' + callbackParam1 + '&_=' + callbackParam2
    url_username = 'https://zhiyou.smzdm.com/user/info/jsonp_get_current?callback=' + callbackParam3 + '&_=' + callbackParam2
    headers = {
        'Host': 'zhiyou.smzdm.com',
        'Referer': 'https://www.smzdm.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Cookie': myCookie
    }
    session = requests.session()
    response = session.get(url_checkin, headers=headers, verify=True)
    usernameresponse = session.get(url_username, headers=headers, verify=True)
    # print(response.content.decode("unicode_escape"))
    # print(response.text.replace(callbackParam1, '')[1:-1])
    result = json.loads(response.text.replace(callbackParam1, '')[1:-1])
    usernameresult = json.loads(usernameresponse.text.replace(callbackParam3, '')[1:-1])
    #print (usernameresult)
    if result['error_code'] == 0:
        #print('签到成功' + '\n' + '用户id：' + str(usernameresult['smzdm_id']) + '\n' + '用户名：' + str(usernameresult['nickname']) + '\n' +'已连续签到' + str(result['data']['checkin_num']) + "天")
        result = '签到成功' + '\n\n' + '用户id：' + str(usernameresult['smzdm_id']) + '\n\n' + '用户名：' + str(usernameresult['nickname']) + '\n\n' +'已连续签到' + str(result['data']['checkin_num']) + "天\n\n---\n\n"
    else:
        #print('签到失败')
        result = ('签到失败\n\n---\n\n')
    return result