import keras
import tensorflow as tf
import pandas as pd # Pour le dataframe
from skimage.transform import resize
import numpy as np # Pour la normalisation et calculs de moyenne
import matplotlib.pyplot as plt # Pour la visualisation
import librosa # Pour l'extraction des features et la lecture des fichiers wav
import librosa.display # Pour récupérer les spectrogrammes des audio
import librosa.feature
import seaborn as sns








model = keras.models.load_model('BadBoyModel.keras')

y, sr = librosa.load(audio_file, mono=True)