import time
import requests
# import json
import pandas as pd
import hashlib
from sqlalchemy import create_engine
# import locale
df=pd.DataFrame(columns=["Region", "Country Name","Languaje", "Time(ms)"])
engine=create_engine('sqlite://', echo=False)
# locale.setlocale(locale.LC_ALL, '')







def obtenerDatosdelPais(pais):
    """Dado el nombre de un pais, devuelve una lista con los datos del pais
    de la API de RestCountries"""
    url='https://restcountries.com/v2/name/'
    url_pais = url + pais.lower().strip() # + '?fullText=true'
    r = requests.get(url_pais)  # r es un objeto de la clase Response
    if r.status_code == 200:
        return r.json()
    else:
        return None

def generarFila(pais):
        startTime=time.time()
        datosPais = obtenerDatosdelPais(pais)
        if datosPais is not None:
            idioma=datosPais[0]['languages'][0]['name']
            hash_idioma = hashlib.sha1(idioma.encode('utf-8')).hexdigest()
            endTime=time.time()
            tiempo=(endTime-startTime)*1000
            # fila = {"Region":datosPais[0]['region'], "Country Name":datosPais[0]['name'],"Languaje":hash_idioma.hexdigest(), "Time":tiempo}
            fila=[datosPais[0]['region'],datosPais[0]['name'],hash_idioma,tiempo]
        else:
            endTime=time.time()
            tiempo=(endTime-startTime)*1000
            # fila=["",pais,"No se encontraron datos",tiempo]           
            fila=None           
        return fila

def adicionarFila(pais,df):
    '''Usando la funcion generarFilas(pais) Agrega una fila al dataframe df
    , guarda el dataframe en la base de datos y en un archivo .json'''
    fila = generarFila(pais)
    if fila!=None:
        df.loc[len(df)]=fila
        # Guardar en una base de datos 
        df.to_sql('paises', engine, if_exists='replace')
        # Guardar en un json
        df.to_json('data.json')
    else:
        print("No se encontraron datos para el pais: ", pais)
    return df
    
    

if __name__=='__main__':
    listadePaises = ["Angola","Argentina", "Brasil", "Chile", "Colombia", "United States of America", "United K", "Uruguay", "Venezuela", "España","Valledupar"]
    for pais in listadePaises:
        adicionarFila(pais,df)
    
    print('_____________________________________________________________')
    print(df)
  
    print("Tiempo total: ",df["Time(ms)"].sum(), "ms")    
    print("Tiempo promedio: ",df["Time(ms)"].mean(), "ms")    
    print("Tiempo Mínimo: ",df["Time(ms)"].min(), "ms")
    print("Tiempo Máximo: ",df["Time(ms)"].max(), "ms")

    
    
    
    
    # Consulta a la base de datos para probar que se guardaron los datos
    print(engine.execute("SELECT * FROM paises").fetchall())
    