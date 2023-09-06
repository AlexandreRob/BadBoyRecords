# Utiliser une image de base Python 3.9
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet dans le répertoire de travail
COPY . .

# Installer les dépendances du projet
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Exposer le port 8501
EXPOSE 8501

# Teste si l'exposition fonctionne ou pas
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health


# Exécuter le script principal lors du démarrage du conteneur
ENTRYPOINT ["streamlit", "run", "./app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]