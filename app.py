from flask import Flask

app = Flask(__name__)

# Route d'accueil pour éviter l'erreur 404 sur "/"
@app.route('/')
def home():
    return "Bienvenue sur mon application Flask hébergée sur GCP!"

# Route dynamique pour afficher un message personnalisé
@app.route('/app/<variable>')
def hello(variable):
    return f"Hello, {variable} from GCP!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
