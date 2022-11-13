import time
import cv2
import requests
from datetime import datetime
from face import perform_face_recognition_with_python
import base64
import os


def cap(url):
    cap=cv2.VideoCapture(0)
    time.sleep(2)
    ret,frame=cap.read()
    print("写真が撮れたかどうか",ret)
    if ret:
        cv2.imwrite("visiter.jpg", frame)
        with open("./visiter.jpg", "rb") as f:
            img = f.read()
        img_base64 = base64.b64encode(img)
        img_base64=img_base64.decode()
        todaytime=datetime.utcnow()
        tstr=todaytime.isoformat()
        print(tstr)
        # 名前を返して欲しい
        name=perform_face_recognition_with_python.check_face()
        # todo jsonにturuかfalseを返す
        r=requests.post(url+"/intercom/image",json={"id":"liot","datetime":tstr,"data":img_base64,"name":name})
        print("image",r)

if __name__ =="__main__":
    cap("https://eaeb-61-116-102-131.jp.ngrok.io")
