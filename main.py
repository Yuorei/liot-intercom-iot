from bell import bell
from readjson import readJson
from voice_record import record
from readtext import readText
import time
from datetime import datetime
import speech_recognition
import requests

url="https://aizuhack-liot-intercom-ifcy7nlzda-an.a.run.app"
stop_time=60

# === メインループ(一生ループし続ける) ===
while 1:
    print('インターホン検知待機中')
    bell(url)#インターホンの音を検知
    print('インターホン音を検知しました')
    recognizer = speech_recognition.Recognizer()
    base_time = time.time() # 一定時間何も起こらなかったら終了するための変数

    while 1:
        try:
            # 音声の録音(無音の場合はexceptへ)
            #     timeout で無音の時間を何秒まで許容するか
            #     phrase_time_limit で訪問者の発言を何秒まで許容するか指定できる
            readText("住人に伝えたいことをおっしゃってください")
            print('音声録音中')
            with speech_recognition.Microphone() as micin: # Microphone() の第一引数で、使用するマイクを指定できるらしいです
                recognizer.adjust_for_ambient_noise(micin) # ノイズ処理
                audio = recognizer.listen(micin, timeout=1, phrase_time_limit=8)
            # 音声からテキストへ変換(失敗したらexceptへ)
            print('音声をテキストへ変換中')
            voice_text = recognizer.recognize_google(audio, language='ja-JP')
            print('変換成功: ', voice_text)
            # サーバーへ送信
            r=requests.post(
                url+"/intercom/text",
                json={
                    "id": "liot",
                    "datetime": datetime.utcnow().isoformat(),
                    "text": voice_text
                }
            )
            # 終了までの猶予時間を更新
            base_time = time.time()
        except (speech_recognition.WaitTimeoutError, speech_recognition.UnknownValueError): # いずれかの例外が発生した場合
            print('失敗')
            print('サーバーからメッセージがないか確認中')
            text = readJson(url) # サーバーからのメッセージを取得(なければFalseが入る)
            if text != False:
                print('新しいメッセージを確認')
                # メッセージがあった場合はその内容を読み上げる
                readText(text)
                # 終了までの猶予時間を更新
                base_time = time.time()
            print('残り猶予時間: ', stop_time - (time.time() - base_time))
            # 最後の猶予時間更新から stop_time 秒以上経っていたらルーブを抜ける
            if time.time() - base_time > stop_time:
                print('一定時間経過したため処理を終了')
                break
            continue
