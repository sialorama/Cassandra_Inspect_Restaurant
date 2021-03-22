from flask import Flask, render_template, request, jsonify
from data import DataAccess as da

app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template("accueil.html")

#infos d'un restaurant
@app.route("/infos_resto/<int:id_resto>", methods=['GET'])
def infos_resto(id_resto):
    da.connexion()
    data = da.infos_resto(id_resto)

    return jsonify(data), 200

#liste des restaurants pour un type de cuisine
@app.route("/liste_cuisine/<cuisine_type>", methods=['GET'])
def liste_cuisine(cuisine_type):
    da.connexion()
    data = da.liste_cuisine(cuisine_type)

    return jsonify(data), 200

#compte des inspections dans un restaurant
@app.route("/compte_inspections/<int:id_resto>", methods=['GET'])
def compte_inspections(id_resto):
    da.connexion()
    data = da.compte_inspections(id_resto)

    return jsonify(data), 200

#dix premiers restaurants d'un certain grade
@app.route("/premiers_restos/<grade>", methods=['GET'])
def premiers_restos(grade):
    da.connexion()
    data = da.premiers_restos(grade)

    return jsonify(data), 200

#lancement de l'app
if __name__ == "__main__" :
    app.run(debug=True, port=5001)