import re
# ---- Nivel 1 ----
# 1. ¿Qué es una expresión regular?
# R: Es una secuencia de caracteres que forma un patrón de búsqueda. 
# Se usa para verificar si un string contiene un patrón específico, 
# para extraer datos o para reemplazar partes de un texto.

# 2. ¿Qué es una variable de expresión regular (regex variable)?
# R: En Python, solemos escribir los patrones como "Raw Strings" (cadenas crudas) 
# poniendo una 'r' delante (ej: patron = r'\d+'). Esto le dice a Python que ignore 
# los caracteres de escape normales (como \n) y trate el string literalmente.
# También puede referirse a un patrón "compilado" usando re.compile() para reutilizarlo.

#3. Recrea patrones:
texto = "Hola que tal talent hoy es 22-04-2020 reading being"
patron_talent = r"talent"
patron_fecha = r"\b\d{2}-\d{2}-\d{4}\b"
patron_ing = r"\b\w+ing\b"
print(re.findall(patron_talent, texto, re.I))
print(re.findall(patron_fecha, texto, re.I))
print(re.findall(patron_ing, texto, re.I))

# ---- Nivel 2 ----
# 1. Validar un nombre de variable en Python
def validacion(texto):
    patron = r"\b[a-zA-Z_]\w*\b"
    return bool(re.match(patron, texto))
print(validacion("3hola"))
print(validacion("hola"))

# 2. Limpiar etiquetas HTML
text = '''
HTML
Hypertext Markup Language (HTML) is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets (CSS) and scripting languages such as JavaScript.

Web browsers receive HTML documents from a web server or from local storage and render the documents into multimedia web pages. HTML describes the structure of a web page semantically and originally included cues for the appearance of the document.

HTML elements are the building blocks of HTML pages. With HTML constructs, images and other objects such as interactive forms may be embedded into the rendered page. HTML provides a means to create structured documents by denoting structural semantics for text such as headings, paragraphs, lists, links, quotes and other items. HTML elements are delineated by tags, written using angle brackets. Tags such as <img /> and <input /> directly introduce content into the page. Other tags such as <p> surround and provide information about document text and may include other tags as sub-elements. Browsers do not display the HTML tags, but use them to interpret the content of the page.

HTML can embed programs written in a scripting language such as JavaScript, which affects the behavior and content of web pages. Inclusion of CSS defines the look and layout of content. The World Wide Web Consortium (W3C), former maintainer of the HTML and current maintainer of the CSS standards, has encouraged the use of CSS over explicit presentational HTML since 1997.
'''
patron_HTML = r"<[^<]+>"
texto_limpio = re.sub(patron_HTML, "", text)
print(texto_limpio)

# ---- Nivel 3 ----
# 1. Limpiar texto 
paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''
patron_l = r"[^\w\s]"
limpio = re.sub(patron_l, "", paragraph)
palabras = limpio.split()

contar = {}
for i in palabras:
    contar[i] = contar.get(i, 0) + 1

print(contar)
top3 = sorted(contar.items(), key=lambda x: x[1], reverse=True)[:3]
print(top3)
for i, (palabra, contador) in enumerate(top3, 1):
    print(f"{i}. palabra {palabra}, unas {contador} veces")

# 2. Escribe un patrón que encuentre o extraiga las direcciones de email válidas:
email_address = '''
asabeneh@gmail.com
alex@yahoo.com
kofi@yahoo.com
doe@arc.gov
asabeneh.com
asabeneh@gmail
alex@yahoo
'''
patron_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails_validos = re.findall(patron_email, email_address)
print(emails_validos)