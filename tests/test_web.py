from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Servidor funcionando correctamente"

if __name__ == '__main__':
    app.run(debug=True)