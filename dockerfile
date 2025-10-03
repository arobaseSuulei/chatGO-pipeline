# Utilise Python 3.11
FROM python:3.11

# Crée un dossier pour l'app
WORKDIR /app

# Copie requirements.txt et installe toutes les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code
COPY . .

# commande pour lancer Jupyter Lab au démarrage
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
