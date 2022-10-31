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

# @app.post('/usuarios/',dependencies=[Depends(JWTBearer())],tags=["posts"])
# def show_users(db:Session=Depends(get_db)):
#     usuarios = db.query(models.Datos).all()
#     return usuarios

@app.post("/user/signup", tags=["user"])
def create_user(user: UserSchema = Body(...)):
    users.append(user) # replace with db call, making sure to hash the password first
    return signJWT(user.email)


@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }


# @app.post('/usuarios/',response_model=schemas.User)
# def create_users(entrada:schemas.User,db:Session=Depends(get_db)):
#     usuario = models.User(username = entrada.username,nombre=entrada.nombre,rol=entrada.rol,estado=entrada.estado)
#     db.add(usuario)
#     db.commit()
#     db.refresh(usuario)
#     return usuario

# @app.put('/usuarios/{usuario_id}',response_model=schemas.User)
# def update_users(usuario_id:int,entrada:schemas.UserUpdate,db:Session=Depends(get_db)):
#     usuario = db.query(models.User).filter_by(id=usuario_id).first()
#     usuario.nombre=entrada.nombre
#     db.commit()
#     db.refresh(usuario)
#     return usuario

# @app.delete('/usuarios/{usuario_id}',response_model=schemas.Respuesta)
# def delete_users(usuario_id:int,db:Session=Depends(get_db)):
#     usuario = db.query(models.User).filter_by(id=usuario_id).first()
#     db.delete(usuario)
#     db.commit()
#     respuesta = schemas.Respuesta(mensaje="Eliminado exitosamente")
#     return respuesta