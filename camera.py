import time
import cv2
import requests
from datetime import datetime
import base64
import os


def cap(url):
    cap=cv2.VideoCapture(0)
    time.sleep(2)
    ret,frame=cap.read()
    print("写真が撮れたかどうか",ret)
    cv2.imwrite("visiter.jpg", frame)
    with open("./visiter.jpg", "rb") as f:
        img = f.read()
    img_base64 = base64.b64encode(img)
    img_base64=img_base64.decode()
    todaytime=datetime.utcnow()
    tstr=todaytime.isoformat()
    print(tstr)
    r=requests.post(url+"/intercom/image",json={"id":"liot","datetime":tstr,"data":img_base64})
    print("image",r)
    os.remove("visiter.jpg")
if __name__ =="__main__":
    cap("https://eaeb-61-116-102-131.jp.ngrok.io")
