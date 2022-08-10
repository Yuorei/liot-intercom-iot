import base64

def base64Picture():
    with open("./visiter.jpg", "rb") as f:
        img = f.read()

    img_base64 = base64.b64encode(img)
    return img_base64
