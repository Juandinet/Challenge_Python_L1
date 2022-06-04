import app
import unittest
import pandas as pd
df=pd.DataFrame(columns=["Region", "Country Name","Languaje", "Time(ms)"])
# engine=create_engine('sqlite://', echo=False)

class TestApp(unittest.TestCase):
    def test_get_DataCountry_Ang(self):
        pais = 'Angola'
        datosPais = app.get_DataCountry(pais)
        self.assertEqual(datosPais[0]['region'], 'Africa')
        self.assertEqual(datosPais[0]['name'], 'Angola')
        self.assertEqual(datosPais[0]['languages'][0]['name'], 'Portuguese')

    def test_get_DataCountry_Esp(self):
        pais = 'España'
        datosPais = app.get_DataCountry(pais)
        self.assertEqual(datosPais[0]['region'], 'Europe')
        self.assertEqual(datosPais[0]['name'], 'Spain')
        self.assertEqual(datosPais[0]['languages'][0]['name'], 'Spanish')

    def test_get_DataCountry_Col(self):
        pais = 'Colombia'
        datosPais = app.get_DataCountry(pais)
        self.assertEqual(datosPais[0]['region'], 'Americas')
        self.assertEqual(datosPais[0]['name'], 'Colombia')
        self.assertEqual(datosPais[0]['languages'][0]['name'], 'Spanish')

    def test_get_DataCountry_Vall(self):
        pais = 'Valledupar'
        datosPais = app.get_DataCountry(pais)
        self.assertEqual(datosPais, None)

    def test_generate_countryRow_Esp(self):
        pais = 'España'
        fila = app.generate_countryRow(pais)
        self.assertEqual(fila[0], 'Europe')
        self.assertEqual(fila[1], 'Spain')
        self.assertEqual(fila[2], '8df7f1b361b2af42d36011e00d22c0f9891ec0b0')

    def test_generate_countryRow_Col(self):
        pais = 'Colombia'
        fila = app.generate_countryRow(pais)
        self.assertEqual(fila[0], 'Americas')
        self.assertEqual(fila[1], 'Colombia')
        self.assertEqual(fila[2], '8df7f1b361b2af42d36011e00d22c0f9891ec0b0')    
    
    
    def test_generate_countryRow_Ang(self):
        pais = 'Angola'
        fila = app.generate_countryRow(pais)
        self.assertEqual(fila[0], 'Africa')
        self.assertEqual(fila[1], 'Angola')
        self.assertEqual(fila[2], '23882c575954a0789bf02aba9e6dd01f539bc738')

    def test_generate_countryRow_Valle(self):
        pais = 'Valledupar'
        fila = app.generate_countryRow(pais)
        self.assertEqual(fila, None)
    
    def test_add_countryRow_to_dataFrame(self):
        listadePaises = ["Angola","Argentina","España","Valledupar"]
        for pais in listadePaises:
            app.add_countryRow_to_dataFrame(pais, df)
        self.assertEqual(df["Region"][0], 'Africa')
        self.assertEqual(df["Country Name"][0], 'Angola')
        self.assertEqual(df["Region"][1], 'Americas')
        self.assertEqual(df["Country Name"][1], 'Argentina')
        self.assertEqual(df["Region"][len(df)-1], 'Europe')
            
    
    