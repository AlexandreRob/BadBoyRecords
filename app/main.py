import streamlit as st
import numpy as np
from PIL import Image
from io import BytesIO
import numpy as np
import tensorflow as tf
from skimage.transform import resize
from toolbox import *
import tempfile
import os



st.write("""
    # Bad Boy Records
""")

uploaded_file = st.file_uploader("Upload an song")
if uploaded_file is not None:
    bytes_data = uploaded_file.read()

    # Créer un fichier temporaire pour enregistrer les données binaires du fichier audio
    temp_audio_file = tempfile.NamedTemporaryFile(delete=False)
    temp_audio_file.write(bytes_data)
    temp_audio_file.close()
    
    predicted_class_name = model_pred(temp_audio_file.name)

    # Supprimer le fichier temporaire
    os.remove(temp_audio_file.name)
    

    st.audio(bytes_data, format="audio/wav")
    st.write(predicted_class_name)