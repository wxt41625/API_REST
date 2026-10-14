from flask import Flask, jsonify

app = Flask(__name__)

materiales = [
    {"id": 1, "nombre": "Cable UTP Cat6 (bobina)", "categoria": "cable",
     "unidad": "metros", "existencias": 120, "stock_minimo": 100},
    {"id": 2, "nombre": "Conector RJ45", "categoria": "conector",
     "unidad": "piezas", "existencias": 18, "stock_minimo": 50},
    {"id": 3, "nombre": "Jack Keystone Cat6", "categoria": "conector",
     "unidad": "piezas", "existencias": 40, "stock_minimo": 40},
    {"id": 4, "nombre": "Pinzas ponchadoras RJ45", "categoria": "herramienta",
     "unidad": "piezas", "existencias": 6, "stock_minimo": 4},
    {"id": 5, "nombre": "Probador de cable de red", "categoria": "herramienta",
     "unidad": "piezas", "existencias": 2, "stock_minimo": 3},
    {"id": 6, "nombre": "Canaleta adhesiva", "categoria": "accesorio",
     "unidad": "metros", "existencias": 35, "stock_minimo": 20},
    {"id": 7, "nombre": "Clips para cable", "categoria": "accesorio",
     "unidad": "paquetes", "existencias": 3, "stock_minimo": 10},
]


@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "Bienvenido a CableTrack API",
        "estado": "La API funciona correctamente",
        "endpoints": [
            "/materiales",
            "/materiales/<id>",
            "/materiales/categoria/<categoria>",
            "/materiales/bajo-stock",
        ],
    })


@app.route("/materiales")
def listar_materiales():
    return jsonify({"total": len(materiales), "materiales": materiales})


@app.route("/materiales/bajo-stock")
def materiales_bajo_stock():

    bajos = [m for m in materiales if m["existencias"] <= m["stock_minimo"]]
    return jsonify({"total": len(bajos), "materiales": bajos})


@app.route("/materiales/<int:id>")
def obtener_material(id):
    for m in materiales:
        if m["id"] == id:
            return jsonify(m)
    return jsonify({"error": f"No existe un material con id {id}"}), 404


@app.route("/materiales/categoria/<categoria>")
def materiales_por_categoria(categoria):
    resultado = [m for m in materiales
                 if m["categoria"].lower() == categoria.lower()]
    return jsonify({"categoria": categoria,
                    "total": len(resultado),
                    "materiales": resultado})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
