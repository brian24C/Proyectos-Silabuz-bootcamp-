from flask import Blueprint,render_template, request, flash
from app.models.personajes import Personajes, Capitulo
from app.db import db
import requests
personajes_ruta=Blueprint("personajes_ruta", __name__)


@personajes_ruta.route("/")
def index():
    personajes=db.personajes.find().sort('id', -1)
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


def gravatar(id=""):
    url = "https://rickandmortyapi.com/api/character/avatar/"
    url=url + str(id) + ".jpeg"
        
    return "{url}".format(url=url)


@personajes_ruta.route("/avatar/<id>")
def avatar(id):
    id=int(id)
    filtro=db.personajes.find({"id":id})

    avt = gravatar(id)
    return render_template("avatar.html", avatar=avt, info=filtro)



#--------------------------------------------------EJERCICIO ADICIONAL--------------------------------------------------------------

@personajes_ruta.route("/insertar_capitulos")
def insertar_capitulos():


    for n in range(1,4):

        url="https://rickandmortyapi.com/api/episode?page="
            
        url_capitulos=url+ str(n)
        response= requests.get(url_capitulos)
        datos=response.json()
        

        for y in datos["results"]:
            infor=Capitulo(y["id"], y["name"], y["air_date"], y["episode"], y["characters"],y["url"], y["created"])
            db.capitulos.insert_one(infor.to_json())

    return "CAPITULOS INGRESADOS"

@personajes_ruta.route("/capitulo/<id>")
def personajes_capitulo(id):
                                                                                    #en los 2 variables "personajes_lista" me dueleve algo así > ['https://rickandmortyapi.com/api/character/1', 'https://rickandmortyapi.com/api/character/2']
    #personajes_lista=db.capitulos.find()[int(id)]["characters"]                    #Aquí uso ["characters"] porque estoy buscando en un diccionario, En html pondría .characters porque así se manejo en html
    #print(db.capitulos.find()[1])                                                  # -> me da el documento con id 2 (porque [1] es el índiceque busca en una lista) 
    personajes_lista=db.capitulos.find({"id":int(id)})[0]["characters"]             # db.capitulos.find({"id":int(id)}) = me da un objeto, por eso tengo que poner "[0]" y me arrojaría el documento, luego con el ["characters"] me arroja solo los capitulos 
                                                                                    # db.capitulos.find() = me da un objeto
    informacion_url=[]                                                              #PREGUNTA : poque tengo que usar [0]: quizás porque en ese objeto hay un elemento en una lista
    for url_personaje in personajes_lista:                                 

        try:                                                
            url=url_personaje
            response= requests.get(url)
            datos=response.json()
            informacion_url.append(datos)
        
        except requests.exceptions.JSONDecodeError:
            informacion_url.append("not found")   
            

    return render_template("personajes_capitulo.html", informacion_url=informacion_url, id=id) 