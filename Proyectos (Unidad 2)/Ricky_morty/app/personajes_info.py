
from models.personajes import Personajes
import requests
from db import db
class personajes():


    # for n in range(1,22):
    #     url_ricky_mortin=url+f"{n}"

    for n in range(1,22):

        url="https://rickandmortyapi.com/api/character?page="
            
        url_personaje=url+ str(n)
        response= requests.get(url_personaje)
        datos=response.json()
        

        for y in datos["results"]:
            infor=Personajes(y["id"], y["name"], y["status"], y["species"], y["type"], y["gender"], y["origin"]["url"], y["location"]["name"], y["image"], y["episode"], y["url"], y["created"])
            db.personajes.insert_one(infor.to_json())
            #lista_personajes.append()
        

 