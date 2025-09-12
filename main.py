from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista global para almacenar los nombres
nombres = []

@app.route("/")
def index():
    return render_template("index.html", nombres=nombres)

@app.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form.get("nombre")
    if nombre:
        nombres.append(nombre)
    return redirect(url_for("index"))

@app.route("/atender")
def atender():
    if nombres:
        nombres.pop(0)  # Elimina el primer nombre de la lista
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)