from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World Silvio"

if __name__ == '__main__':
    app.run()