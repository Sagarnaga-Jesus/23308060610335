from flask import Flask, render_template,request,redirect

app = Flask(__name__)

alimentos=[]


@app.route("/")
def formulario():
    return render_template("formulario.html")

@app.route("/resultado",methods=["POST","GET"])
def resultado():
    if  request.method == ["POST"]:
        nombre = request.form["nombre"]
        grasas = request.form["grasas"]
        prote = request.form["proteinas"]
        carbo = request.form["carbohidratos"]
        
        grasa=0
        proteinas=0
        carbohidratos=0
        
        
        alimentos.append({
            "nombre": nombre ,
            "grasas": grasas ,
            "proteinas": prote ,
            "carbohidratos":carbo ,
            
        })
        
        grasa = 8*float(grasas)
        proteinas = 4*float(prote)
        carbohidratos = 4*float(carbo)
        
        
        
    return render_template("resultado.html", nombre=nombre, grasa=grasa, proteinas=proteinas, carbohidratos=carbohidratos)


if __name__ == '__main__':
    app.run(debug=True)