from flask import Blueprint,render_template, request, flash
from app.models.personajes import Personajes
from app.db import db
import requests
personajes_ruta=Blueprint("personajes_ruta", __name__)


@personajes_ruta.route("/")
def index():
    personajes=db.personajes.find()
    return render_template("index.html", personajes=personajes) 

@personajes_ruta.route("/insertar")
def insertar():

    for n in range(1,22):

        url="https://rickandmortyapi.com/api/character?page="
            
        url_personaje=url+ str(n)
        response= requests.get(url_personaje)
        datos=response.json()
        

        for y in datos["results"]:
            infor=Personajes(y["id"], y["name"], y["status"], y["species"], y["type"], y["gender"], y["origin"]["url"], y["location"]["name"], y["image"], y["episode"], y["url"], y["created"])
            db.personajes.insert_one(infor.to_json())
            #lista_personajes.append()

    return "PERSONAJES INGRESADOS"



