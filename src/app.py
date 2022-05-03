import time
import requests
import pandas as pd
import hashlib
from sqlalchemy import create_engine
import sys
df=pd.DataFrame(columns=["Region", "Country Name","Languaje", "Time(ms)"])
engine=create_engine('sqlite://', echo=False)

def obtenerDatosdelPais(pais):
    """Dado el nombre de un pais, devuelve una lista con los datos del pais
    de la API de restCountries.com"""
    try:
        url = "https://restcountries.com/v2/name/" + pais
        respuesta = requests.get(url)
        
        if respuesta.status_code == 200:
            return respuesta.json()
            
        else:
            return None
        
    except:
        print('la url no responde')
        exit()
        
    

def generarFila(pais):
    """Dado el nombre de un pais, devuelve una fila(lista) con los datos que requerimos del pais"""
    startTime=time.time()
    datosPais = obtenerDatosdelPais(pais)
    if datosPais is not None:
        idioma=datosPais[0]['languages'][0]['name']
        hash_idioma = hashlib.sha1(idioma.encode('utf-8')).hexdigest()
        endTime=time.time()
        tiempo=(endTime-startTime)*1000
        fila=[datosPais[0]['region'],datosPais[0]['name'],hash_idioma,tiempo]
    else:
        endTime=time.time()
        tiempo=(endTime-startTime)*1000
        print(f"No se encontraron datos del pais {pais}, tiempo de búsqueda {tiempo}ms")           
        fila=None           
    return fila

def adicionarFila(pais,df):
    '''Usando la funcion generarFilas(pais) Agrega una fila al dataframe df
    , guarda el dataframe en la base de datos y en un archivo .json'''
    fila = generarFila(pais)
    if fila!=None:
        df.loc[len(df)]=fila
        
    # else:
    #    print("No se encontraron datos para el pais: ", pais)
    return df
    
    

if __name__=='__main__':
    # listadePaises = ["Angola","Argentina", "Brasil", "Chile", "Colombia", "United States of America", "United K", "Uruguay", "Venezuela", "España","Valledupar","Bogota"]
    if len(sys.argv)>1:
        listadePaises=sys.argv[1:]
        # print(listadePaises)
        for pais in listadePaises:
            df=adicionarFila(pais,df)
            df.to_sql('paises',engine,if_exists='replace',index=False)
            df.to_json('paises.json',orient='records')
    
        print('_____________________________________________________________')

        print(df)
    
        print("Tiempo total: ",df["Time(ms)"].sum(), "ms")    
        print("Tiempo promedio: ",df["Time(ms)"].mean(), "ms")    
        print("Tiempo Mínimo: ",df["Time(ms)"].min(), "ms")
        print("Tiempo Máximo: ",df["Time(ms)"].max(), "ms")

        # Guardar DataFrame en una base de datos 
        df.to_sql('paises', engine, if_exists='replace')
        # Guardar DataFrame en un json
        df.to_json('data.json')
        
        # Consulta a la base de datos para probar que se guardaron los datos
        print(engine.execute("SELECT * FROM paises").fetchall())
    else:
        print("No se ingresaron paises")    