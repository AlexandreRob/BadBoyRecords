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
    
    # Créer un fichier temporaire pour sauvegarder l'audio uploadé
    tfile = tempfile.NamedTemporaryFile(delete=False) 
    tfile.write(uploaded_file.read())
    
    predict = model_pred(tfile.name)  # Utilisez le nom du fichier temporaire ici
    
    st.write(predict[0])

    agree = st.checkbox("Si la prédiction n'est pas bonne clique")

    if agree:
        genre = st.radio("Choisir à quel genre appartient la musique", genres)
        
        if genre:  # Changez ceci de `if genres:` à `if genre:`
            st.write(f'Le genre selectionner est: {genre}.')
            if st.button('envoyer le resultat'):
                create_img(predict[1], uploaded_file.name)
                create_full_spectrogram(tfile.name, uploaded_file.name, genre)  # Utilisez le nom du fichier temporaire ici