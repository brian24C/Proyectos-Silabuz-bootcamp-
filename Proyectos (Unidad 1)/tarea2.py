import requests

def información_Nombre_Habilidad_URL(name_pokemon:str , url : str , pokemon_link : list , pokemon_habilidad : list) -> tuple[list, list]:
    
    url_pokemon=url+ name_pokemon
    response= requests.get(url_pokemon)
    datos=response.json()
    
    pokemon_habilidad_2=[]
   
    for y in datos["abilities"]:
        pokemon_habilidad_2.append(y["ability"]["name"])
        
    pokemon_link.append(datos["sprites"]["back_default"])
    pokemon_habilidad.append(pokemon_habilidad_2)
 
    return pokemon_link, pokemon_habilidad


def generacion():
    url_api_v2_pokemon="https://pokeapi.co/api/v2/pokemon/"
    url_generacion="https://pokeapi.co/api/v2/generation/"

    lista_generacion=["1","2","3","4","5","6","7","8"]

    generacion_elegida=input("Ingrese la generación (1 al 8): ").lower()

    while generacion_elegida not in lista_generacion:
        generacion_elegida= input("Ingrese UNA GENERACION VALIDA de pokemon: ").lower()

    url_generacion_elegida = url_generacion + generacion_elegida

    response_generacion= requests.get(url_generacion_elegida)
    datos_generacion = response_generacion.json()   

    #SE LISTAN EL NOMBRE, HABILIDAD Y LINK DE LOS POKEMONES DE LA GENERACION ESCOGIDA
    pokemon_nombre=[]
    pokemon_habilidad=[]
    pokemon_link=[]


    print("CARGANDO LOS DATOS...ESTO PUEDE TARDAR UNOS SEGUNDOS")

    for i in datos_generacion["pokemon_species"]:
        pokemon_nombre.append(i["name"])

        try:                                                 
            información_Nombre_Habilidad_URL(i["name"],url_api_v2_pokemon,pokemon_link,pokemon_habilidad)
        except requests.exceptions.JSONDecodeError:
            pokemon_link.append("No found")
            pokemon_habilidad.append("No found")     
    
    print(f"GENERACION: {generacion_elegida}")
    print("A continuación se muestran los NOMBRES, HABILIDADES, link de la imagen")
    print("(NOMBRE - HABILIDADES - LINK)")

    for i in list(zip(pokemon_nombre, pokemon_habilidad, pokemon_link)):
        print(i)
   

def forma():

    url_api_v2_pokemon="https://pokeapi.co/api/v2/pokemon/"
    url_forma="https://pokeapi.co/api/v2/pokemon-shape/"
    response= requests.get(url_forma)
    datos=response.json() 

    lista_forma=[]
    for i in datos["results"]:
        lista_forma.append(i["name"])

    print("-----------LISTA DE FORMAS DE POKEMON------------")
    print(lista_forma)  


    forma_escogida= input("Ingrese LA FORMA de pokemon: ").lower()

    while forma_escogida not in lista_forma:
        forma_escogida= input("Ingrese UNA FORMA VALIDA de pokemon: ").lower()

    url_forma_elegida=url_forma + forma_escogida

    response= requests.get(url_forma_elegida)
    datos=response.json()   

    #SE LISTAN EL NOMBRE, HABILIDAD Y LINK DE LOS POKEMONES DE LA FORMA ESCOGIDA

    pokemon_nombre=[]
    pokemon_habilidad=[]
    pokemon_link=[]

    print("CARGANDO LOS DATOS...ESTO PUEDE TARDAR UNOS SEGUNDOS")

    for i in datos["pokemon_species"]:
        pokemon_nombre.append(i["name"])

        try:                                                
            información_Nombre_Habilidad_URL(i["name"],url_api_v2_pokemon,pokemon_link,pokemon_habilidad)
        except requests.exceptions.JSONDecodeError:
            pokemon_link.append("No found")
            pokemon_habilidad.append("No found")

    print(f"TIPO: {forma_escogida}")
    print(f"A continuación se muestran los NOMBRES, HABILIDADES, link de la imagen . De todos aquellos que tienen LA FORMA de {forma_escogida}")
    print("(NOMBRE - HABILIDADES - LINK)")

    for i in list(zip(pokemon_nombre, pokemon_habilidad, pokemon_link)):
        print(i)


def habilidad():

    url_api_v2_pokemon="https://pokeapi.co/api/v2/pokemon/"
    url_Habilidad="https://pokeapi.co/api/v2/ability/"

    response= requests.get(url_Habilidad)
    datos=response.json() 

    lista_Habilidad=[]

    for i in datos["results"]:
        lista_Habilidad.append(i["name"])

    print("Lista de las 20 habilidades de los 327 del total de habilidades de pokemones:")
    print(lista_Habilidad)  

    pokemon_ability= input("Ingrese la HABILIDAD: ").lower()  
    while pokemon_ability not in lista_Habilidad:
        pokemon_ability= input("Ingrese una habilidad valida: ").lower()

    pokemon_url = url_Habilidad + pokemon_ability

    response= requests.get(pokemon_url)
    datos=response.json()   

    pokemon_nombre=[]
    pokemon_habilidad=[]
    pokemon_link=[]
    
    print("CARGANDO LOS DATOS...ESTO PUEDE TARDAR UNOS SEGUNDOS")

    for i in datos["pokemon"]:
        pokemon_nombre.append(i["pokemon"]["name"])

        try:                                                
            información_Nombre_Habilidad_URL(i["pokemon"]["name"],url_api_v2_pokemon,pokemon_link,pokemon_habilidad)
        
        except requests.exceptions.JSONDecodeError:
            pokemon_link.append("No found")
            pokemon_habilidad.append("No found")

    print(f"HABILIDAD: {pokemon_ability}")
    print(f"A continuación se muestran los NOMBRES, HABILIDADES y  LINK DE LA IMAGEN . De todos aquellos que tienen la habilidad de {pokemon_ability}")
    print("(NOMBRE - HABILIDADES - LINK)")

    for i in list(zip(pokemon_nombre, pokemon_habilidad, pokemon_link)):
        print(i)

