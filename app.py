import streamlit as st
from fastai import *
from fastai.vision import *
from PIL import Image

st.set_option('deprecation.showfileUploaderEncoding', False)

st.title('Maple vs Dogs')

uploaded_file = st.file_uploader("text here", type=['png', 'jpg'])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")







    #export_file_url = Path('https://drive.google.com/file/d/1PnK5-fhDRr_9xBc1PqErQTdyh_jdbXRv/view?usp=sharing')
    export_file_url_local = Path('./')

    learn = load_learner(export_file_url_local)

    img = open_image(uploaded_file)

    learn.predict(img)

    pred_class = learn.predict(img)[0].obj
    st.text(pred_class)