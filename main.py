# -*- coding: utf-8 -*-
import configparser
import time
import requests
import random
import smzdm
import lenovoclub

def doCheckin():
    config_cfg = 'config.cfg'
    config_raw = configparser.RawConfigParser()
    config_raw.read(config_cfg)
    # 什么值得买
    smzdmCookies = config_raw.get('SMZDM', 'cookies')
    print ("什么值得买")
    smzdm.checkin(smzdmCookies)
    # 联想社区
    lenovoclubCookies = config_raw.get('LENOVOCLUB','cookies')
    lenovoclubToken = config_raw.get('LENOVOCLUB','token')
    lenovoclubId = config_raw.get('LENOVOCLUB','lenovoid')
    print ("联想社区")
    lenovoclub.checkin(lenovoclubCookies,lenovoclubToken,lenovoclubId)
    # V2EX
    # v2exCookies = config_raw.get('V2EX', 'cookies')
    # v2ex.checkin(v2exCookies)

def pushWechat(desp):
    config_cfg = 'config.cfg'
    config_raw = configparser.RawConfigParser()
    config_raw.read(config_cfg)
    ssckey = config_raw.get('SEVERCHAN', 'SCKEY')
    #print (desp)
    send_url='https://sc.ftqq.com/' + ssckey + '.send'
    params = {
        'text': '签到提醒'+ time.strftime('%Y-%m-%d %H:%M:%S'),
        'desp': desp
    }
    requests.post(send_url,params=params)

if __name__ == "__main__":
    doCheckin()
    #pushWechat(doCheckin())