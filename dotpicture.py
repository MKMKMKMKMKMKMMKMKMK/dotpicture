import streamlit as st
from PIL import Image

def image_to_dot_art(image, pixel_size=10):
    # 画像を縮小してピクセル化する
    small_image = image.resize(
        (image.width // pixel_size, image.height // pixel_size), 
        Image.NEAREST
    )
    
    # ピクセル化された画像を元のサイズにリサイズする
    dot_art_image = small_image.resize(
        (image.width, image.height), 
        Image.NEAREST
    )
    
    return dot_art_image

# Streamlitアプリケーションのタイトル
st.title('ドット絵変換アプリ')

# ファイルアップローダーの作成
uploaded_file = st.file_uploader("画像をアップロードしてください", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # 画像を読み込む
    image = Image.open(uploaded_file)

    # ドット絵に変換するピクセルサイズの選択
    pixel_size = st.slider('ピクセルサイズを選択してください', min_value=1, max_value=30, value=10)

    # ドット絵に変換
    dot_art_image = image_to_dot_art(image, pixel_size)

    # 画像を表示
    st.image(dot_art_image, caption='変換後のドット絵', use_column_width=True)

    # 画像を保存するオプション
    if st.button('画像を保存'):
        dot_art_image.save('dot_art_image.png')
        st.success('画像を保存しました！')


