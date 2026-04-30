from Contenido import Pelicula, Serie, Documental, Contenido
from Favoritos import Favorito

menuUsuario = None
contenido = None

def mostrar_menu():
    print("\n" + "="*40)
    print("        SISTEMA DE GESTIÓN ")
    print("="*40)
    print("1. Registrar usuario")
    print("2. Listar usuarios")
    print("3. Registrar contenido")
    print("4. Listar contenido")
    print("5. Agregar favorito")
    print("6. Ver favoritos de un usuario")
    print("7. Salir")
    print("="*40)

while True:
    try:
        mostrar_menu()
        eleccion = int(input("Selecciona una opción: "))
    except:
        print("Entrada inválida, intenta de nuevo.")
        continue

    match eleccion:

        case 1:
            print("\n--- USUARIO ---")
        case 2:
            print("\n--- LISTA DE USUARIOS ---")
           
        case 3:
            print("\n--- REGISTRO DE CONTENIDO ---")
            print("1. Película")
            print("2. Serie")
            print("3. Documental")

            tipo = int(input("Selecciona el tipo: "))

            titulo = input("Título: ")
            anio = input("Fecha de publicación (DD/MM/AAAA): ")
            sinopsis = input("Sinopsis: ")
            genero = input("Género: ")

            if tipo == 1:
                duracion = input("Duración (minutos): ")
                contenido = Pelicula(titulo, anio, sinopsis, genero, duracion)
            elif tipo == 2:
                temporadas = int(input("Número de temporadas: "))
                contenido = Serie(titulo, anio, sinopsis, genero, temporadas)
            elif tipo == 3:
                tema = input("Tema del documental: ")
                contenido = Documental(titulo, anio, sinopsis, genero, tema)

            print("Contenido registrado correctamente.")


        case 4:
            print("\n--- LISTA DE CONTENIDO ---")
            if Contenido.vector:
                contenido.mostrar()
            else:
                print("No hay contenido registrado.")


        case 5:
            print("\n--- AGREGAR A FAVORITOS ---")

   
        case 6:
            print("\n--- FAVORITOS DEL USUARIO ---")



        case 7:
            print("\nGracias por usar el sistema. ¡Hasta luego!")
            break

        case _:
            print("Opción inválida, intenta de nuevo.")