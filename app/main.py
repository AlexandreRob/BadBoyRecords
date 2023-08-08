import streamlit as st
import numpy as np
from PIL import Image
from io import BytesIO
import numpy as np
import tensorflow as tf
import keras
import librosa

model = keras.models.load_model('BadBoyModel.keras')

st.write("""
    # Bad Boy Records
""")

uploaded_file = st.file_uploader("Upload an song")
if uploaded_file is not None:
    bytes_data = uploaded_file.read()

    music_load = librosa.core.load(bytes_data)

    results = model.predict(music_load)

    st.audio(bytes_data, format="audio/wav")
    st.write('Prediction: ')