import streamlit as st
from toolbox import *
import tempfile
import os



st.write("""
    # Bad Boy Records
""")

uploaded_file = st.file_uploader("Upload an song", type=['wav','mp3'])
if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")
    
    predict = model_pred(uploaded_file)
        
    st.write(predict[0])

    agree = st.checkbox("Si la prédiction n'est pas bonne clique")

    if agree:
        genre = st.radio("Choisir à quel genre appartient la musique", genres)
        
        if genres :
            
            st.write(f'Le genre selectionner est: {genre}.')
            if st.button('envoyer le resultat'):
                create_img(predict[1],uploaded_file.name)
                # create_song(uploaded_file)
        else:
            st.write("Selectionner un genre.")