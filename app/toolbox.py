import os
import keras
import shutil
import librosa
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from skimage.transform import resize


model = keras.models.load_model('./BadboyModelV2.h5')

#Voici la liste des genres musicaux représentés dans la notre base de données, on en compte 10.
genres = ['blues', 'classical', 'country', 'disco', 'hiphop', 
          'jazz', 'metal', 'pop', 'reggae', 'rock']



def model_pred(audio_file):
    y, sr = librosa.load(audio_file)
   
    mel_specs = []
    # y = audio_file[0]
    # sr = audio_file[1]

    spect = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=2048, hop_length=1024)
    spect = librosa.power_to_db(spect, ref=np.max)

    # On modifie la taille des images 128 x 660 en gardant les paramètres proposés dans l'article initial
    if spect.shape[1] != 600:
        # spect.resize(128,660, refcheck=False)
        spect = spect[:128,:600]
        # print(spect.shape)
        spect.reshape(128,600)

    mel_specs.append(spect)
        
    X = np.array(mel_specs)

    res = model.predict(X)

    # actual_best = 0
    # result_genre = ""

    # for i in range(len(genres)):
    #     actual = res[0][i]
    #     if actual > actual_best:
    #         actual_best = actual
    #         result_genre = genres[i]

    predicted_class_index = np.argmax(res[0])
    predicted_class_name = genres[predicted_class_index]
    predicted_class_name

    return predicted_class_name, mel_specs


def save_song(audio_file, name_pred, genre):
    # Charger l'audio
    y, sr = librosa.load(audio_file, sr=None)  # sr=None garantit que le taux d'échantillonnage d'origine est conservé
    
    # Créer un répertoire pour sauvegarder les fichiers audio, s'il n'existe pas
    upload_directory = f"folder_audio/{genre}"
    if not os.path.exists(upload_directory):
        os.makedirs(upload_directory)
        
    # Construire le chemin du fichier où l'audio sera sauvegardé
    file_name = os.path.join(upload_directory, f"{name_pred}.wav")
    
    # Utiliser soundfile pour enregistrer l'audio au format WAV
    sf.write(file_name, y, sr)
    
    # Enregistrer une copie du fichier audio dans la structure de dossiers "Data/genres_original"
    save_to_genre_folder(file_name, f"{name_pred}.wav", genre)

    return file_name  # Retourner le chemin du fichier audio


def save_to_genre_folder(audio_file_path, file_name, genre):
    # Chemin de base pour le dossier "Data"
    base_path = "Data"
    
    # Chemin pour le dossier "genres_original"
    genres_original_path = os.path.join(base_path, "genres_original")
    
    # Chemin pour le genre spécifique
    genre_path = os.path.join(genres_original_path, genre)
    
    # Vérifier et créer les dossiers s'ils n'existent pas
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    if not os.path.exists(genres_original_path):
        os.makedirs(genres_original_path)
    if not os.path.exists(genre_path):
        os.makedirs(genre_path)
    
    # Construire le chemin complet où le fichier sera sauvegardé
    destination_path = os.path.join(genre_path, file_name)
    
    # Copier le fichier audio dans le dossier de destination
    shutil.copy2(audio_file_path, destination_path)
    
    return destination_path  # Retourner le chemin du fichier audio copié


def create_img(mel_specs, name_pred):
    upload_directory = "folder_img"
    if not os.path.exists(upload_directory):
        os.makedirs(upload_directory)
        
    # Creation img
    plt.imshow(mel_specs[0], cmap="inferno")

    # path
    nom_fichier = f"folder_img/{name_pred}.png"

    plt.savefig(nom_fichier)
    plt.close()


def create_full_spectrogram(audio_file, name_pred, genre):
    # Charger l'audio
    y, sr = librosa.load(audio_file)
    
    # Calculer le spectrogramme
    spect = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=2048, hop_length=1024)
    spect = librosa.power_to_db(spect, ref=np.max)
    
    # Créer un répertoire pour sauvegarder les images du spectrogramme, s'il n'existe pas
    upload_directory = f"folder_full_spectrogram/{genre}"
    if not os.path.exists(upload_directory):
        os.makedirs(upload_directory)
        
    # Créer et sauvegarder l'image du spectrogramme
    plt.figure(figsize=(10, 4))
    plt.imshow(spect, aspect='auto', cmap='inferno', origin='lower')
    plt.tight_layout()
    
    # Sauvegarder l'image
    file_name = os.path.join(upload_directory, f"{name_pred}.png")
    plt.savefig(file_name)
    plt.close()
    
    return file_name  # Retourner le chemin du fichier image


def new_train():
    model = keras.models.load_model('../BadBoyModelV2.keras')
    # model.fit(X_combined, y_combined, epochs=epochs, batch_size=batch_size, validation_split=validation_split)