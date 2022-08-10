#coding:utf-8

import speech_recognition as sr
import requests
from datetime import datetime
import time

def record(url):
    count=0
    r = sr.Recognizer()
    mic = sr.Microphone()
    voice=""
    print("Say something ...")

    with mic as source:
        r.adjust_for_ambient_noise(source) #雑音対策
        try:
            audio = r.listen(source,timeout=20)
        except sr.WaitTimeoutError:
            return False
    print ("Now to recognize it...")

    try:
        voice=r.recognize_google(audio, language='ja-JP')
        print(voice)
        todaytime=datetime.utcnow()
        tstr=todaytime.isoformat()
        r=requests.post(url+"/intercom/text",json={"id":"liot","datetime":tstr,"text":voice})
        print("text",r)
        return time.time()
    # 以下は認識できなかったときに止まらないように。
    except sr.UnknownValueError:
        print("could not understand audio")
        return False
    

if __name__=="__main__":
	record("https://eaeb-61-116-102-131.jp.ngrok.io")
