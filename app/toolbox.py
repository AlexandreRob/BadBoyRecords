import keras
import librosa
import numpy as np
from skimage.transform import resize



model = keras.models.load_model('BadBoyModel.keras')

#Voici la liste des genres musicaux représentés dans la notre base de données, on en compte 10.
genres = ['blues', 'classical', 'country', 'disco', 'hiphop', 
          'jazz', 'metal', 'pop', 'reggae', 'rock']

def model_pred(audio_file):

    y, sr = librosa.load(audio_file, mono=True)
    # Compute the spectrogram of the audio file
    spectrogram = np.abs(librosa.stft(y))
    # Resize the spectrogram to match the input shape of the model
    input_shape = (128, 660)
    spectrogram = resize(spectrogram, input_shape)
    # Reshape the spectrogram to match the expected input shape of the model
    spectrogram = np.expand_dims(spectrogram, axis=-1)
    spectrogram = np.expand_dims(spectrogram, axis=0)
    # Make a prediction with the preprocessed audio
    predictions = model.predict(spectrogram)
    # Get the predicted class index
    predicted_class_index = np.argmax(predictions[0])

    # Get the name of the predicted class
    predicted_class_name = genres[predicted_class_index]
    
    return predicted_class_name