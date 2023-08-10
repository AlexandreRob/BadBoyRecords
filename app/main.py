import keras
import numpy as np
from PIL import Image
import librosa # Pour l'extraction des features et la lecture des fichiers wav
import librosa.display # Pour récupérer les spectrogrammes des audio
import librosa.feature
import streamlit as st
from io import BytesIO
import tensorflow as tf
from skimage.transform import resize

model = keras.models.load_model('BadBoyModel.keras')

genres = ['blues', 'classical', 'country', 'disco', 'hiphop', 
        'jazz', 'metal', 'pop', 'reggae', 'rock']

st.write("""
    # Bad Boy Records
""")

uploaded_file = st.file_uploader("Upload an song")
if uploaded_file is not None:
    bytes_data = uploaded_file.read()

    y, sr = librosa.load(uploaded_file, mono=True)
    # Compute the spectrogram of the audio file
    spectrogram = np.abs(librosa.stft(y))
    # Resize the spectrogram to match the input shape of the model
    input_shape = (128, 660)
    spectrogram = resize(spectrogram, input_shape)
    # Reshape the spectrogram to match the expected input shape of the model
    spectrogram = np.expand_dims(spectrogram, axis=-1)
    spectrogram = np.expand_dims(spectrogram, axis=0)
    #Voici la liste des genres musicaux représentés dans la notre base de données, on en compte 10.
    # Make a prediction with the preprocessed audio
    predictions = model.predict(spectrogram)
    # Get the predicted class index
    predicted_class_index = np.argmax(predictions[0])

    # Get the name of the predicted class
    predicted_class_name = genres[predicted_class_index]

    # Get the predicted class
    predicted_class = np.argmax(predictions[0])
    # Display the name of the predicted class
    print(f'The predicted class is: {predicted_class_name}')
    st.audio(bytes_data, format="audio/wav")
    st.write(predicted_class_name)