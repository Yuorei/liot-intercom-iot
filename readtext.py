from gtts import gTTS
import pygame
import os


def readText(txt):
    tts =gTTS(text=txt,lang="ja")

    tts.save(r'communication.mp3')
    storefile ="communication.mp3"
    
    pygame.mixer.init()    # 初期設定
    pygame.mixer.music.load(storefile)     # 音楽ファイルの読み込み
    pygame.mixer.music.play(1)              # 音楽の再生回数(1回)
    os.remove(storefile)

if __name__ =="__main__":
    readText("使うたに")
