import requests

BASE = "http://127.0.0.1:5000"

# Consultar el endpoint de bajo stock
respuesta = requests.get(f"{BASE}/materiales/bajo-stock")
print("Código de estado:", respuesta.status_code)

# Convertir el JSON en un objeto de Python (diccionario)
datos = respuesta.json()
print(f"Materiales que requieren reabastecimiento: {datos['total']}\n")

for m in datos["materiales"]:
    print(f"- {m['nombre']}: {m['existencias']} {m['unidad']} "
          f"(mínimo {m['stock_minimo']})")
