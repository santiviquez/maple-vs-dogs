import streamlit as st
from fastai import *
from fastai.vision import *
from PIL import Image
st.set_option('deprecation.showfileUploaderEncoding', False)
export_file_url_local = Path('./')

def predict(image_file):
    img = open_image(image_file)
    learn.predict(img)
    prediction = learn.predict(img)[0].obj
    return prediction


st.title('Maple not Maple')

uploaded_file = st.file_uploader("Select an image (preferably a dog one)", type=['png', 'jpg'])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Load trained model 
    learn = load_learner(export_file_url_local)
    # Get predicted class
    prediction = predict(uploaded_file)

    if prediction != 'maple':
        st.title('Not Maple :(')
    else:
        st.title('Maple!')