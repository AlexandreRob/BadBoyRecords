import streamlit as st
from toolbox import *
import tempfile
import os



st.write("""
    # Bad Boy Records
""")

uploaded_file = st.file_uploader("Upload an song", type=["wav"])
if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")
    
    predict = model_pred(uploaded_file)

    st.write(predict)