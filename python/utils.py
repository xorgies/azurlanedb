import requests
from requests_html import HTMLSession
import json
import urllib.request
from bs4 import BeautifulSoup

def sacarDatos(url,urlBase):
    respuesta = {}

    this_session = HTMLSession()
    response = this_session.get(url)
    response.html.render()

    soup = BeautifulSoup(response.html.raw_html, "html.parser")

    # tipo de barco
    tipoBarco = soup.find_all("a", class_="active nav-link")[1].text
    respuesta["clase"] = tipoBarco

    respuesta["barcos"] = []

    divBody = soup.find_all("div", class_="card-body")
    divContenedor = divBody[0].find_all("div", class_="tab-pane active")
    divsBarcos = divContenedor[0].findChildren("div",recursive=False)

    # el primero es el filtro por tipos especiales
    divsBarcos.pop(0)

    for divsBarcosTier in divsBarcos:
        # Comprobar que no este vacio
        # tier
        tier = ""
        try:
            tier = divsBarcosTier.find("h3",class_="title").text.split(" ")[1]
        except:
            continue
        
        divsBarcos = divsBarcosTier.findChildren("div",recursive=False)[0].findChildren("div",recursive=False)
        for divBarco in divsBarcos:
            barco = {}

            # nombre
            nombre = divBarco.find("p").text

            print("-----------------------")
            print("Barco: "+nombre)

            # badges

            # imagen barco
            imagen = divBarco.find("img",recursive=False)["src"]
            imagenNombre = imagen.split("/")[-1]
            download_image(urlBase+urllib.parse.quote(imagen),imagenNombre)

            barco["nombre"] = nombre
            barco["tier"] = tier
            barco["imagen"] = imagenNombre

            respuesta["barcos"].append(barco)
            
    # print(json.dumps(respuesta))
    return respuesta

def download_image(url, file_name):
    full_path = "datos/img/" + file_name
    urllib.request.urlretrieve(url, full_path)