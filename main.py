import configparser
import smzdm
import time
import random


def doCheckin():
    config_cfg = 'config.cfg'
    config_raw = configparser.RawConfigParser()
    config_raw.read(config_cfg)
    # SMZDM
    smzdmCookies = config_raw.get('SMZDM', 'cookies')
    smzdm.checkin(smzdmCookies)


if __name__ == "__main__":
    while True:
        doCheckin()
        sleepSecs = 60 * 60 * 24 + random.randint(1, 500)
        print('下次执行时间' + str(sleepSecs) + '秒后')
        time.sleep(sleepSecs)
