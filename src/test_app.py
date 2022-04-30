import app
import unittest
import pandas as pd
from sqlalchemy import create_engine
df=pd.DataFrame(columns=["Region", "Country Name","Languaje", "Time(ms)"])
# engine=create_engine('sqlite://', echo=False)

class TestApp(unittest.TestCase):
    def test_obtenerDatosdelPais_Ang(self):
        pais = 'Angola'
        datosPais = app.obtenerDatosdelPais(pais)
        self.assertEqual(datosPais[0]['region'], 'Africa')
        self.assertEqual(datosPais[0]['name'], 'Angola')
        self.assertEqual(datosPais[0]['languages'][0]['name'], 'Portuguese')

    def test_obtenerDatosdelPais_Esp(self):
        pais = 'España'
        datosPais = app.obtenerDatosdelPais(pais)
        self.assertEqual(datosPais[0]['region'], 'Europe')
        self.assertEqual(datosPais[0]['name'], 'Spain')
        self.assertEqual(datosPais[0]['languages'][0]['name'], 'Spanish')

    def test_obtenerDatosdelPais_Col(self):
        pais = 'Colombia'
        datosPais = app.obtenerDatosdelPais(pais)
        self.assertEqual(datosPais[0]['region'], 'Americas')
        self.assertEqual(datosPais[0]['name'], 'Colombia')
        self.assertEqual(datosPais[0]['languages'][0]['name'], 'Spanish')

    def test_obtenerDatosdelPais_Vall(self):
        pais = 'Valledupar'
        datosPais = app.obtenerDatosdelPais(pais)
        self.assertEqual(datosPais, None)

    def test_generarFila_Esp(self):
        pais = 'España'
        fila = app.generarFila(pais)
        self.assertEqual(fila[0], 'Europe')
        self.assertEqual(fila[1], 'Spain')
        # self.assertEqual(fila[2], 'sha1$5f47a1b3$1$3c3e3a8a2b9d2a7a9a9b9c1b076b0d6b1c6e5e0f')

    def test_generarFila_Col(self):
        pais = 'Colombia'
        fila = app.generarFila(pais)
        self.assertEqual(fila[0], 'Americas')
        self.assertEqual(fila[1], 'Colombia')
        # self.assertEqual(fila[2], 'sha1$5f47a1b3$1$3c3e3a8a2b9d2a7a9a9b9c1b076b0d6b1c6e5e0f')    
    
    
    def test_generarFila_Ang(self):
        pais = 'Angola'
        fila = app.generarFila(pais)
        self.assertEqual(fila[0], 'Africa')
        self.assertEqual(fila[1], 'Angola')
        # self.assertEqual(fila[2], 'sha1$5f47a1b3$1$3c3e3a8a2b9d2a7a9a9b9c1b076b0d6b1c6e5e0f')

    def test_generarFila_Valle(self):
        pais = 'Valledupar'
        fila = app.generarFila(pais)
        self.assertEqual(fila, None)
    
    def test_adicionarFila(self):
        listadePaises = ["Angola","Argentina","España","Valledupar"]
        for pais in listadePaises:
            app.adicionarFila(pais, df)
        self.assertEqual(df["Region"][0], 'Africa')
        self.assertEqual(df["Country Name"][0], 'Angola')
        self.assertEqual(df["Region"][1], 'Americas')
        self.assertEqual(df["Country Name"][1], 'Argentina')
        self.assertEqual(df["Region"][len(df)-1], 'Europe')
            
    
    