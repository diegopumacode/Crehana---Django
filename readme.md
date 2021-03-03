# Crehana + BackEnd

## Paso 1
Para comenzar debes tener instalado Python en la versión 3.9.2, para descargar, haz click en el [siguiente](https://www.python.org/downloads/) enlace

## Paso 2
Una vez instalado debes instalar las siguientes librerias, puedes hacerlo de dos formas.
   - La primera es ubicarte en el repositorio encontrarás un archivo llamado `requirements.txt` y ejecutar el siguiente comando en esa ubicacion:
```sh
> pip install -r requirements.txt
```
- Eso instalará todas las librerias necesarias para que el proyecto pueda funcionar.
- La segunda forma es instalar manualmente uno por uno las librerias, algunas son incluyentes de otras por lo que recomiendo la primera opcion, si se desea por la segunda opcion se debera correr el siguiente comando:
```sh
> pip install nombre_paquete
```
## Paso 3
Por finalizar, si queremos ver si hemos instalado todas las librerias correctamente en nuestra máquina, deberemos correr el siguiente comando
```sh
> pip freeze
```
- Este es un comando global y por ende las librerias se instalarán en toda nuestra máquina

## Paso 4
Por ultimo ya para levantar nuestro proyecto deberemos correr el siguiente comando
```sh
> py manage.py runserver
```
Si levanto indicando que la base de datos no existe, felicidades, todas las libererias fueron instaladas con exito y ahora veamos la conexion a la base de datos y sus migraciones.

## Paso 5
Si todo esta correcto entonces hay que llevar todos los modelos a la base de datos. Para ello haremos uso del siguiente comando
```sh
> py manage.py migrate
```
Eso nos mostrara todas las migraciones encontradas en el proyecto y para visualizar si fueron realizadas con exito se necesitará ejecutar el siguiente comando:
```sh
> py manage.py showmigrations
```
Las migraciones que esten con un `check` serán las que realizaron con éxito.
## Paso 6
Solamente quedaría entonces volver a levantar nuestro servidor para ver si todo se ha configurado correctamente.
```sh
> py manage.py runserver
```
