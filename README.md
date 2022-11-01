# Proyecto con FASTAPI, SQLALCHEMY Y MYSQL

## PASOS PARA INSTALAR
1. Crear un ambiente virtual con Python3 y/o con Anaconda navigator
```
virtualenv env -p python3

```
2. Activar el ambiente virtual
```
source env/bin/activate

```
3. Instalar Xamc Server, para subir los servicios de apache y Mysql
... 
https://www.apachefriends.org/es/index.html

Levantar servicio Apache ( puertos 80,443)
Levantar servicio MySQL (puerto 3306)

...
4. Crear BD mysql teniendo instalado Xamp server (se adjunta script)
...
Importar ScripDatos.sql 
...
5. Desde cmd instalar las librerías necesarias que se encuentran en el archivo requirements.txt, desde la ruta donde se guardo el proyecto
```
pip install -r requirements.txt

```
6. Instalar manualmente las sigientes librerias
...
pip install httptools

pip install mysqlclient

pip install ujson

pip install PyJWT

pip install python-decouple

pip install request

...

## DESPLEGANDO EL AMBIENTE
```
uvicorn main:app --reload

```
* main es el nombre del archivo main.py
* app es el nombre de la variable de FASTAPI inicializada en el archivo main

7. - Ver FastAPI implementada y documentada con Swagger

http://127.0.0.1:8000/docs#/

Generar el Token con el metodo user/post
Autorizar el consumo del servicio con token generado
Consumir el servicio con el token generado post/get
Consumir el servicio de la BD con el token db/get

Consumir metodo get de usuarios, para ello primero se debe generar el token en el metodo create_user que pide username, email y passwd

Consultar datos insertados en la BD Mysql 