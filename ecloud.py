import requests
import urllib3
import json
import time
from xml.etree import ElementTree

urllib3.disable_warnings()

def checkin(myCookie,signature,sessionKey):
    callbackParam = str(int(round(time.time() * 1000)))
    url_checkin = 'https://api.cloud.189.cn/mkt/userSign.action?rand=' + callbackParam + '&clientType=TELEANDROID&version=8.5.4&model=NX512J'
    url_drawprize = 'https://m.cloud.189.cn/v2/drawPrizeMarketDetails.action?taskId=TASK_SIGNIN&activityId=ACT_SIGNIN&noCache=0.5355988284033437'
    url_drawprize1 = 'https://m.cloud.189.cn/v2/drawPrizeMarketDetails.action?taskId=TASK_SIGNIN_PHOTOS&activityId=ACT_SIGNIN&noCache=0.5322540734566603'
    headers = {
        'Cache-Control': 'no-cache',
        'X-Request-ID': '3b5344df-8736-4a41-8592-9b4555fba75e',
        'User-Agent': 'Ecloud/8.5.4 (NX512J; 866925020077377; qq) Android/22',
        'SessionKey': sessionKey,
        'Signature': signature,
        'Date': 'Sun, 8 Mar 2020 01:00:32 GMT',
        'Accept-Encoding': 'gzip',
        'Content-Type': 'text/xml; charset=utf-8',
        'Host': 'api.cloud.189.cn',
        'Connection': 'Keep-Alive'
    }
    
    headers_drawprize = {
        'Host': 'm.cloud.189.cn',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; NX512J Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.2661.86 Mobile Safari/537.36 Ecloud/8.5.4 Android/22 clientId/866925020077377 clientModel/NX512J imsi/null clientChannelId/qq proVersion/1.0.6',
        'Referer': 'https://m.cloud.189.cn/zhuanti/2016/sign/index.jsp?albumBackupOpened=0',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en,en-US;q=0.8',
        'Cookie': myCookie
    }
    
    headers_drawprize1 = {
        'Host': 'm.cloud.189.cn',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; NX512J Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.2661.86 Mobile Safari/537.36 Ecloud/8.5.4 Android/22 clientId/866925020077377 clientModel/NX512J imsi/null clientChannelId/qq proVersion/1.0.6',
        'Referer': 'https://m.cloud.189.cn/zhuanti/2016/sign/index.jsp?albumBackupOpened=1',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en,en-US;q=0.8',
        'Cookie': myCookie
    }
    
    session = requests.session()
    response_checkin = session.get(url_checkin,headers=headers,verify=False) #关闭校验ssl证书
    checkin_unicode = response_checkin.content.decode("utf-8")
    tree = ElementTree.fromstring(checkin_unicode)
    box = tree.find('resultTip')
    response_drawprize = session.get(url_drawprize,headers=headers_drawprize,verify=False)
    drawprize_unicode = response_drawprize.content.decode("utf-8")
    response_drawprize1 = session.get(url_drawprize1,headers=headers_drawprize1,verify=False)
    drawprize1_unicode = response_drawprize1.content.decode("utf-8")
    #drawprize_unicode ='{"activityId":"ACT_SIGNIN","description":"天翼云盘50M空间","isUsed":1,"listId":64559600,"prizeGrade":1,"prizeId":"SIGNIN_CLOUD_50M","prizeName":"天翼云盘50M空间","prizeStatus":1,"prizeType":4,"useDate":"2020-03-05T10:31:27","userId":376673451}'
    result_drawprize = json.loads(drawprize_unicode)
    result_drawprize1 = json.loads(drawprize1_unicode)
    if 'activityId' in result_drawprize:
        result = '\n\n用户id：' + str(result_drawprize['userId']) + '\n\n签到' + box.text + '\n\n一次抽奖获得:' + str(result_drawprize['description']) + '\n\n二次抽奖获得:' + str(result_drawprize1['description']) + '\n\n---\n\n'
    else :
        result = "\n\n签到抽奖失败/已签到抽奖\n\n---\n\n"
    return result