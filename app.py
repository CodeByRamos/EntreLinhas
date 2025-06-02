from flask import Flask, render_template, request, redirect, url_for
from db import init_db

app = Flask(__name__)

# Lista temporária de desabafos
desabafos = []

@app.route("/")
def exibir_feed_de_desabafos():
    return render_template("feed.html", desabafos=desabafos)

@app.route("/enviar", methods=["POST"])
def receber_novo_desabafo():
    conteudo = request.form.get("conteudo")
    if conteudo:
        if len(conteudo) > 500:
            return "Seu desabafo é muito importante, mas por favor, tente resumir em até 500 caracteres"
    desabafos.append(conteudo.strip())
    return redirect(url_for("exibir_feed_de_desabafos"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
