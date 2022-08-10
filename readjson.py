import json
import requests
def readJson(url):
    url_get=url+"/intercom/get-message?id=liot"
    r = requests.get(url_get)
    print("get-message",r)
    jsonData=r.json()
    print("GETを受信できたかどうか",jsonData['exist'])
    if jsonData['exist']==True:
        txt=jsonData["text"]
        print("送られてきた返信内容　",txt)
        return txt
    elif jsonData['exist']==False:
        return False