import ast
import csv

lista_autores=[]
class Libro():

    def __init__(self, id=None,titulo=None,genero=None,ISBN=None ,editorial=None,autor=None):
        
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.ISBN = ISBN
        self.editorial = editorial
        self.autor = autor         

        self.Lista_libros=open("Libros.csv", "a+", newline='')
        self.Lista_libros.seek(0)
 
        leer=self.Lista_libros.readlines()  

        if leer==[]:

            list=["id","titulo","genero","ISBN","editorial","autor"]
            archivo=csv.writer(self.Lista_libros)
            archivo.writerow(list)  
                 
    def leer_archivo(self):

        self.Lista_libros.seek(0)    
        archivo=csv.reader(self.Lista_libros)
        next(archivo,None)    
        
        for i,valor in enumerate(archivo):
            print(valor)
            if i>1:
                return
    
        if list(archivo)==[]:
            print("No hay libros guardados en archivo 'Libros.csv'")
            
    def listar_libros_guardados(self):

        self.Lista_libros.seek(0)   
        archivo=csv.reader(self.Lista_libros)

        next(archivo,None)
        
        if list(archivo)==[]:
            print("No hay libros guardados en archivo 'Libros.csv'")
            
        for i in list(archivo):
            print(i)

        self.Lista_libros.close()
    
    def listar_libros_sin_guardar(self):
        global lista_autores
        if lista_autores==[]:
            print("No hay libros sin guardar, Todos están guardados")
        for i in lista_autores:
            print(i)


    def agregar_libros(self):
        
        global lista_autores
        self.Lista_libros.seek(0)
    
        archivo=csv.reader(self.Lista_libros)

        Ide=len(list(archivo))

     
        Ide_actualizado=Ide+len(lista_autores)
        print(Ide_actualizado)

        lista_autores.append([f"{Ide_actualizado}",f"{self.titulo}" ,f"{self.genero}",f"{self.ISBN}",f"{self.editorial}", self.autor])

        self.Lista_libros.close()   
        print(f"SE AGREGO EL LIBRO {self.titulo} A LA LISTA CON ÉXITO")   

    def eliminar_libros(self):
        
        self.Lista_libros.seek(0)  

        archivo=list(csv.reader(self.Lista_libros))
     
        for i,value in enumerate(archivo):
            if value[0]==self.id:
                archivo.pop(i)

                with open("Libros.csv", "w", newline='') as file:  
                    writer=csv.writer(file)
                    writer.writerows(archivo)
            

                print(f"Libro {value[1]} ELIMINADO")
                self.Lista_libros.close()
                return
            
        print("NO SE ENCONTRÓ DICHO LIBRO CON ESE ID DADO, TIENE QUE INGRESAR UN ID QUE ESTÉ EN EL ARCHIVO 'Libros.csv' .")
        self.Lista_libros.close()


    def buscar_libro_ISBN_título(self):

        self.Lista_libros.seek(0)  
        archivo=csv.reader(self.Lista_libros)
        
        next(archivo,None)

        archivo=list(archivo)

        print("OPCIONES DE TITULO Y ISBN DISPONIBLES: ")    

        for i,value in enumerate(archivo):
            print("TITULO:",value[1],", ISBN:",value[3])


        codigo=input("ingrese el ISBN: ").lower()
        nombre_libro = input("ingrese el titulo del libro: ").lower()



        for i,value in enumerate(archivo):
            if value[3]==codigo or value[1]==nombre_libro:

                print("\n--------RESULTADOS---------\n")
                print("ID:",value[0])
                print("TITULO:",value[1])
                print("GENERO:",value[2])
                print("ISBN:",value[3])
                print("EDITORIAL",value[4])
                print("AUTOR:",value[5])

                return

        self.Lista_libros.close()

    def ordenar_libros(self):

        self.Lista_libros.seek(0)  
        archivo=(csv.reader(self.Lista_libros))

        next(archivo,None)

        archivo=list(archivo)

        ordenados=sorted(archivo, key=lambda titulo : titulo[1])

        emcabezado=["id","titulo","genero","ISBN","editorial","autor"]
        ordenados.insert(0,emcabezado)

        with open("Libros.csv", "w", newline='') as file:
            writer=csv.writer(file)
            writer.writerows(ordenados)

        self.Lista_libros.close()

    def buscar_libro_x_autor_editorial_género(self):

        self.Lista_libros.seek(0)  
        archivo=csv.reader(self.Lista_libros)

        next(archivo,None)

        archivo=list(archivo)

        print("OPCIONES DE AUTOR, EDITORIAL Y GENERO DISPONIBLES: ")    

        for i,value in enumerate(archivo):
            print("AUTOR:",value[5],", EDITORIAL:",value[4] ,", GENERO: ",value[2])

        autor_libro=input("Ingrese el autor: ").lower()
        editorial_libro = input("Ingrese el editorial libro: ").lower()
        genero_libro=input("Ingrese el genero: ").lower()

        encontrar_actor=False
        for i,value in enumerate(archivo):
            
            for autor in ast.literal_eval(value[5]):
                if autor.lower()==autor_libro:
                    encontrar_actor=True
                    
        
            if encontrar_actor==True or value[4].lower()==editorial_libro or value[2].lower()==genero_libro:

                print("\n--------RESULTADOS DEL LIBRO BUSCADO---------\n")
                print("TITULO:",value[1])
                print("GENERO:",value[2])
                print("ISBN:",value[3])
                print("EDITORIAL",value[4])
                print("AUTOR:",value[5])

                return

        self.Lista_libros.close()
        
    def buscar_libro_x_numero_de_autores(self,num):

        self.Lista_libros.seek(0)  
        archivo=csv.reader(self.Lista_libros)

        next(archivo,None)

        archivo=list(archivo)

        print(f"---LIBROS CON {num} AUTORES---")
        
        libros_disponibles=False
        for i,value in enumerate(archivo):

            lista_serializada=ast.literal_eval(value[5]) 
           
            if len(lista_serializada)==num:
                print(f"->{value[1]}")
                self.Lista_libros.close()
                libros_disponibles=True
                
        if libros_disponibles==False:
            print(f"No hay libros de {num} autor(es) guardados en el archivo 'Libros.csv'")
        
        self.Lista_libros.close()

    def editar_libro(self):

        self.Lista_libros.seek(0)  
        archivo=csv.reader(self.Lista_libros)

        archivo=list(archivo)
        
        libro_disponible=False
        for i,value in enumerate(archivo):
            if value[0]==self.id :

                print(f"\n--------RESULTADOS DEL LIBRO CON ID {self.id}---------\n")
                print("TIULO:",value[1])
                print("GENERO:",value[2])
                print("ISBN:",value[3])
                print("EDITORIAL",value[4])
                print("AUTOR:",value[5])

                posicion=i
                libro_disponible=True
                break   
       
        if libro_disponible:
            
            titulo_libro= input("ingrese el titulo actualizado: ")
            genero_libro=input("ingrese el genero actualizado: ")
            ISBN_libro=input("ingrese el ISBN actualizado: ")

            while not ISBN_libro.isdigit():
                ISBN_libro = input("Ingrese un ISBN VALIDO: ")

            editorial_libro=input("ingrese el editorial actualizado: ")

            archivo[posicion][1]=titulo_libro
            archivo[posicion][2]=genero_libro
            archivo[posicion][3]=ISBN_libro
            archivo[posicion][4]=editorial_libro


            cant_autores=input("cant_autores: ")

            while  not cant_autores.isdigit():
                cant_autores=input("Ingrese una cantidad numerica de autores: ")

            cant_autores=int(cant_autores)

            dicc={}
            for i in range(1,cant_autores+1):

                dicc[f"Autor{i}"] = input(f"ingrese el autor {i}: ")
            autor_libro=list(dicc.values())


            archivo[posicion][5]=autor_libro

            with open("Libros.csv", "w", newline='') as file: 
                writer=csv.writer(file)
                writer.writerows(archivo)
                    
        else:
            print(f"No existe el ID {self.id} en el archivo Libros.csv")

        self.Lista_libros.close()


    def guardar_libros(self):

        global lista_autores
        archivo=csv.writer(self.Lista_libros)
        archivo.writerows(lista_autores)            
        
        if lista_autores==[]:
            print("Aún no hay libros que guardar, agregue libros con la opcion 3.")
            self.Lista_libros.close() 
            return

        print("EL LIBRO SE GUARDÓ CON ÉXITO")
        print("A CONTINUACIÓN SE MUESTRAN LOS TITULOS DE LOS LIBROS RECIEN GUARDADOS:")

        for valor in lista_autores:
            print(f"Título: {valor[1]}")


        lista_autores=[]
        self.Lista_libros.close()  




