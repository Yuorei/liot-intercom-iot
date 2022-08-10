#インターホンの音の検知

#!/usr/bin/env python

# ライブラリの読込
import pyaudio
import wave
import numpy as np
from datetime import datetime
import requests
import time
from camera import cap

def bell(url):
    # 音データフォーマット
    chunk = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 2

    # 閾値
    threshold = 0.1

    # 音の取込開始
    p = pyaudio.PyAudio()
    stream = p.open(format = FORMAT,
        channels = CHANNELS,
        rate = RATE,
        input = True,
        frames_per_buffer = chunk
    )



    while True:
        # 音データの取得
        data = stream.read(chunk)
        # ndarrayに変換
        x = np.frombuffer(data, dtype="int16") / 32768.0

        # 閾値以上の場合はファイルに保存
        if x.max() > threshold:
            todaytime=datetime.utcnow()
            tstr=todaytime.isoformat()
            r=requests.post(url+"/intercom/notice",json={"id":"liot","datetime":tstr})
            print("notice",r)
            print(tstr)
            cap(url)
            break

    stream.close()
    p.terminate()
