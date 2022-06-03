import time
import requests
import pandas as pd
import hashlib
from sqlalchemy import create_engine
import sys
df = pd.DataFrame( columns = ["Region", "Country Name","Languaje", "Time(ms)"] )
engine = create_engine( 'sqlite://', echo = False )

def obtian_DataCuntry( country ):
    '''Dado un pais, los cunsulta  en restcountries.com y devuelve una lista con los datos del pais'''
    try:
        url = "https://restcountries.com/v2/name/" + country
        response = requests.get( url )
        
        if response.status_code == 200:
            return response.json()
            
        else:
            return None
        
    except:
        print( 'la url no responde' )
        exit()
        
    

def generate_countryRow( country ):
    """Dado el nombre de un pais, devuelve una fila(lista) con los datos que requerimos del pais"""
    startTime = time.time()
    dataCountry = obtian_DataCuntry( country )
    if dataCountry is not None:
        country_lang = dataCountry[0]['languages'][0]['name']
        hash_country_lang = hashlib.sha1(country_lang.encode( 'utf-8' ) ).hexdigest()
        endTime = time.time()
        time_generated_row = ( endTime - startTime ) * 1000
        country_row = [ dataCountry[ 0 ][ 'region' ], dataCountry[ 0 ][ 'name' ], hash_country_lang, time_generated_row ] 
    else:
        endTime = time.time()
        time_generated_row = ( endTime - startTime ) * 1000
        print( f"No se encontraron datos del pais { country }, tiempo de búsqueda {time_generated_row}ms" )           
        country_row = None           
    return country_row

def add_countryRow_to_dataFrame( country, df ):
    '''Usando la funcion generarFilas(pais) Agrega una fila al dataframe df
    , guarda el dataframe en la base de datos y en un archivo .json'''
    country_row = generate_countryRow( country )
    if country_row!=None:
        df.loc[ len( df ) ] = country_row
    
    return df

if __name__=='__main__':
    # listadePaises = ["Angola","Argentina", "Brasil", "Chile", "Colombia", "United States of America", "United K", "Uruguay", "Venezuela", "España","Valledupar","Bogota"]
    if len( sys.argv ) > 1:
        listCountries = sys.argv[1:]

        for country in listCountries:
            df = add_countryRow_to_dataFrame( listCountries, df)
            
    
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