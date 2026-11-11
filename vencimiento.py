"""Publica la propuesta hasta fecha_limite (inclusive, hora de Colombia).
Despues de esa fecha publica el aviso de propuesta no disponible."""
import json, shutil, os, datetime as dt
cfg = json.load(open("propuesta.json", encoding="utf-8"))
ultimo_dia = dt.date.fromisoformat(cfg["fecha_limite"])
hoy = dt.datetime.now(dt.timezone(dt.timedelta(hours=-5))).date()
os.makedirs("_site", exist_ok=True)
if hoy > ultimo_dia or not os.path.exists("index.html"):
    shutil.copy("expirada.html", "_site/index.html")
    print(f"Se publica el aviso (ultimo dia: {ultimo_dia}).")
else:
    shutil.copy("index.html", "_site/index.html")
    print(f"Propuesta activa hasta el {ultimo_dia} inclusive.")
