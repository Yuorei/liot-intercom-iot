import face_recognition
import matplotlib.pyplot as plt
import os

def check_face():
    # 保存されている人物の顔の画像を読み込む。
    known_face_imgs = []
    # ./register_facesに保存されている写真一覧を取得
    image_path="./face/register_fases"
    register_faces = os.listdir(image_path)
    for path in register_faces:
        img = face_recognition.load_image_file(image_path+"/"+path)
        known_face_imgs.append(img)

    # 認証する人物の顔の画像を読み込む。
    face_img_to_check = face_recognition.load_image_file("visiter.jpg")


    # 顔の画像から顔の領域を検出する。
    known_face_locs = []
    for img in known_face_imgs:
        loc = face_recognition.face_locations(img, model="hog")
        known_face_locs.append(loc)
        print(loc)

    face_loc_to_check = face_recognition.face_locations(face_img_to_check, model="hog")

    # 顔の領域から特徴量を抽出する。
    known_face_encodings = []
    for img, loc in zip(known_face_imgs, known_face_locs):
        try:
            (encoding,) = face_recognition.face_encodings(img, loc)
        except ValueError:
            continue
        known_face_encodings.append(encoding)

    (face_encoding_to_check,) = face_recognition.face_encodings(
        face_img_to_check, face_loc_to_check
    )

    # 抽出した特徴量を元にマッチングを行う。
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding_to_check)
    print(matches)  # [True, False, False]
    for i,j in enumerate(matches):
        if j == True:
            #拡張子を取り外して名前だけを返す
            return os.path.splitext(register_faces[i])[0]
    return "unknown"

    # 各画像との近似度を表示する。
    # dists = face_recognition.face_distance(known_face_encodings, face_encoding_to_check)
    # print(dists)
if __name__ =="__main__":
    check_face()