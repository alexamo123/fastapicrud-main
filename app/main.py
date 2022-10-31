from typing import List
from fastapi import FastAPI, Body, Depends
from starlette.responses import RedirectResponse
from schemas import UserLoginSchema, UserSchema
import models,schemas
#import app.models import UserLoginSchema
from jwt_handler import signJWT
from Conexion import SessionLocal,engine
from sqlalchemy.orm import Session
from jwt_bearer import JWTBearer
import requests
import json
import datetime


models.Base.metadata.create_all(bind=engine)
users = []
app = FastAPI()


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.get('/usuarios/',dependencies=[Depends(JWTBearer())],tags=["posts"])
def show_users(db:Session=Depends(get_db)):
    usuarios = db.query(models.Datos).all()
    return usuarios


@app.post("/user/signup", tags=["user"])
def create_user(user: UserSchema = Body(...)):
    users.append(user) # replace with db call, making sure to hash the password first
    return signJWT(user.email)


@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details harto!"
    }

@app.get("/cargadb/", dependencies=[Depends(JWTBearer())], tags=["db"])
def call_extapi():
    url_destino = "https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios/" 
    engn=engine
    connection = engn.raw_connection()
    respuesta = requests.get(url_destino)
    mycursor = connection.cursor()
    sqlcode = """INSERT INTO datos 
                (
                    id,
                    fec_alta,
                    user_name,
                    codigo_zip,
                    credit_car_num,
                    cuenta_numero,
                    direccion,
                    geo_latitud,
                    geo_longitud,
                    color_favorito,
                    foto_dni,
                    ip,
                    auto,
                    auto_modelo,
                    auto_tipo,
                    auto_color,
                    cant_compras,
                    avatar,
                    fec_nacimiento) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    arrRespuesta = respuesta.json()
    for usuario in arrRespuesta:
        mycursor.execute(sqlcode, (usuario['id'], \
        datetime.datetime.strptime(usuario['fec_alta'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d %H:%M:%S'), \
        usuario['user_name'], usuario['codigo_zip'], \
        usuario['credit_card_ccv'], usuario['cuenta_numero'], usuario['direccion'], usuario['geo_latitud'], usuario['geo_longitud'], \
        usuario['color_favorito'], usuario['foto_dni'], usuario['ip'], usuario['auto'], usuario['auto_modelo'], \
        usuario['auto_tipo'], usuario['auto_color'], usuario['cantidad_compras_realizadas'], usuario['avatar'], \
        datetime.datetime.strptime(usuario['fec_birthday'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d %H:%M:%S') ))
    connection.commit()
    return "ok"