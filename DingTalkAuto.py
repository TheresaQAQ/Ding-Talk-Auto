from pymouse import PyMouse
from ctypes import *  # 获取屏幕上某个坐标的颜色
from datetime import datetime
import time
import os
import operator


def get_color(x, y):
    gdi32 = windll.gdi32
    user32 = windll.user32
    hdc = user32.GetDC(None)  # 获取颜色值
    pixel = gdi32.GetPixel(hdc, x, y)  # 提取RGB值
    r = pixel & 0x0000ff
    g = (pixel & 0x00ff00) >> 8
    b = pixel >> 16
    return [r, g, b]
def now_time():  # 获取系统时间，返回int
    time = datetime.now().strftime('%H%M')
    return int(time)
start = [829, 919, 1009, 1059, 1429, 1520]  # 上课时间
finish = [910, 959, 1049, 1140, 1510, 1600]  # 下课时间
m = PyMouse()
os.popen('C:\\Program Files (x86)\\DingDing\\DingtalkLauncher.exe') # 打开钉钉
time.sleep(1)
print('打开钉钉主程序......')
while True:
    if operator.eq(get_color(30, 20), [0, 112, 244]):  # 判断是否打开钉钉
        print('成功打开钉钉')
        time.sleep(1) # 钉钉菜单需要加载，等待一秒
        break
    else:
        print('程序未打开')
        break
while True:
    if operator.eq(get_color(89, 116), [255, 203, 99]) and operator.eq(get_color(90, 116), [255, 203, 225]):  # 判断直播是否直播
        # 如果正在直播
        print('正在直播......')
        if operator.eq(get_color(998, 253), [237, 241, 244]):  # 是否已经进入直播间
            print('正在观看直播......')
            time.sleep(30)
        else:
            print('加入直播......')
            m.click(89, 116)
            time.sleep(30)
    else:
        # 如果没有直播
        # 判断当前时间是否下课
        for i in range(len(start)-1):
            if finish[i] < now_time() < start[i+1]:
                print('已下课')
                diff_time = (int(str(start[i + 1])[:-2])*3600 + int(str(start[i + 1])[-2:])*60) - (int(str(now_time())[:-2])*3600 + int(str(now_time())[-2:])*60)
                print(diff_time, 's后上课')
                time.sleep(diff_time)
                break
        # 如果没有直播
        # 判断当前时间是否上课
        for i in range(len(start)):
            if start[i] < now_time() < finish[i]:
                print('上课时间未直播...')
                time.sleep(10)
                break