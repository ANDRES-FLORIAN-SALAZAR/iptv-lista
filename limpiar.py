import re, requests, os

# 1. Descargar lista original desde iptv-org
url = "https://iptv-org.github.io/iptv/index.category.m3u"
resp = requests.get(url)
entrada = "index.category.m3u"
with open(entrada, "w", encoding="utf-8") as f:
    f.write(resp.text)

# 2. Limpiar resolución y priorizar español
salida = "lista_espanol.m3u"
nuevas_lineas = []
canales_vistos = {}

with open(entrada, "r", encoding="utf-8") as f:
    lineas = f.readlines()

for linea in lineas:
    if linea.startswith("http"):
import re, requests, os

# 1. Descargar lista original desde iptv-org
url = "https://iptv-org.github.io/iptv/index.category.m3u"
resp = requests.get(url)
entrada = "index.category.m3u"
with open(entrada, "w", encoding="utf-8") as f:
    f.write(resp.text)

# 2. Limpiar resolución y priorizar español
salida = "lista_espanol.m3u"
nuevas_lineas = []
canales_vistos = {}

with open(entrada, "r", encoding="utf-8") as f:
    lineas = f.readlines()

for linea in lineas:
    if linea.startswith("http"):
        url_sin_res = re.sub(r"[?&](resolution|quality)=[^&]+", "", linea).rstrip("&")
        canal_id = re.sub(r"[?&](audio|track|lang)=[^&]+", "", url_sin_res)

        if canal_id in canales_vistos:
            if ("audio=spa" in url_sin_res or "lang=es" in url_sin_res):
                idx = nuevas_lineas.index(canales_vistos[canal_id])
                nuevas_lineas[idx] = url_sin_res
                canales_vistos[canal_id] = url_sin_res
            continue
        else:
            canales_vistos[canal_id] = url_sin_res
            nuevas_lineas.append(url_sin_res)
    else:
        nuevas_lineas.append(linea)

with open(salida, "w", encoding="utf-8") as f:
    f.writelines(nuevas_lineas)

print("✅ Lista en español creada:", salida)

# 3. Subir a GitHub (requiere autenticación previa con gh auth login)
os.system("git init")
os.system("git branch -M main")
os.system("git remote add origin https://github.com/usuario/iptv-lista.git")
os.system("git add lista_espanol.m3u")
os.system("git commit -m 'Lista adaptativa en español'")
os.system("git push -u origin main")        url_sin_res = re.sub(r"[?&](resolution|quality)=[^&]+", "", linea).rstrip("&")
        canal_id = re.sub(r"[?&](audio|track|lang)=[^&]+", "", url_sin_res)

        if canal_id in canales_vistos:
            if ("audio=spa" in url_sin_res or "lang=es" in url_sin_res):
                idx = nuevas_lineas.index(canales_vistos[canal_id])
                nuevas_lineas[idx] = url_sin_res
	                canales_vistos[canal_id] = url_sin_res
            continue
        else:
            canales_vistos[canal_id] = url_sin_res
            nuevas_lineas.append(url_sin_res)
    else:
        nuevas_lineas.append(linea)

with open(salida, "w", encoding="utf-8") as f:
    f.writelines(nuevas_lineas)

print("✅ Lista en español creada:", salida)

# 3. Subir a GitHub (requiere autenticación previa con gh auth login)
os.system("git init")
os.system("git branch -M main")
os.system("git remote add origin https://github.com/usuario/iptv-lista.git")
os.system("git add lista_espanol.m3u")
os.system("git commit -m 'Lista adaptativa en español'")
os.system("git push -u origin main")

