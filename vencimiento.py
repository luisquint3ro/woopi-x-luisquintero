"""Decide que pagina se publica: la propuesta o el aviso de vencimiento.
Cuenta dias habiles (lunes a viernes, sin festivos de propuesta.json) desde fecha_envio."""
import json, shutil, os, datetime as dt
cfg = json.load(open("propuesta.json", encoding="utf-8"))
inicio = dt.date.fromisoformat(cfg["fecha_envio"])
festivos = {dt.date.fromisoformat(d) for d in cfg.get("festivos", [])}
d, contados = inicio, 0
while contados < cfg["dias_habiles"]:
    d += dt.timedelta(days=1)
    if d.weekday() < 5 and d not in festivos:
        contados += 1
ultimo_dia = d
hoy = dt.datetime.now(dt.timezone(dt.timedelta(hours=-5))).date()
os.makedirs("_site", exist_ok=True)
if hoy > ultimo_dia:
    shutil.copy("expirada.html", "_site/index.html")
    print(f"Propuesta vencida (ultimo dia: {ultimo_dia}). Se publica el aviso.")
else:
    shutil.copy("index.html", "_site/index.html")
    print(f"Propuesta activa hasta el {ultimo_dia} inclusive.")
