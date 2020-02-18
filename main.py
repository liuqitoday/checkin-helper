# -*- coding: utf-8 -*-
import configparser
import time
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
    print('\n')
    # 联想社区
    lenovoclubCookies = config_raw.get('LENOVOCLUB','cookies')
    lenovoclubToken = config_raw.get('LENOVOCLUB','token')
    print ("联想社区")
    lenovoclub.checkin(lenovoclubCookies,lenovoclubToken)
    # V2EX
    # v2exCookies = config_raw.get('V2EX', 'cookies')
    # v2ex.checkin(v2exCookies)

if __name__ == "__main__":
        doCheckin()
