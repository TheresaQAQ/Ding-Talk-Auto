import pyautogui, os, time,sys
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

def send_Auto_In_QQ(message): # 自动发送QQ消息
    while True:
        if pyautogui.locateOnScreen('pic\\sendKey.png') != None:
            send_key = pyautogui.locateOnScreen('pic\\sendKey.png')
            pyautogui.moveTo(send_key, duration=0.5)
            pyautogui.moveRel(-50, -50)
            pyautogui.click()
            pyautogui.typewrite(message, interval=0.25)
            pyautogui.moveTo(send_key, duration=0.1)
            pyautogui.click()
            break
        else:
            time.sleep(1)

def Sign_in_QQ(message = '39'):
    while True:
        if pyautogui.locateOnScreen('pic\\QQGroupStatus2.png') != None:
            send_Auto_In_QQ(message=message)
            break
        elif pyautogui.locateOnScreen('pic\\QQGroupStatus1.png') != None:
            pyautogui.moveTo(pyautogui.locateOnScreen('pic\\QQGroupStatus1.png'), duration=0.5)
            pyautogui.click()
            send_Auto_In_QQ(message=message)
            break
        else:
            pyautogui.moveTo(1676, 1059, duration=0.5)
            pyautogui.click()

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
    startTime = StrT0List('8:30 9:20 10:10 11:00 14:30 15:20')
    finishTime = StrT0List('9:10 10:00 10:50 11:40 15:10 16:00')
    os.popen('C:\\Program Files (x86)\\DingDing\\DingtalkLauncher.exe')  # 打开钉钉
    print('打开钉钉主程序......')
    while True:
        while True:
            if pyautogui.locateOnScreen('pic\\DingTalkGroupStatus2.png') != None:
                break
            else:
                pyautogui.moveTo(pyautogui.locateOnScreen('pic\\DingTalkGroupStatus1.png'),duration=0.5)
                pyautogui.click()
                pyautogui.moveRel(100,100)
        try:
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
                        diff_time = get_second(startTime[i + 1]) - get_second(now_time())
                        print('已下课!',diff_time,'S后上课')
                        if diff_time >= 600:
                            time.sleep(diff_time - 600)
                            Sign_in_QQ()
                            time.sleep(600)
                        elif 30 < diff_time < 600:
                            Sign_in_QQ()
                            time.sleep(diff_time-30)
                        else:
                            Sign_in_QQ()
                            time.sleep(diff_time)
                        break
                for i in range(len(startTime)):
                    if get_second(startTime[i]) < get_second(now_time()) < get_second(finishTime[i]):
                        print('上课时间未直播...')
                        time.sleep(10)
                        break
                if get_second(startTime[i]) > get_second(now_time()):
                    diff_time = get_second(startTime[i + 1]) - get_second(now_time())
                    print('已下课!', diff_time, 'S后上课')
                    Sign_in_QQ()
                    if diff_time > 30:
                        time.sleep(diff_time - 30)
                    else:
                        time.sleep(diff_time)
                if get_second(now_time()) > get_second(finishTime[-1]):
                    print('今天没课了，你看尼玛呢')
        except:
            print('error')

if __name__ == "__main__":
    main()