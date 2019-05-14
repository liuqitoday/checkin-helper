import configparser
import time
import random
import smzdm
import v2ex



def doCheckin():
    config_cfg = 'config.cfg'
    config_raw = configparser.RawConfigParser()
    config_raw.read(config_cfg)
    # SMZDM
    smzdmCookies = config_raw.get('SMZDM', 'cookies')
    smzdm.checkin(smzdmCookies)
    # V2EX
    v2exCookies = config_raw.get('V2EX', 'cookies')
    v2ex.checkin(v2exCookies)

if __name__ == "__main__":
    while True:
        doCheckin()
        sleepSecs = 60 * 60 * 24 + random.randint(1, 500)
        print('下次执行时间' + str(sleepSecs) + '秒后')
        time.sleep(sleepSecs)
