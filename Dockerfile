# Utilisez une image Python légère comme base
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt
COPY .  /app


# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 8080 pour Cloud Run
EXPOSE 8080



ENV BUCKET_NAME="bucket_localnote"
ENV GOOGLE_APPLICATION_CREDENTIALS="/vagrant/app/cicd-sa-key.json"

# Commande pour démarrer l'application
CMD ["python", "app_bucket.py"]
