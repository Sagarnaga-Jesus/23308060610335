from flask import Flask, render_template,request,redirect

app = Flask(__name__)

alimentos=[
    {
        "nombre": "Manzana",
        "grasas": "0.2",
        "proteinas": "0.3",
        "carbohidratos": "14",
        "agua": "0.85"
    }
]


@app.route("/")
def formulario():
    return render_template("formulario.html")

@app.route("/resultado",methods=["POST","GET"])
def resultado():
    if  request.method == ["POST"]:
        nombre = request.form["alimento"]
        grasas = request.form["grasas"]
        prote = request.form["proteinas"]
        carbo = request.form["carbohidratos"]
        agua = request.form["agua"]
        
        grasa=0
        proteinas=0
        carbohidratos=0
        
        grasa = 9*float(grasas)
        proteinas = 4*float(prote)
        carbohidratos = 4*float(carbo)
        
        
        grasat = str(grasa)
        proteinast = str(proteinas)
        carbohidratost = str(carbohidratos)
        alimentos.append({
            "nombre": nombre ,
            "grasas": grasas ,
            "proteinas": prote ,
            "carbohidratos":carbo ,
            "grasasc":grasat,
            "proteinasc":proteinast,
            "carbohidratosc":carbohidratost
        })
        
        
    return render_template("resultado.html", alimentos=alimentos,)


if __name__ == '__main__':
    app.run(debug=True)