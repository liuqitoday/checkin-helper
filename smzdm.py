import requests
import time
import json
import configparser


def checkin(myCookie):
    callbackParam1 = 'jQuery11240676892179874939_' + str(int(round(time.time() * 1000)))
    callbackParam2 = str(int(round(time.time() * 1000)))
    url_checkin = 'https://zhiyou.smzdm.com/user/checkin/jsonp_checkin?callback=' + callbackParam1 + '&_=' + callbackParam2
    headers = {
        'Host': 'zhiyou.smzdm.com',
        'Referer': 'https://zhiyou.smzdm.com/user/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'Cookie': myCookie
    }
    session = requests.session()
    response = session.get(url_checkin, headers=headers, verify=True)
    # print(response.content.decode("unicode_escape"))
    # print(response.text.replace(callbackParam1, '')[1:-1])
    result = json.loads(response.text.replace(callbackParam1, '')[1:-1])
    if result['error_code'] == 0:
        print('什么值得买签到成功, 已经连续签到' + str(result['data']['checkin_num']) + "天")
    else:
        print('什么值得买签到失败')
