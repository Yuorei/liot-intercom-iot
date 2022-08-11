from gtts import gTTS
# import pygame
import pyaudio
import wave
import os
import time

def readText(txt):
    tts =gTTS(text=txt,lang="ja")

    tts.save(r'communication.wav')
    storefile ="communication.wav"
    
    pa = pyaudio.PyAudio()
    stream = pa.open(44100, 2, pyaudio.paInt16, output=True, output_device_index=1)
    wav = wave.open(storefile)

    # 音声の再生が終了するまで待つ
    print('メッセージを読み上げ中: ', txt)
    while 1:
        data = wav.readframes(wav.getnframes())
        if not data:
            break
        stream.write()
    stream.close()
    wav.close()
    pa.terminate()
    print('メッセージの読み上げ完了')
    os.remove(storefile)

if __name__ =="__main__":
    readText("使うたに")
