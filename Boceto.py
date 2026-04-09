import pandas as pd

class Peliculas:
    peliculas = {} 

    def __init__(self, titulo, autor, id, isValid = False):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.isValid = isValid

    def registrar(self):
            self.verificarID()
            if self.isValid == True:
                print("El identificador ya es existente digite uno diferente")
                return
            else: 
                self.peliculas[self.id] = {
                    "tituloPeli": self.titulo,
                    "autorPeli": self.autor
                }
                print("La pelicula se a registrado exitosamente!!!!!")

    def verificarID(self):
        for clave in self.peliculas.keys():
            if clave == self.id:
                self.isValid = True
                return

    def verPelicula(self):
        df_peliculas = pd.DataFrame(self.peliculas)
        print(df_peliculas)

    def actualizarPelicula(self):
        eleccionId = int(input("Ingresa el ID de la pelicula que desea actualizar: ")) 
        print(" ==== Datos actuales ==== ")
        print(self.peliculas[eleccionId])
        k = 0
        for id, valor in self.peliculas.items():
           
            if id == eleccionId:
                print(" ===== Ingresa los nuevos datos ===== ")
                nuevoTitulo = input("Ingresa un nuevo titulo: ")
                nuevoAutor = input("Ingresa un nuevo autor: ")  

                self.peliculas[eleccionId]["tituloPeli"] = nuevoTitulo
                self.peliculas[eleccionId]["autorPeli"] = nuevoAutor
        #     else:
        #         k += 1
        # if k == len(self.peliculas):
        #     print("Recuerde que debe elegir un id existente")


        
    def borrarPelicula(self):
        eleccionId = int(input("Digite el id de la pelicula: "))
        for id, valor in list(self.peliculas.items()):
            if id == eleccionId:
                print("se va a borrar la pelicula con los datos: *datos del diccionario*")
                del self.peliculas[id]
                
eleccion = 0
while eleccion != 5:
    eleccion = int(input("Elegi: "))
    match eleccion:
        case 1:      
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            id = int(input("Id: "))
            listaP = Peliculas(titulo, autor, id)
            listaP.registrar()
        case 2:
            listaP.verPelicula()
        case 3:
            listaP.actualizarPelicula()
        case 4:
            listaP.borrarPelicula()
        case 5:
            print("Chau ;)")
            eleccion =5