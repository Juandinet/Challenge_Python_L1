import time
import requests
# import json
import pandas as pd
import hashlib
from sqlalchemy import create_engine
# import locale

# locale.setlocale(locale.LC_ALL, '')



url='https://restcountries.com/v2/name/'
formato='?fullText=true'

listadePaises = ["Angola","Argentina", "Brasil", "Chile", "Colombia", "Ecuador", "Paraguay", "Uruguay", "Venezuela", "españa"]

def obtenerDatosdelPais(pais):
    """Dado el nombre de un pais, devuelve una lista con los datos del pais
    de la API de RestCountries"""
    url_pais = url + pais.lower().strip() #+ formato
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

            # fila = {"Region":datosPais[0]['region'], "Country Name":datosPais[0]['name'],"Languaje":hash_idioma.hexdigest(), "Time":tiempo}
            fila=[datosPais[0]['region'],datosPais[0]['name'],hash_idioma.hexdigest(),tiempo]
        else:
            endTime=time.time()
            tiempo=(endTime-startTime)*1000
            # fila = {"Region":"None", "Country Name":pais,"Languaje":"No se encontraron datos", "Time":0}
            fila=["",pais,"No se encontraron datos",tiempo]           
        return fila

if __name__=='__main__':
    # print("Bienvenido a la lista de paises")
    # print("Estos son los paises de nuestra lista")
    # print(listadePaises)
    indiceFilas=0
    df=pd.DataFrame(columns=["Region", "Country Name","Languaje", "Time(ms)"])
    for pais in listadePaises:
        df.loc[indiceFilas]=generarFila(pais)
        # df = df.append(generarFila(pais),ignore_index=True)
        
        indiceFilas+=1
    print(df)
    print("Tiempo total: ",df["Time(ms)"].sum(), "ms")    
    print("Tiempo promedio: ",df["Time(ms)"].mean(), "ms")    
    print("Tiempo Mínimo: ",df["Time(ms)"].min(), "ms")
    print("Tiempo Máximo: ",df["Time(ms)"].max(), "ms")  
    engine=create_engine('sqlite://', echo=False)  
    df.to_sql('paises', engine, if_exists='replace')
    print(engine.execute("SELECT * FROM paises").fetchall())
    

