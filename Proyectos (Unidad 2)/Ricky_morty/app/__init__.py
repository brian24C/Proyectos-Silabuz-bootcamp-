from flask import Flask, render_template
from flask_bootstrap import Bootstrap  #2
from app.config import Config
from .routes.ricky_morty import personajes_ruta
import hashlib
from app.db import db

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    Bootstrap(app)                      #2

    app.register_blueprint(personajes_ruta)

    

    def gravatar(id=""):
        url = "https://rickandmortyapi.com/api/character/avatar/"
        url=url + str(id) + ".jpeg"
        
        return "{url}".format(url=url)


    @app.route("/avatar/<id>")
    def avatar(id):
        id=int(id)
        filtro=db.personajes.find({"id":id})

        avt = gravatar(id)
        return render_template("avatar.html", avatar=avt, info=filtro)
        
    return app

