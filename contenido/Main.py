from Contenido import Pelicula, Serie, Documental, Contenido
from Usuario import Usuario, Favoritos, validarCorreo
import pandas as pd
import time

print("\n===============================")
print("      BIENVENIDO A FUTIMEDIA      ")
print("===============================")
time.sleep(2)

instancias_usuarios = {}           

while True:
    
    print(" (1) Registrar Usuario \n (2) Listar Usuarios \n (3) Registrar Serie \n (4) Registrar Pelicula \n (5) Registrar Documental \n (6) Listar Catalogo de contenidos \n (7) Agregar Contenido a Favoritos de un Usuario \n (8) Listar Favoritos de un Usuario \n (9) Salir del Menu ")

    try:
        eleccion = int(input("Ingresa una opcion: "))
    except ValueError:
        print("Por favor, ingrese solo números enteros")
        continue

    match eleccion:
        
        case 1:

            print("---------REGISTRAR A UN USUARIO---------")
            nombre = input("Ingrese el nombre del usuario nuevo: ")
            apellido = input("Ingrese el apellido del usuario nuevo: ")

            correo = validarCorreo()

            while True:
                fechaFormato = input("Año publicacion (dd/mm/yyyy): ")
                validarFecha = Usuario.validarAnioNacimiento(fechaFormato)

                if validarFecha is not None:
                    fechaN = validarFecha
                    break  

            usuario = Usuario(nombre, apellido, correo, fechaN) 
            instancias_usuarios = usuario.registrar()

        
        case 2:

            print("Mostrando Contenido...")
            time.sleep(2)
            usuario.mostrar()

        case 3:

            print("---- REGISTRAR SERIE ----")
            tipo = 2
            
            while True:
                titulo = input("Titulo: ").strip()

                if Contenido.verificarTituloRepetido(titulo):
                    break


            while True:
                fechaFormato = input("Año de publicación (dd/mm/yyyy): ")
                validarFecha = Contenido.validarAnioPublicacion(fechaFormato)
                
                if validarFecha is not None:
                    anioDePublicacion = validarFecha
                    break 

            while True:
                sinopsis = input("Sinopsis (10-300 caracteres): ")
                if Contenido.validarCaracteres(sinopsis, "Sipnosis"):
                    break

            genero = Contenido.seleccionarGenero()

            while True:
                    temporadas = input("Número de temporadas: ").strip()
                    temporadasValida = Contenido.validarEnteroPositivo(temporadas)

                    if temporadasValida is not None:
                        break
            
            contenido = Serie(titulo, anioDePublicacion, sinopsis, genero, temporadasValida)
            contenido.listarSerie()
            print("Serie registrada con exito.")

        
        case 4:

            print("---- REGISTRAR PELICULA ----")
            tipo = 1
            
            while True:
                titulo = input("Titulo: ").strip()

                if Contenido.verificarTituloRepetido(titulo):
                    break


            while True:
                fechaFormato = input("Año de publicación (dd/mm/yyyy): ")
                validarFecha = Contenido.validarAnioPublicacion(fechaFormato)
                
                if validarFecha is not None:
                    anioDePublicacion = validarFecha
                    break 

            while True:
                sinopsis = input("Sinopsis (10-300 caracteres): ")
                if Contenido.validarCaracteres(sinopsis, "Sipnosis"):
                    break

            genero = Contenido.seleccionarGenero()

            while True:
                duracionMinutos = input("Duración (minutos enteros): ").strip()
                duracionValida = Contenido.validarEnteroPositivo(duracionMinutos)
                if duracionValida is not None:
                    break

            contenido = Pelicula(titulo, anioDePublicacion, sinopsis, genero, duracionValida)
            contenido.listarPelicula()

            print("Pelicula registrada con exito.")


        case 5: 

            print("---- REGISTRAR DOCUMENTAL ----")
            tipo = 3
            
            while True:
                titulo = input("Titulo: ").strip()

                if Contenido.verificarTituloRepetido(titulo):
                    break


            while True:
                fechaFormato = input("Año de publicación (dd/mm/yyyy): ")
                validarFecha = Contenido.validarAnioPublicacion(fechaFormato)
                
                if validarFecha is not None:
                    anioDePublicacion = validarFecha
                    break 

            while True:
                sinopsis = input("Sinopsis (10-300 caracteres): ")
                if Contenido.validarCaracteres(sinopsis, "Sipnosis"):
                    break

            genero = Contenido.seleccionarGenero()

            while True:
                tema = input("Tema (5-35 caracteres): ")

                if Contenido.validarCaracteres(tema, "Tema", 5, 35):
                    break

            contenido = Documental(titulo, anioDePublicacion, sinopsis, genero, tema)
            contenido.listaDocumental()   

            print("Documental registrada con exito.")


        case 6:

            print("\n--- CATALOGO DE CONTENIDOS ---")
            if not Contenido.catalogo_general:
                print("No se ha registrado contenido en el catalogo.")
            else:
                contenido.mostrar()


        case 7:
            # print("\n--- AGREGAR A FAVORITOS ---")
            # if not Contenido.catalogo_general:
            #     print("No hay contenido registrado en el catálogo general para agregar.")
            #     continue
                
            # id_u = input("Ingrese el ID del Usuario: ").strip()

            # if id_u.isdigit() and int(id_u) in instancias_usuarios:
            #     usuario_actual = instancias_usuarios[int(id_u)]               
                
            #     id_cont = input("\nIngrese el ID del contenido a agregar (Ej: 'Pelicula 1', 'Serie 1'): ").strip()
                
            #     if id_cont in Contenido.catalogo_general:
            #         # Invoca el método de la clase hija Favoritos
            #         usuario_actual.agregarFavorito(id_cont, Contenido.catalogo_general[id_cont])
            #     else:
            #         print("El ID de contenido ingresado no existe.")
            # else:
            #     print("ID de usuario no válido o no registrado.")

        case 8:
            # print("\n--- MOSTRAR LISTA DE FAVORITOS ---")
            # id_u = input("Ingrese el ID del Usuario para ver sus favoritos: ").strip()
            
            # if id_u.isdigit() and int(id_u) in instancias_usuarios:
            #     usuario_actual = instancias_usuarios[int(id_u)]
            #     # Invoca el método heredado/propio para visualizar el DataFrame de favoritos
            #     usuario_actual.mostrarFavoritos()
            # else:
            #     print("ID de usuario no válido o no registrado.")
        case 9: 
            print("Hasta Luego esperamos verte pronto 👋")
            break