Paso 1: Creacion de un entorno virtual de python(Se uso Python 3.9.16).
```
  pip install virtualenv

  python -m venv venv
```

Paso 2: Instalar librerias necesarias con el comando: 
```
  pip install -r requirements.txt
```

Paso 3: Una vez creado nuestro entorno virtual de python debemos de agregarlo a VSCode presionando CTRL + P y escribir ">Python Interpreter", luego debemos de seleccionar el interpreter de python del entorno virutal que recien creamos.
En windows se activa mediante el comando:
```
  venv/Scripts/activate.ps1
```

Paso 4: Colocarse dentro de la direccion "ProyectoCarritodeCompras/CarritoDeCompras/CarritoDeCompras" y ejecutar el comando:
```
  python ../manage.py runserver
```

Direccion de la api: http://127.0.0.1:8000/carrito/api/
