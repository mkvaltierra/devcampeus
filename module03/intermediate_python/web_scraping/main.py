"""
Ir a la web : http://www.dailysmarty.com/topics/python

Seleccionar/Filtrar todos los enlaces (desde los links principales) a los posts:
'https://www.dailysmarty.com/posts/installing-anaconda-python-data-science-platform'

Desde el link del post, extraer el titulo real del post. Ponerlo entre comillas dobles, através de una función que filtre el texto
Conseguir una lista con todos los titulos de los links

Ej: "How to Implement FizzBuzz in Python"

Librerías a utilizar:
- requests
- inflection
- beautifulsoup

"""

import requests
from bs4 import BeautifulSoup
from libs.helper import formating_text



url = 'http://www.dailysmarty.com/topics/python'

# Obtener la web 
website = requests.get(url)
page = BeautifulSoup(website.text, 'html.parser')


# Obtenemos todas la etiquetas padre (h2) de donde están los titulos
links = page.find_all('h2')

# Formateo lista etiquetas
formating_text(links)

