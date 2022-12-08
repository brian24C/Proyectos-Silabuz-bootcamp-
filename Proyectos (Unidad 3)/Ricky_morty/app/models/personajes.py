import datetime

class Personajes:
    def __init__(self,id,name,status,species,type,gender,origin,location,image,episode,url,created):
        self.id=id
        self.name=name
        self.status=status
        self.species=species
        self.type=type
        self.gender = gender
        self.origin = origin
        self.location = location
        self.image = image
        self.episode = episode
        self.url = url
        self.created = created

        
    def to_json(self):
        return {
            'id':self.id,
            'name':self.name,
            'status':self.status,
            'species':self.species,
            'type':self.type,
            'gender':self.gender,
            'origin':self.origin,
            'location':self.location,
            'image':self.image,
            'episode':self.episode,
            'url':self.url,
            'created':self.created

        }
    

class Capitulo:
    def __init__(self,id,name,air_date,episode,characters,url,created):
        self.id=id
        self.name=name
        self.air_date=air_date
        self.episode = episode
        self.characters = characters
        self.url = url
        self.created = created

        
    def to_json(self):
        return {
            'id':self.id,
            'name':self.name,
            'air_date':self.air_date,
            'episode':self.episode,
            'characters':self.characters,
            'url':self.url,
            'created':self.created
        }
    
