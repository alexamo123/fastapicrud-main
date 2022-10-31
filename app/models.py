from sqlalchemy import Column, Integer, String,DateTime
from Conexion import Base
from datetime import datetime, time, timedelta
from uuid import UUID
from datetime import date as date_type


class Datos(Base):
    __tablename__ = 'datos'
    id=Column(Integer, primary_key=True, index=True)
    fec_alta=Column(DateTime)
    user_name=Column(String(50))
    codigo_zip=Column(String(20))
    credit_car_num=Column(String(250))
    cuenta_numero=Column(Integer)
    direccion=Column(String(20))
    geo_latitud=Column(String(20))
    geo_longitud=Column(String(20))
    color_favorito=Column(String(20))
    foto_dni=Column(String(20))
    ip=Column(String(20))
    auto=Column(String(20))
    auto_modelo=Column(String(20))
    auto_tipo=Column(String(20))
    auto_color=Column(String(20))
    cant_compras=Column(Integer)
    avatar=Column(String(20))
    fec_nacimiento=Column(DateTime)

    class Config:
        orm_mode =True
