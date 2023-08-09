# Utiliser une image de base Python 3.9
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet dans le répertoire de travail
COPY app/main.py app/main.py
COPY app/toolbox.py app/toolbox.py
COPY Data/ Data/
COPY BadBoyModel.keras BadBoyModel.keras
COPY requirements.txt requirements.txt

# Installer les dépendances du projet
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Exécuter le script principal lors du démarrage du conteneur
CMD ["python", "app/main.py"]