
## LO QUE APRENDÍ CON FLASK:
- Crear una estructura básica para una página web con FLASK
- Conectarme a una BBDD NOSQL
- Extraer información de la BBDD y mostrarlo en una pagina web
- Usar querys para encontrar o insertar información  (por ejem: db.personajes.insert_one(infor.to_json()))




### Planteamiento del problema

Hacer uso de la API y extraer todos los personajes de la página 1 a la 21. Para extraer personajes por página, use la siguiente ruta.

​https://rickandmortyapi.com/api/character?page=n

Donde "n" es el número de página.

Debe insertar los datos obtenidos en una colección de MongoDB.

La estructura del Json obtenido es el siguiente:

{
    info:{ "Información de la página, conteo de personajes, página siguiente y anterior, etc." },
    results:{ "Array de personajes" }
}

Únicamente debe insertar los results en la base de datos.

Crearemos la siguiente vista HTML haciendo uso de PyMongo. (No centrarse en lo visual, lo importante es que retornen los datos de los personajes en pantalla).

![Rick_morty](https://user-images.githubusercontent.com/109192347/204162672-d356b53b-eb18-404d-acdf-0dd715c99bb4.png)

Los personajes deben estar ordenados por el id de forma descendente.

Perfil
Crear un perfil en el que se pueda visualizar más datos del personaje: Capitulos en los que aparece, etc.
