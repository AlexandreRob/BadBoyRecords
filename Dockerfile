# Utiliser une image de base Python 3.9
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Install dependencies
RUN pip install wheel
COPY ./requi_docker.txt requi_docker.txt
RUN pip install --no-cache-dir -r requi_docker.txt
EXPOSE 8501

# Copier les fichiers du projet dans le répertoire de travail
COPY . .

ENTRYPOINT ["streamlit", "run"]

# Run the Django development server
CMD ["main.py"]