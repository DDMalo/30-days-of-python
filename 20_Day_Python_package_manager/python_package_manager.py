import requests
url = "https://restcountries.com/v3.1/all?fields=name,population,languages,area,capital"
response = requests.get(url)
paises = response.json()
print(f"Total de países: {len(paises)}")

# 2. Usa una API de países para obtener todos los datos y encuentra los 10 países más poblados.
top_10 = sorted(paises, key=lambda x: x.get("population", 0), reverse=True)[:10]
print("Lista de los 10 paises mas poblados: ")
for i, pais in enumerate(top_10, 1):
    print(f"{i}. {pais["name"]["common"]} con un total de {pais["population"]:,} habitantes")

# 3. Encuentra todos los países cuyo idioma oficial sea inglés (código 'eng') a partir de los datos de la API.
lista_eng = [pais for pais in paises if "eng" in pais.get("lenguages", {})]
print(f"He encontrado {len(lista_eng)} paises. Mostrando 5:")
for pais in lista_eng[:5]:
    print(f"{pais['name']['common']}")

# 4. A partir de los datos de la API, encuentra los 10 países con mayor superficie.
top_10_sup = sorted(paises, key=lambda x: x.get("area", 0), reverse=True)[:10]
print("Lista de paises con mayor suprficie: ")
for i, pais in enumerate(top_10_sup, 1):
    print(f"{i}. {pais["name"]["common"]} con una superficie de {pais["area"]:,}")

# 5. Encuentra todos los países recién listados (o filtrados según la API) y ordénalos por capital.
def obtener_capital(pais):
    capitales = pais.get('capital', [])
    if capitales:
        return capitales[0] 
    return "" 

paises_ordenados_capital = sorted(paises, key=obtener_capital)
for i, pais in enumerate(paises_ordenados_capital, 1):
    print(f"{i}. {pais["name"]["common"]} ")