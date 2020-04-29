import pyautogui, os, time, sys, configparser
from datetime import datetime


#输入的字符串转换为列表
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

#自动发送QQ消息 个人需求
def send_Auto_In_QQ(message):
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

#在QQ群中签到 个人需求
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
            pyautogui.moveTo(pyautogui.locateOnScreen('pic\\live2.png'), duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(1676, 1059, duration=0.5)
            pyautogui.click()

#进入直播间
def Enter_the_Live_Room():
    if pyautogui.locateOnScreen('pic\\live2.png') != None:
        pyautogui.moveTo(pyautogui.locateOnScreen('pic\\live2.png'), duration=0.5)
        pyautogui.click()
    else:
        pyautogui.moveTo(pyautogui.locateOnScreen('pic\\live.png'), duration=0.5)
        pyautogui.moveRel(200,100)
        pyautogui.click()

# 获取系统时间，返回字典
def now_time():
    time = {}
    time['hour'] = int(datetime.now().strftime('%H'))
    time['minute'] = int(datetime.now().strftime('%M'))
    time['second'] = int(datetime.now().strftime('%S'))
    return time

#将24小时制转换为秒
def get_second(x):
    return int(x['hour'] * 3600 + x['minute']*60 +x['second'])


def main():
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')
    startTime = StrT0List(config.get('Time', 'startTime'))
    finishTime = StrT0List(config.get('Time', 'finishTime'))
    path_DT = config.get('Path', 'DingTalk')
    path_OutDT = config.get('Path', 'OutDt')
    path_InDT = config.get('Path', 'InDT')

    #打开钉钉
    os.popen(path_DT)
    print('打开钉钉主程序......')
    time.sleep(3)

    #进入钉钉群
    while True:

        #如果已经进入钉钉群
        if pyautogui.locateOnScreen(path_InDT) != None:
            break

        #如果没有进入钉钉群
        else:
            pyautogui.moveTo(pyautogui.locateOnScreen(path_OutDT), duration=0.5)
            pyautogui.click()
            pyautogui.moveRel(100, 100)



    while True:
        try:
            #如果正在直播
            if pyautogui.locateOnScreen('pic\\live.png') or pyautogui.locateOnScreen('pic\\LiveWindows.png') or pyautogui.locateOnScreen('pic\\live2.png')  != None:
                print('正在直播...')

                #如果已经进入直播间
                if pyautogui.locateOnScreen('pic\\WatchLive.png') != None:
                    print('已进入直播间...')
                    time.sleep(15)

                #如果没有进入直播间
                else:
                    print('未进入直播间，正在加入...')
                    Enter_the_Live_Room()

            #如果没有直播
            else:
                #现在时间是否下课
                for i in range(len(startTime) - 1):
                    if get_second(finishTime[i]) < get_second(now_time()) < get_second(startTime[i+1]):
                        diff_time = int(get_second(startTime[i + 1]) - get_second(now_time()))
                        print('已下课!',diff_time,'S后上课')
                        if diff_time >= 600:
                            time.sleep(diff_time - 600)
                            #Sign_in_QQ() # 个人需要，不需要请删除
                            time.sleep(600)
                        elif 30 < diff_time < 600:
                            #Sign_in_QQ() # 个人需要，不需要请删除
                            time.sleep(diff_time-30)
                        else:
                            #Sign_in_QQ() # 个人需要，不需要请删除
                            time.sleep(diff_time)
                        break

                #现在时间是否上课
                for i in range(len(startTime)):
                    if get_second(startTime[i]) < get_second(now_time()) < get_second(finishTime[i]):
                        print('上课时间未直播...')
                        time.sleep(5)
                        break

                #特殊情况
                if get_second(startTime[0]) > get_second(now_time()):
                    diff_time = get_second(startTime[0]) - get_second(now_time())
                    print('已下课!', diff_time, 'S后上课')

                    #距离上课还有十分钟以上
                    if diff_time >= 600:
                        time.sleep(diff_time - 600)
                        #Sign_in_QQ() # 个人需要，不需要请删除
                        time.sleep(600)

                    #距离上课还有30秒以上但不足十分钟
                    elif 30 < diff_time < 600:
                        #Sign_in_QQ() # 个人需要，不需要请删除
                        time.sleep(diff_time - 30)

                    #距离上课不足30秒
                    else:
                        #Sign_in_QQ() # 个人需要，不需要请删除
                        time.sleep(diff_time)
                if get_second(now_time()) > get_second(finishTime[-1]):
                    print('今天没课了，你看尼玛呢') # 嘤嘤嘤
        except:
            print('error')
            time.sleep(10)

if __name__ == "__main__":
    main()
