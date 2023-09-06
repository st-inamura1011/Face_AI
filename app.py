import streamlit as st
import numpy as np
from PIL import Image, ImageDraw
import cv2
import os
import face_effect
import face_recognition
from utility import *

st.header("Face_AI TEST APP")
src = st.file_uploader('加工したい画像をアップロードしてください')
if src:
    img_path = os.path.join("./tmp/", src.name)
    # 画像を保存する
    with open(img_path, 'wb') as f:
        f.write(src.read())
        f.close()

if src:
    bar = st.progress(0)
    # 画像を読み込む。
    # img = face_recognition.load_image_file(img_path)
    img = cv2.imread(img_path)
    bar.progress(20)
    # 画像から顔の領域を検出する。
    loc = face_recognition.face_locations(img, model="cnn", number_of_times_to_upsample=2)
    bar.progress(40)

    # 関数実行
    # draw_face_locations(img, loc)
    bar.progress(80)

    # 画像の表示
    dst = face_effect.pixelate_area(img, loc, ratio=0.1)
    pil_img = Image.fromarray(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
    pil_img.save('./tmp/test.png')
    bar.progress(100)

    col1, col2 = st.columns(2)

    with col1:
        st.header("Before")
        st.image(src, use_column_width=True)

    with col2:
        st.header("After")
        st.image("./tmp/test.png", use_column_width=True)

    download_img(st, "./tmp/test.png")
