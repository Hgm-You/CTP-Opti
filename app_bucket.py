import os
from flask import Flask, jsonify
from google.cloud import storage

app = Flask(__name__)

# Récupérer les variables d'environnement
BUCKET_NAME = os.getenv("BUCKET_NAME", "bucket_localnote")
GOOGLE_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "/vagrant/app/cicd-sa-key.json")

# Initialiser Google Cloud Storage
storage_client = storage.Client.from_service_account_json(GOOGLE_CREDENTIALS)
bucket = storage_client.bucket(BUCKET_NAME)

@app.route('/')
def home():
    return "Bienvenue sur mon application Flask hébergée sur GCP!"

@app.route('/app/<variable>')
def hello(variable):
    return f"Hello, {variable} from GCP!"

@app.route('/upload/<filename>')
def upload_file(filename):
    """Upload un fichier vide dans le Bucket."""
    blob = bucket.blob(filename)
    blob.upload_from_string("Fichier créé depuis Flask", content_type="text/plain")
    return jsonify({"message": f"Fichier {filename} uploadé dans {BUCKET_NAME}"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
