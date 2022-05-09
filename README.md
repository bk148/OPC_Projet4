# Jeux d'échecs suisse
### Prerequis :
Python est installé sur votre machine :

    python -V

Vous avez le module pour les virtualenv venv :
    
    python -m venv --help
  
Installer le le cas echeant:
    
    py -m pip install --user virtualenv
    

### Une fois Python installé :
    
Créer l'environnement virtuel :`python -m venv ***nom de l'environnement***` : pour créer l'environnement virtuel --- exemple : 

    py -m venv env
    
Activer l'environnement virtuel : `***nom de l'environnement***/Scripts/activate.bat` --- exemple : 

    env/Scripts/activate.bat
    
Installer les dépendances: 

    pip install -r requirements.txt

Lancer: 

    python main.py

Générer le rapport flake8 :

    flake8 --format=html --htmldir=flake-report



