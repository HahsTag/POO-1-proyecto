class Peliculas:
    peliculas = {}
    contadorId = 1  

    # def __init__(self, titulo, autor, ):
    #     self.titulo = titulo
    #     self.autor = autor
    #     self.peliculas = peliculas

    def registrar(self):
        global contadorId
        self.contadorId
        self.peliculas

        for i in range(2):
            
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            
            self.peliculas[self.contadorId] = {
                "tituloPeli": titulo,
                "autorPeli": autor
            }
            self.contadorId += 1

    def verPelicula(self):
        print(self.peliculas)

    def actualizarPelicula(self):
        eleccion = int(input("Ingresa el ID de la pelicula que desea actualizar: ")) 
        print(" ==== Datos actuales ==== ")
        print(self.peliculas[eleccion])
        
        for id, valor in self.peliculas.items():
            if id == eleccion:
                print(" ===== Ingresa los nuevos datos ===== ")
                nuevoTitulo = input("Ingresa un nuevo titulo: ")
                nuevoAutor = input("Ingresa un nuevo autor: ")  

                self.peliculas[eleccion]["tituloPeli"] = nuevoTitulo
                self.peliculas[eleccion]["autorPeli"] = nuevoAutor

            else:
                print("El id de la pelicula no esta existente.")
        
    def borrarPelicula(self):
        eleccion = int(input("Digite el id de la pelicula: "))
        for id, valor in list(self.peliculas.items()):
            if id == eleccion:
                print("se va a borrar la pelicula con los datos: *datos del diccionario*")
                del self.peliculas[id]

#ENCAPSULAMIENTO
# [(1, {}), (2, {})]
# {(1, {}), 2: {}}

                

listaP = Peliculas()
listaP.registrar()
listaP.verPelicula()
listaP.actualizarPelicula()
listaP.verPelicula()
listaP.borrarPelicula()
listaP.verPelicula()