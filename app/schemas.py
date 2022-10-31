from typing import Optional
from pydantic import BaseModel, Field,EmailStr
from datetime import date, datetime, time, timedelta

class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True

class Datos(OurBaseModel):
    id:int
    fec_alta:date
    user_name:str
    codigo_zip:str
    credit_car_num:str
    cuenta_numero:int
    direccion:str
    geo_latitud:str
    geo_longitud:str
    color_favorito:str
    foto_dni:str
    ip:str
    auto:str
    auto_modelo:str
    auto_tipo:str
    auto_color:str
    cant_compras:int
    avatar:str
    fec_nacimiento:date


class UserUpdate(BaseModel):   
    nombre:str

    class Config:
        orm_mode =True
class UserSchema(BaseModel):   
    user_name:str=Field(default=None)
    email:EmailStr=Field(default=None)
    password:str=Field(default=None)
    class Config:
        the_schema={
            "user_demo":{
                "name":"alexa",
                "email":"raziel214@hotmail.com",
                "password":"123"

            }
        }
class UserLoginSchema(BaseModel):
    email:EmailStr=Field(default=None)
    password:str=Field(default=None)
    class Config:
        the_schema={
            "user_demo":{
                "email":"raziel214@hotmail.com",
                "password":"123"

            }
        }

class Respuesta(BaseModel):   
    mensaje:str