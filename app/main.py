import streamlit as st
import numpy as np
from PIL import Image
from io import BytesIO
import numpy as np
import tensorflow as tf
import keras
import librosa
from skimage.transform import resize

model = keras.models.load_model('BadBoyModel.keras')

st.write("""
    # Bad Boy Records
""")

uploaded_file = st.file_uploader("Upload an song")
if uploaded_file is not None:
    bytes_data = uploaded_file.read()
    

    music_load, sr = librosa.core.load(bytes_data)

    # Compute the spectrogram of the audio file
    spectrogram = np.abs(librosa.stft(music_load))

    # Resize the spectrogram to match the input shape of the model
    input_shape = (128, 660)
    spectrogram = resize(spectrogram, input_shape)

    # Reshape the spectrogram to match the expected input shape of the model
    spectrogram = np.expand_dims(spectrogram, axis=-1)
    spectrogram = np.expand_dims(spectrogram, axis=0)

    #Voici la liste des genres musicaux représentés dans la notre base de données, on en compte 10.
    genres = ['blues', 'classical', 'country', 'disco', 'hiphop', 
          'jazz', 'metal', 'pop', 'reggae', 'rock']
    
    # Make a prediction with the preprocessed audio
    results = model.predict(spectrogram)

    # Get the predicted class index
    predicted_class_index = np.argmax(results[0])

    # Get the name of the predicted class
    predicted_class_name = genres[predicted_class_index]

    # Get the predicted class
    predicted_class = np.argmax(results[0])

    st.audio(bytes_data, format="audio/wav")
    st.write(predicted_class_name)