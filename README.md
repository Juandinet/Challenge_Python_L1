# Challenge_Python_L1
Prueba de conocimientos Python Tangelo

## Descripcion de la prueba

| Region         | City Name       | Languaje                                   | Time    |
| ----- | ---- | ----- | ---- |
| Africa         | Angola          | AF4F4762F9BD3F0F4A10CAF5B6E63DC4CE543724   | 0.23 ms |


Desarrolle una aplicacion en python que genere la tabla anterior teniendo las siguientes consideraciones:

- De https://restcountries.com/ obtenga el nombre del idioma que habla el pais y encriptelo con SHA1
- En la columna Time ponga el tiempo que tardo en armar la fila (debe ser automatico)
- La tabla debe ser creada en un DataFrame con la libreria PANDAS
- Con funciones de la libreria pandas muestre el tiempo total, el tiempo promedio, el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla.
- Guarde el resultado en sqlite.
- Genere un Json de la tabla creada y guardelo como data.json
- La prueba debe ser entregada en un repositorio git.

Es un plus si:

- No usa famework
- Entrega Test Unitarios
- Presenta un diseño de su solucion.

# DESARROLLO DE LA SOLUCIÓN
## En un entorno virtual usando Python3 , pip y la siguiente lista de dependencias (requirements.txt)
- certifi==2021.10.8
- charset-normalizer==2.0.12
- greenlet==1.1.2
- idna==3.3
- numpy==1.22.3
- pandas==1.4.2
- python-dateutil==2.8.2
- pytz==2022.1
- requests==2.27.1
- six==1.16.0
- SQLAlchemy==1.4.36
- urllib3==1.26.9


Si no está instalado, instalamos virtualenv

```powershell
pip install virtualenv
```

Para crear un ambiente virtual digitamos el siguiente comando:

```powershell
virtualenv -p python3 env
```

para poner a funcionar el entorno virtual, se debe ejecutar:

```powershell
.\env\Scripts\activate
```

Una vez iniciado el entorno virtual, se ejecuta el siguiente comando:

```powershell
pip install -r .\requirements.txt
```

Para correr la solución se ejecuta el siguiente comando, se pasa una lista de paises, separados por coma y entre comillas los nombres para evitar inconvenientes con los espacios.

```powershell
.\src\app.py "Angola", "Brasil", "Colombia", "United States of America", "United K", "Venezuela", "España","Valledupar","Bogota"
```

Para correr los test unitarios se ejecuta el siguiente comando:

```powershell
python .\src\test_app.py
```
