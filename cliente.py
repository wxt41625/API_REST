import requests

BASE = "http://127.0.0.1:5000"

respuesta = requests.get(f"{BASE}/materiales/bajo-stock")
print("Código de estado:", respuesta.status_code)

datos = respuesta.json()
print(f"Materiales que requieren reabastecimiento: {datos['total']}\n")

for m in datos["materiales"]:
    print(f"- {m['nombre']}: {m['existencias']} {m['unidad']} "
          f"(mínimo {m['stock_minimo']})")
