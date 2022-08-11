from gtts import gTTS
import pygame
import os
import time

def readText(txt):
    tts =gTTS(text=txt,lang="ja")

    tts.save(r'communication.mp3')
    storefile ="communication.mp3"
    
    pygame.mixer.init()    # 初期設定
    pygame.mixer.music.load(storefile)     # 音楽ファイルの読み込み
    pygame.mixer.music.play(1)              # 音楽の再生回数(1回)
    # 音声の再生が終了するまで待つ
    print('メッセージを読み上げ中')
    while pygame.mixer.music.get_busy(): # get_busy() は、再生中の場合 True、そうでない場合 False を返す
        time.sleep(0.1)
    print('メッセージの読み上げ完了')
    os.remove(storefile)

if __name__ =="__main__":
    readText("使うたに")
