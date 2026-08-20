import streamlit as st<
from PIL import Image

st.title("La primera app de Juana en Streamlit")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("Facilmente puedo realizar backend y frontend")
image = Image.open("vaca.jpg")
st.image(image, caption="Interfaces Multimodales")
*
st.title("Mi primera app en streamlit")