def habitat():

    url_api_v2_pokemon="https://pokeapi.co/api/v2/pokemon/"
    url_Habitat="https://pokeapi.co/api/v2/pokemon-habitat/"
    response= requests.get(url_Habitat)
    datos=response.json()    

    lista_Habitat=[]

    for i in datos["results"]:
        lista_Habitat.append(i["name"])

    print("Lista de los habitat de los pokemones:")
    print(lista_Habitat) 

    pokemon_habitat= input("Ingrese el habitat: ").lower()
    while pokemon_habitat not in lista_Habitat:
        
        pokemon_habitat= input("Ingrese un habitat valido: ").lower()

    pokemon_url= url_Habitat + pokemon_habitat

    response= requests.get(pokemon_url)
    datos=response.json()   

    pokemon_nombre=[]
    pokemon_habilidad=[]
    pokemon_link=[]

    print("CARGANDO LOS DATOS...ESTO PUEDE TARDAR UNOS SEGUNDOS")

    for i in datos["pokemon_species"]:
        pokemon_nombre.append(i["name"])

        try:                                                
            información_Nombre_Habilidad_URL(i["name"],url_api_v2_pokemon,pokemon_link,pokemon_habilidad)
        
        except requests.exceptions.JSONDecodeError:
            pokemon_link.append("No found")
            pokemon_habilidad.append("No found")
    
    print(f"HABITAT: {pokemon_habitat}")
    print(f"A continuación se muestran los NOMBRES, HABILIDADES Y LINK DE LA IMAGEN. De todos aquellos que están en el HABITAT {pokemon_habitat}")
    print("(NOMBRE - HABILIDADES - LINK)")

    for i in list(zip(pokemon_nombre, pokemon_habilidad, pokemon_link)):
        print(i)

def tipo():

    url_api_v2_pokemon="https://pokeapi.co/api/v2/pokemon/"
    url_tipo="https://pokeapi.co/api/v2/type/"
    response= requests.get(url_tipo)
    datos=response.json() 

    lista_tipo=[]
    for i in datos["results"]:
        lista_tipo.append(i["name"])

    print("LISTA DE TIPOS DE POKEMON")
    print(lista_tipo)  

    pokemon_tipo= input("Ingrese el tipo de pokemon: ").lower()
    while pokemon_tipo not in lista_tipo:
        pokemon_tipo= input("Ingrese UN TIPO VALIDO de pokemon: ").lower()

    pokemon_url=url_tipo + pokemon_tipo

    response= requests.get(pokemon_url)
    datos=response.json()   


    pokemon_nombre=[]
    pokemon_habilidad=[]
    pokemon_link=[]


    print("CARGANDO LOS DATOS...ESTO PUEDE TARDAR UNOS SEGUNDOS...")

    for i in datos["pokemon"]:
        pokemon_nombre.append(i["pokemon"]["name"])

        try:                                                
            información_Nombre_Habilidad_URL(i["pokemon"]["name"],url_api_v2_pokemon,pokemon_link,pokemon_habilidad)
        
        except requests.exceptions.JSONDecodeError:
            pokemon_link.append("No found")
            pokemon_habilidad.append("No found")

    print(f"TIPO: {pokemon_tipo}")
    print(f"A continuación se muestran los NOMBRES, HABILIDADES, link de la imagen . De todos aquellos que tienen EL TIPO {pokemon_tipo}")
    print("(NOMBRE - HABILIDADES - LINK)")
    


    for i in list(zip(pokemon_nombre, pokemon_habilidad, pokemon_link)):
        print(i)

def menu():
    print("----------------------------------------------------MENU---------------------------------------------------")

    print("""Opción 1: Listar pokemons por generación.
    Opción 2: Listar pokemons por forma. 
    Opción 3: Listar pokemons por habilidad. 
    Opción 4: Listar pokemons por habitat. .
    Opción 5: Listar pokemons por tipo. """)



    opcion=input("INGRESE UNA OPCION DEL 1 AL 5: ")
    opciones=["1","2","3","4","5"]

    while opcion not in opciones:
        opcion=input("INGRESE UNA OPCION VALIDA DEL 1 AL 5: ")


    if opcion=="1":
        generacion()
    if opcion=="2":
        forma()
    if opcion=="3":
        habilidad()
    if opcion=="4":
        habitat()
    if opcion=="5":
        tipo()

    
menu()

print("Presione 'y' para continuar y cualquier letra para salir del programa")
continuar=input("Desea continuar con las opciones? (y/n): ")

while continuar=="y":
    menu()
    print("Presione 'y' para continuar y cualquier letra para salir del programa")
    continuar=input("Desea continuar con las opciones? (y/n): ")