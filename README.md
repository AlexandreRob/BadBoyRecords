# BadBoyRecords

## Sommaire :
1. [Technologies utilisées](#1technologies-utilisées)
2. [Création de l'environnement virtuel](#2création-de-lenvironement-virtuel-à-ne-faire-quune-fois)
3. [Activation de l'environnement virtuel](#3activation-de-lenvironement-virtuel)
    1. [Désactivation de l'environnement virtuel](#désactivation-de-lenvironement-virtuel) (Optionnel)
    2. [Installation des dépendances dans l'environnement virtuel](#installation-des-dépendances-dans-lenvironnement-virtuel)
4. [Arborescence de l'application](#4arborescence-de-lapplication)
5. [Choix du modèle](#5choix-du-modèle)

___


## 1.Technologies utilisées :
- [keras](https://keras.io/)
- [numpy](https://www.numpy.org/)
- [Python](https://www.python.org/downloads/release/python-3912/)
- [streamlit](https://streamlit.io/)
- [Tensorflow](https://www.tensorflow.org/)
- [JupiterNotebook](https://jupyter.org/)


### 2.Création de l'environement virtuel (à ne faire qu'une fois):
Ce dernier nous permettra d'installer toutes les dépendances du projet
```sh
python -m venv ./venv
```
### 3.Activation de l'environement virtuel
```sh
.\venv\Scripts\activate
```
### Désactivation de l'environement virtuel
```sh
deactivate
```
### Installation des dépendances dans l'environnement virtuel
```sh
pip install -r requirements.txt
```
___
### 4.Arborescence de l'application
<details>
<summary>BadBoyRecords</summary>

- **app**
    - main.py
- **Data**
    - genres_original
    - images_original
    - features_3_sec.csv
    - features_30_sec.csv
- **venv**
- **BadBoyModel.keras**
- **classification_music.ipynb**
- **README.md**
- **requirements.txt**
</details>

### 5.Choix du modèle
