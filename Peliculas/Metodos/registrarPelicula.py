from Peliculas.Class.pelicula import Pelicula

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