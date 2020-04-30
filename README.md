[TOC]

# 钉钉自动化

## 背景

**刚学**Python没多久，所以技术上是肯定有问题的，希望大佬能提出意见

现在还在上高一，马上开学了，所以估计以后会很少上GitHub的

## 用途

钉钉自动上课挂机，后期可能加入按+1回答问题假装在线😁

## 使用方法

### 安装pyautogui库

CMD命令 **pip install pyautogui**

![Image text](https://github.com/TheresaQAQ/PictureWarehouse/blob/master/DingTalkAuto/1588185085372.png)

### 填写配置文件

#### 填写上、下课时间

24小时制，用空格分开

![Image text](https://github.com/TheresaQAQ/PictureWarehouse/blob/master/DingTalkAuto/1588184969233.png)

#### 钉钉安卓路径

右键桌面快捷方式，打开**属性**，复制红框

![Image text](https://github.com/TheresaQAQ/PictureWarehouse/blob/master/DingTalkAuto/1588184430290.png)

稍加修改后填进去

![Image text](https://github.com/TheresaQAQ/PictureWarehouse/blob/master/DingTalkAuto/1588184506761.png)

**注意:** 去掉 **‘’**，把  **单反斜杠** 改成  **双反斜杠**

#### 钉钉群头像路径

##### 截图

先看两张图

![Image text](https://github.com/TheresaQAQ/PictureWarehouse/blob/master/DingTalkAuto/1588165524658.png)

![Image text](https://github.com/TheresaQAQ/PictureWarehouse/blob/master/DingTalkAuto/1588165556638.png)

不难看出进入钉钉群和离开钉钉群的**背景色不一样**

为了判断是否进入群，所以需要这两种情况的截图

![Image text](https://github.com/TheresaQAQ/PictureWarehouse/blob/master/DingTalkAuto/1588184222044.png)

##### 填写路径

把图片路径填进去，记得后缀名 

**注意:** 把  **单反斜杠** 改成  **双反斜杠**

![Image text](https://github.com/TheresaQAQ/PictureWarehouse/blob/master/DingTalkAuto/1588184143381.png)

## 特别说明

源代码里的**Sign_in_QQ** 和 **send_Auto_In_QQ()** 是用来自动在QQ群签到的，不需要请删除

默认情况下已经把它注释了
