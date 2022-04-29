import time
import requests
import json
import pandas as pd
import hashlib
import locale
locale.setlocale(locale.LC_ALL, '')


url='https://restcountries.com/v2/name/'
formato='?fullText=true'

listadePaises = ["Angola","Argentina", "Brasil", "Chile", "Colombia", "Ecuador", "Paraguay", "Uruguay", "Venezuela"]

def obtenerDatosdelPais(pais):
    # de la api https://restcountries.com/v2/name/{name}?fullText=true obtener los datos del pais
    # retornar un diccionario con los datos
    url_pais = url + pais.lower().strip() + formato
    r = requests.get(url_pais)  # r es un objeto de la clase Response
    if r.status_code == 200:
        return r.json()
    else:
        return None
def generarFila(pais):
        startTime=time.time()
        datosPais = obtenerDatosdelPais(pais)
        if datosPais is not None:
            # print(datosPais[0]['region'])
            # print(datosPais[0]['name'])
            idioma=datosPais[0]['languages'][0]['name']
            # print(idioma)
            hash_idioma = hashlib.sha1(b'{idioma}')
            # print(hash_idioma.hexdigest())
            endTime=time.time()
            tiempo=(endTime-startTime)*1000

            fila = [datosPais[0]['region'], datosPais[0]['name'], hash_idioma.hexdigest(), tiempo]
        else:
            fila = ['','No encotrado','', '']
                       
        return fila
def generarFila(pais):
        startTime=time.time()
        datosPais = obtenerDatosdelPais(pais)
        if datosPais is not None:
            # print(datosPais[0]['region'])
            # print(datosPais[0]['name'])
            idioma=datosPais[0]['languages'][0]['name']
            # print(idioma)
            hash_idioma = hashlib.sha1(b'{idioma}')
            # print(hash_idioma.hexdigest())
            endTime=time.time()
            tiempo=(endTime-startTime)*1000

            fila = [datosPais[0]['region'], datosPais[0]['name'], hash_idioma.hexdigest(), tiempo]
        else:
            fila = ['','No encotrado','', '']
                       
        return fila

    


if __name__=='__main__':
    print("Bienvenido a la lista de paises")
    print("Estos son los paises de nuestra lista")
    print(listadePaises)
    for pais in listadePaises:
        print("datos del pais: ",pais, generarFila(pais))
        
    

