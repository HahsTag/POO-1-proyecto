peliculas = {}

class Pelicula: 
    
    contadorId = 1 

    def __init__(self, tituloPeli, autorPeli, descripcionPeli, anioPeli, generoPeli, isFavorito):
        
        self.idPeli = Pelicula.contadorId
        Pelicula.contadorId += 1
        
        self.tituloPeli = tituloPeli
        self.autorPeli = autorPeli
        self.descripcionPeli = descripcionPeli
        self.anioPeli = anioPeli
        self.generoPeli = generoPeli
        self.isFavorito = isFavorito
    
def registrarPelicula(peliculas):
    print("--------- REGISTRAR UNA PELICULA ---------")

    titulo = input("Ingresa el titulo de la pelicula: ")
    autor = input("Ingresa el autor de la pelicula: ")
    descripcion = input("Ingresa la descripcion de la pelicula: ")
    anio = input("Ingresa el anio de la pelicula: ")
    genero = input("Ingresa el genero de la pelicula: ")

    nuevaPelicula = Pelicula(titulo, autor, descripcion, anio, genero)

    peliculas.append(nuevaPelicula)

    print("✅ Se ha registrado la nueva pelicula correctamente.")

    
while True:
    print("======== MENU DE PELICULAS ========")
    eleccion = input("Que deseas realizar \n (1) Registrar una nueva pelicula \n (2) Ver todas de peliculas registradas \n (3) Salir de este menu \n Ingresa tu opcion: ")

    match eleccion:
        case "1":
            registrarPelicula(peliculas)
            
        case _:
            print("Opcion invalida")
    


