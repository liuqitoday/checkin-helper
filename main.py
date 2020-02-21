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
    title_smzdm = '***什么值得买***\n\n'
    smzdmCookies = config_raw.get('SMZDM', 'cookies')
    result_smzdm =smzdm.checkin(smzdmCookies)
    #print (result_smzdm)
    title_lenovo = '\n\n***联想社区***\n\n'
    lenovoclubCookies = config_raw.get('LENOVOCLUB','cookies')
    #print ("联想社区")
    result_lenovo  = lenovoclub.checkin(lenovoclubCookies)
    return (title_smzdm + result_smzdm + title_lenovo +result_lenovo)
    # V2EX
    # v2exCookies = config_raw.get('V2EX', 'cookies')
    # v2ex.checkin(v2exCookies)

def pushWechat(desp):
    config_cfg = 'config.cfg'
    config_raw = configparser.RawConfigParser()
    config_raw.read(config_cfg)
    ssckey = config_raw.get('SEVERCHAN', 'SCKEY')
    print (desp)
    send_url='https://sc.ftqq.com/' + ssckey + '.send'
    params = {
        'text': '签到提醒'+ time.strftime('%Y-%m-%d %H:%M:%S'),
        'desp': desp
    }
    requests.post(send_url,params=params)

if __name__ == "__main__":
    pushWechat(doCheckin())