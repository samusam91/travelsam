from app import app

# Definizione delle route dell'applicazione
@app.route('/')
@app.route('/index')
def index():
    return "Benvenuto su travelsam!"

@app.route('/about')
def about():
    return "Informazioni su travelsam"
