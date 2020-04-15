import pyautogui
import os
import time
from datetime import datetime



def StrT0List(str):
    list = []
    while str != '':
        time = {}
        a = str.find(':')
        time['hour'] = int(str[:a])
        time['minute'] = int(str[:a + 3][-2:])
        time['second'] = 0
        list.append(time)
        str = str[a + 4:]
    return list

def send_Auto_In_QQ(message = '39'): # 自动发送QQ消息
    while True:
        if pyautogui.locateOnScreen('pic\\SendKey.png') != None:
            send_key = pyautogui.locateOnScreen('pic\\SendKey.png')
            pyautogui.moveTo(send, duration=0.5)
            pyautogui.moveRel(-50, -50)
            pyautogui.click()
            pyautogui.typewrite(message, interval=0.25)
            pyautogui.moveTo(send_key, duration=1)
            pyautogui.click()
            break
        else:
            time.sleep(2)

def live():
    pyautogui.moveTo(pyautogui.locateOnScreen('pic\\live.png'), duration=0.5)
    pyautogui.click()

def now_time():  # 获取系统时间，返回列表
    time = {}
    time['hour'] = int(datetime.now().strftime('%H'))
    time['minute'] = int(datetime.now().strftime('%M'))
    time['second'] = int(datetime.now().strftime('%S'))
    return time

def get_second(x):
    return x['hour'] * 3600 + x['minute']*60 +x['second']

def main():
    startTime = StrT0List('8:29 9:19 10:09 10:59 14:29 15:20')
    finishTime = StrT0List('9:10 9:59 10:49 11:40 15:10 16:00')
    os.popen('C:\\Program Files (x86)\\DingDing\\DingtalkLauncher.exe')  # 打开钉钉
    print('打开钉钉主程序......')
    time.sleep(1)
    while True:
        if pyautogui.locateOnScreen('pic\\live.png') != None:
            print('正在直播...')
            if pyautogui.locateOnScreen('pic\\WatchLive.png') != None:
                print('已进入直播间...')
                time.sleep(15)
            else:
                print('未进入直播间，正在加入...')
                live()
        else:
            for i in range(len(startTime) - 1):
                if get_second(finishTime[i]) < get_second(now_time()) < get_second(startTime[i+1]):
                    diff_time = get_second(startTime[i+1]) - get_second(now_time())
                    print('已下课!',diff_time,'S后上课')
                    time.sleep(diff_time-30)
                    break
            for i in range(len(startTime)):
                if get_second(startTime[i]) < get_second(now_time()) < get_second(finishTime[i]):
                    print('上课时间未直播...')
                    time.sleep(10)
                    break

if __name__ == "__main__":
    main()