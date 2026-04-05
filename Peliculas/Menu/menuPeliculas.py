from Peliculas.Metodos.registrarPelicula import registrarPelicula

peliculas = []

while True:
    print("======== MENU DE PELICULAS ========")
    eleccion = input("Que deseas realizar \n (1) Registrar una nueva pelicula \n (2) Ver todas de peliculas registradas \n (3) Salir de este menu \n Ingresa tu opcion: ")

    match eleccion:
        case "1":
            registrarPelicula(peliculas)
            
        case _:
            print("Opcion invalida")