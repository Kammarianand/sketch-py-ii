import streamlit as st
from PIL import Image, ImageFilter, ImageChops
from io import BytesIO
import base64
import time
st.set_page_config(page_title="sketchi-py", page_icon="🎨")

st.markdown(
    f'<h1 style="color:#22ebff;">StreamlitSketchR: Magical Sketches</h1>',
    unsafe_allow_html=True
)

with st.expander("About this project 🎦"):
    st.markdown("""
        
        The application is created for fun, utilizing the Python programming language along with modules such as PIL,and Streamlit. 
        I'm fine-tuning my skills as part of my data analysis journey, and the project is still in its initial phase. 
        While it may not consistently produce accurate sketch images, I'm striving to optimize the output quality. 
        
        
        Have a great day! 🌥️ 

        [![LinkedIn](https://img.shields.io/badge/LinkedIn-Kammari%20Anand-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/kammari-anand-504512230/) 
    """)

def sketchify_img(img):
    # Convert image to grayscale
    gray_img = img.convert('L')
    # Apply inverted Gaussian blur
    blurred_img = gray_img.filter(ImageFilter.GaussianBlur(radius=21))
    inverted_blurred_img = Image.eval(blurred_img, lambda x: 255 - x)
    # Combine grayscale image and inverted blurred image using pencil sketch formula
    pencil_sketch = ImageChops.darker(gray_img, inverted_blurred_img)
    return pencil_sketch


def spinner():
    with st.spinner("please wait for some time"):
        time.sleep(2.5)

def balloons():
    for i in range(3):
        st.balloons()

def download_sketch(sketch_img):
    # Convert the PIL image to bytes
    img_bytes = BytesIO()
    sketch_img.save(img_bytes, format='PNG')
    # Return a download link for the bytes data
    return img_bytes.getvalue()

img_file = st.file_uploader("Upload your image", type=['png', 'jpeg', 'jpg'])

if st.button("Sketch Me"):
    if img_file is not None:
        img = Image.open(img_file)
        sketch_img = sketchify_img(img)
        spinner()
        st.image(sketch_img, caption="Sketch Image", use_column_width=True)
        balloons()
        sketch_img_bytes = download_sketch(sketch_img)
        st.download_button(label="Download Sketch", data=sketch_img_bytes, file_name='sketch.png', mime='image/png')
        st.balloons()
    else:
        st.error("Please upload an image.")
        st.snow()
