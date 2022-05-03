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

# Diseño de la solución

![avatar](diagrama_de-flujo.py)

La app recibe parámetros por consola, en este caso un país o lista de países separados por coma(,) y debe hacer la consulta de cada país a la URI: https://restcountries.com/ con el fin de obtener la información de cada país solicitado (uno por uno), para ello la maquina donde ese ejecute debe tener el suficiente acceso a internet para realizar la consulta y recibir la respuesta.

Luego internamente genera un a fila de la tabla teniendo en cuenta el tiempo que se lleve realizar la consulta y armar la fila en general.

Estas filas las va recibiendo una función que va agregando las filas al Data Frame (Pandas)

Luego de procesar toda la lista de países recibida, procede a guardar en SQLite una tabla llamada países y exporta a un archivo “data.json” como lo dicta el requerimiento.

Finalmente, la aplicación imprime por consola el Data Frame, genera e imprime los datos de Tiempo total, promedio,  máximo y mínimo de la columna de tiempos del Data Frame, usando las funciones que Pandas tiene para ello.

A modo de prueba, al final se hace una consulta a la tabla en SQLite y se imprime la lista resultante por consola, pero esta parte no va en una posible versión de producción. 

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

Para correr la solución se ejecuta el siguiente comando, se pasan como argumentos, una lista de paises separados por coma y entre comillas los nombres para evitar inconvenientes con los espacios y acentos.

```powershell
python .\src\app.py "Angola", "Brasil", Colombia, "United States of America", "United K", "Venezuela", "España","Valledupar","Bogota"
```

Para correr los test unitarios se ejecuta el siguiente comando:

```powershell
python .\src\test_app.py
```


