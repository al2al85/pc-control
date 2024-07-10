# Utilise une image de base Python
FROM python:3.9-slim

# Définit le répertoire de travail
WORKDIR /server

# Copie le fichier requirements.txt et installe les dépendances
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie le code de l'application
COPY . .

EXPOSE 5000

# Commande par défaut pour exécuter le script (elle peut être remplacée par la commande dans docker-compose.yml)
CMD ["python", "src/server.py"]
