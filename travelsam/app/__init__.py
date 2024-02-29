import sys
import os

# Ottieni il percorso assoluto della directory corrente
current_dir = os.path.dirname(os.path.abspath(__file__))
# Aggiungi il percorso della directory del progetto al percorso di ricerca dei moduli
sys.path.append(os.path.dirname(current_dir))

from flask import Flask

# Creazione dell'oggetto Flask
app = Flask(__name__)

# Configurazioni dell'applicazione Flask
app.config['SECRET_KEY'] = 'il_tuo_segreto'

# Import delle route dall'altro file
from app import routes

