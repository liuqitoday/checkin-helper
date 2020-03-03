# -*- coding: utf-8 -*-
import configparser
import time
import requests
import random
import re
import json
import smzdm
import lenovoclub
import huaweiclub

#联想签到cookies含有特殊符号"，需替换后json方可loads
def doReplace():
    try:
        with open('config.json', mode='r' ,encoding='utf-8') as f_oldfile:
            f_newfile = open('config_bak.json', 'w', encoding='utf-8')
            for line in f_oldfile :
                if 'cerpreg-passport="' in line :
                    line = re.sub(r'cerpreg-passport="','cerpreg-passport=\\"',line)
                    line = re.sub(r'==\|"','==|\\"',line)
                f_newfile.write(line)
            f_oldfile.close()
            f_newfile.close()
    except IOError :
        print ('config.json不存在')

#配置多账户
def loadConfig(website,usercookies):
    doReplace()
    try:
        with open('config_bak.json', 'r', encoding='utf-8') as f:
            dict_config= json.loads(f.read())
            global sckey #获取sckey，定义severchan通道sckey为全局变量，以便pushwechat调用
            sckey = dict_config['SEVERCHAN']
            cookies_list = dict_config[website]
            i = 0
            datalist = []
            for item in cookies_list:
                i += 1
                try:
                    cookies = item[usercookies]
                except KeyError as e:
                    print('第%d个账户实例配置出错，跳过该账户' % i, e)
                    continue
                if website == "LENOVOCLUB":
                    result_lenovo = lenovoclub.checkin(cookies)
                    datalist.append(result_lenovo)
                elif website == "SMZDM":
                    result_smzdm = smzdm.checkin(cookies)
                    datalist.append(result_smzdm)
                elif website == "HUAWEICLUB":
                    result_huaweiclub = huaweiclub.checkin(cookies)
                    datalist.append(result_huaweiclub)
                else :
                    print ("other")
            return (datalist)
    except ValueError as e:
        print ('config.json载入错误', e)
    except json.JSONDecodeError as e:
        print('config.json格式有误', e)

def pushWechat(desp):
    send_url='https://sc.ftqq.com/' + sckey + '.send'
    params = {
        'text': '签到提醒'+ time.strftime('%Y-%m-%d %H:%M:%S'),
        'desp': desp
    }
    requests.post(send_url,params=params)

if __name__ == "__main__":
    lenovoclub_desp = loadConfig('LENOVOCLUB','cookies')
    smzdz_desp  = loadConfig('SMZDM','cookies')
    #loadConfig('HUAWEICLUB','cookies')
    result_desp = "***联想社区***\n\n" + ''.join(lenovoclub_desp) + "***什么值得买***\n\n" + ''.join(smzdz_desp)
    pushWechat(result_desp)