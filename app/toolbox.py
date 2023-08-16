import keras
import tensorflow as tf
import librosa
import numpy as np
from skimage.transform import resize


model = keras.models.load_model('../BadBoyModelV2.keras')

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
    # result_label = ""

    # for i in range(len(genres)):
    #     actual = res[0][i]
    #     if actual > actual_best:
    #         actual_best = actual
    #         result_label = genres[i]

    predicted_class_index = np.argmax(res[0])
    predicted_class_name = genres[predicted_class_index]
    predicted_class_name

    return predicted_class_name