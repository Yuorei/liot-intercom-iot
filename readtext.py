from gtts import gTTS
# import pygame
import pyaudio
import wave
import os
import time
import pydub

def readText(txt):
    tts =gTTS(text=txt,lang="ja")
    tempFile = 'communication.mp3'
    tts.save(tempFile)
    audio: pydub.AudioSegment = pydub.AudioSegment.from_mp3(tempFile)
    
    pa = pyaudio.PyAudio()
    stream = pa.open(audio.frame_rate, audio.channels, pyaudio.get_format_from_width(audio.sample_width), output=True, output_device_index=1)

    # 音声の再生が終了するまで待つ
    print('メッセージを読み上げ中: ', txt)
    stream.write(audio.raw_data)
    
    stream.close()
    pa.terminate()
    print('メッセージの読み上げ完了')
    os.remove(tempFile)

if __name__ =="__main__":
    readText("使うたに")
