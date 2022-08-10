from bell import bell
from readjson import readJson
from voice_record import record
from readtext import readText
import time
from datetime import datetime
url="https://aizuhack-liot-intercom-ifcy7nlzda-an.a.run.app"
stop_time=10
while 1:
    base=time.time()

    bell(url)#インターホンの音を検知
    while time.time()-base<stop_time:
        readText("住人に伝えたいことをおっしゃってください")
        recode_time=record(url)#訪問者の音声を録音してサーバーに送信
        
        if recode_time!=False:
            base=recode_time
        
        txt=readJson(url)#送られてきたJSONのテキストを戻り値として受け取る
        if txt != False :
            readText(txt)#音声の読み上げ
            time.sleep(5)
            base=time.time()
        
    
