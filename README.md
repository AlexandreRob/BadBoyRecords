# BadBoyRecords

## Sommaire :
1. [Technologies utilisées](#1technologies-utilisées)
2. [Création de l'environnement virtuel](#2création-de-lenvironement-virtuel-à-ne-faire-quune-fois)
3. [Activation de l'environnement virtuel](#3activation-de-lenvironement-virtuel)
    1. [Désactivation de l'environnement virtuel](#désactivation-de-lenvironement-virtuel) (Optionnel)
    2. [Installation des dépendances dans l'environnement virtuel](#installation-des-dépendances-dans-lenvironnement-virtuel)
    3. [Lancement de l'application streamlit](#lancement-de-lapplication-streamlit)
    4. [Lancement de l'application sous Docker](#lancement-de-lapplication-sous-docker)
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

### Lancement de l'application streamlit
```sh
streamlit run .\app\main.py
```

### Lancement de l'application sous Docker
Il sera accessible à cette adresse `http://localhost:8501/`
```sh
docker run -d -p 8501:8501 badboyrecords:image
```
___
### 4.Arborescence de l'application ci-dessous :

---
<details>
<summary>BadBoyRecords</summary>

- **app**
    - main.py
    - toolbox.py
- **Data**
    - genres_original
    - images_original
    - features_3_sec.csv
    - features_30_sec.csv
- **venv**
- **BadBoyModel.keras**
- **classification_music.ipynb**
- **Dockerfile**
- **README.md**
- **requi_docker_.txt**
</details>

---

### 5.Choix du modèle
Nous avons un tableau venant du Notebook de Googlecolab ci-dessous:

|Modèle| Score |
|-----:|-----------|
|  SVM  | 17.5% |
| k-nn  | 29%   |
| RF  | 59.2%   |
| XGB  | 57.6%  |
| Neural Net | 60.8% |
| CNN  | 60.8% |

Le modèle avec le plus haut score, [CNN](https://www.tensorflow.org/tutorials/images/cnn?hl=fr) à été choisit pour avoir des prédictions assez correctes.
