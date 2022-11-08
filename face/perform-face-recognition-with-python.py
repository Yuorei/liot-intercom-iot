import face_recognition
import matplotlib.pyplot as plt
import os

# 保存されている人物の顔の画像を読み込む。
known_face_imgs = []
# ./register_facesに保存されている写真一覧を取得
image_path="./register_fases"
register_faces = os.listdir(image_path)
for path in register_faces:
    img = face_recognition.load_image_file(image_path+"/"+path)
    known_face_imgs.append(img)

# 認証する人物の顔の画像を読み込む。
face_img_to_check = face_recognition.load_image_file("face_to_check.jpg")
# チェックした画像を削除
#os.remove("face_to_check.jpg")

# 顔の画像から顔の領域を検出する。
known_face_locs = []
for img in known_face_imgs:
    loc = face_recognition.face_locations(img, model="hog")
    known_face_locs.append(loc)

face_loc_to_check = face_recognition.face_locations(face_img_to_check, model="hog")


# 検出した顔の位置を画像に描画する。
def draw_face_locations(img, locations):
    fig, ax = plt.subplots()
    ax.imshow(img)
    ax.set_axis_off()
    for i, (top, right, bottom, left) in enumerate(locations):
        w, h = right - left, bottom - top
        ax.add_patch(plt.Rectangle((left, top), w, h, ec="r", lw=2, fill=None))
    #plt.show()#PC画面に画像表示


for img, loc in zip(known_face_imgs, known_face_locs):
    draw_face_locations(img, loc)

draw_face_locations(face_img_to_check, face_loc_to_check)

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

# 各画像との近似度を表示する。
dists = face_recognition.face_distance(known_face_encodings, face_encoding_to_check)
print(dists)