def menu():
    global continuar

    print("================== REGISTRO DE LIBROS =======================")
    print("""Opción 1: Leer archivo de disco duro csv, se que cargaran 3 libros.
Opción 2: Listar libros.
Opción 3: Agregar libro.
Opción 4: Eliminar libro.
Opción 5: Buscar libro por ISBN o por título. 
Opción 6: Ordenar libros por título.
Opción 7: Buscar libros por autor, editorial o género.
Opción 8: Buscar libros por número de autores.
Opción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).
Opción 10: Guardar libros en archivo de disco duro (.txt o csv)
Opcion 11: Salir """)
    print("=============================================================")
    numero=input("\n Ingrese una de las opciones (numero): ")

    while numero not in ["1","2","3","4","5","6","7","8","9","10","11"]:
        numero=input("\n ingrese una opcion CORRECTA (numero):  ")
    numero=int(numero)

    if numero==1:
        Autor=Libro()
        Autor.leer_archivo()

    if numero==2:

        print("""\n----OPCIONES DE LISTADO----
        1). QUIERO LISTAR LOS LIBROS GUARDADOS EN MI ARCHIVO libros.csv
        2). QUIERO LISTAR LOS LIBROS NO GUARDADOS\n""")

        pregunta=input("Elige una opcion (1 o 2): ")

        while pregunta not in ["1","2"]:
            pregunta=input("Elige una opcion CORRECTA (1 o 2): ")
        
        Autor=Libro()
        if pregunta=="1":
            Autor.listar_libros_guardados()
        else:
            Autor.listar_libros_sin_guardar()

    if numero==3:

        titulo = input("Ingrese el titulo: ")
        genero = input("Ingrese el genero: ")
        ISBN_unico = input("Ingrese el ISBN: ")
        
        while not ISBN_unico.isdigit():
            ISBN_unico = input("Ingrese un ISBN VALIDO: ")
            
        editorial = input("ingrese el editorial: ")

        cant_autores=input("cant_autores: ")
        while  not cant_autores.isdigit():
            cant_autores=(input("cant_autores: "))
        cant_autores=int(cant_autores)

        dicc={}
        
        for i in range(1,cant_autores+1):
                
            dicc[f"Autor{i}"] = input(f"ingrese el autor {i}: ")

        autor=list(dicc.values())

        Autor=Libro(titulo=titulo,genero=genero,ISBN=ISBN_unico,editorial=editorial,autor=autor)
        Autor.agregar_libros()

    if numero==4:

        ide=input("ingrese el ID del libro que quiere eliminar: ")
        Autor=Libro(id=ide)
        Autor.eliminar_libros()

    if numero==5:
        Autor=Libro()
        Autor.buscar_libro_ISBN_título()

    if numero==6:
        Autor=Libro()
        Autor.ordenar_libros()

    if numero==7:
        Autor=Libro()
        Autor.buscar_libro_x_autor_editorial_género()

    if numero==8:

        num=input("ingrese cantidad de autores: ")
        
        while  not num.isdigit():
            num=input("ingrese nuevamente cantidad (entero) de autores: ")
        num=int(num)
        
        Autor=Libro()
        Autor.buscar_libro_x_numero_de_autores(num)

    if numero==9:

        Ide=input("ingrese el ID del libro que quiera editar: ")

        Autor=Libro(id = Ide)
        Autor.editar_libro()

    if numero==10:
        Autor=Libro()
        Autor.guardar_libros()

    if numero==11:
        continuar=False
        return print("A SALIDO DEL REGISTRO DE LIBROS")

 
    
    print("Ingrese 'y' para continuar con las opciones, Cualquier letra para cancelar.")
    pregunta=input("Desea continuar? (y/n): ").lower()
    if pregunta!="y":
        continuar=False
        return print("A SALIDO DEL REGISTRO DE LIBROS")

continuar=True
while continuar:
    menu()