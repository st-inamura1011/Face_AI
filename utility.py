def download_img(st, img):
    with open(img, 'rb') as file:
        st.download_button(
            label='画像のダウンロード',
            data=file,
            file_name='download.png'
        )
