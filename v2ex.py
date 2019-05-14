import requests
import re


def checkin(myCookies):
    headers = {
        'referer': 'https://www.v2ex.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'cookie': myCookies
    }
    
    url_daily = 'https://www.v2ex.com/mission/daily'

    session = requests.session()
    response = session.get(url_daily, headers=headers, verify=True)
    #print(response.text)
    result = re.search('/mission/daily/redeem\?once=(\\d*)', response.text)
    if result:
        onece = result.group(1)
        url_checkin = 'https://www.v2ex.com/mission/daily/redeem?once=' + str(onece)
        print(url_checkin)
        session.get(url_checkin, headers=headers, verify=True)

    response_checkin = session.get('https://www.v2ex.com/mission/daily', headers=headers, verify=True)
    #print(response_checkin.text)
    result_checkin = re.search(r'已连续登录 (\d*) 天', response_checkin.text)
    if result_checkin:
        print('V2EX' + result_checkin.group(0))
    else:
        print('V2EX签到异常')
