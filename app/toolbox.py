import keras
import librosa
import soundfile as sf
import numpy as np
from skimage.transform import resize
import matplotlib.pyplot as plt
import os


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
    
    return file_name  # Retourner le chemin du fichier audio


def create_img(mel_specs,name_pred):
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