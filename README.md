# base_rover
建立基本的農業機器人環境
* * *

## 流程圖
>實線部分為完成的項目，虛線部分為農業機器人的核心功能，需依據個人需求自行開發
![image](https://github.com/bz-lin/base_rover/blob/master/rover%E5%9F%BA%E7%A4%8E%E5%8A%9F%E8%83%BD%E6%B5%81%E7%A8%8B%E5%9C%96.svg)

## 硬體架構
>可以自行添加模組，來增加功能
![image](https://github.com/bz-lin/base_rover/blob/master/rover%E5%9F%BA%E7%A4%8E%E7%A1%AC%E9%AB%94%E6%9E%B6%E6%A7%8B.svg)

## 環境架設
* 系統安裝
>到官方網站下載[Raspibian Stretch Lite](http://downloads.raspberrypi.org/raspbian/images/raspbian-2019-04-09/) image檔案
使用[rufus](https://rufus.ie/)軟體，將image檔案燒入至SD卡
* 網路設定
>由於我們的rover與monitor要在同一個區域網路內工作，因此要設定在同一個wifi網路。
成功開機後，啟動終端機，並且輸入

        $sudo raspi-config
        
並選2 Network Options -> N2 Wi-fi 輸入SSID與密碼後，即可

        
* 測試

