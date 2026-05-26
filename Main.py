from Contenido import Pelicula, Serie, Documental, Contenido
from menuFinalUsuario import Usuario, validarCorreo
import time


            

while True:
    print("\n===============================")
    print("      BIENVENIDO A FUTIMEDIA    ")
    print("===============================")
    time.sleep(2)
    print(" (1) Registrar Usuario \n (2) Listar Usuarios \n (3) Registrar Contenido \n (4) Listar Catalogo Contenido \n (5) Agregar Contenido a Favoritos \n (6) Listar Favoritos Usuario \n (7) Salir")

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

            validarCorreo()

            while True:
                fechaFormato = input("Año publicacion (dd/mm/yyyy): ")
                validarFecha = Usuario.validarAnioNacimiento(fechaFormato)

                if validarFecha is not None:
                    fechaN = validarFecha
                    break  

            menuUsuario = Usuario(nombre, apellido, correo, fechaN) 
            menuUsuario.registrar()

            # print("---- REGISTRAR CONTENIDO ----")

            # tipo = 0

            # while tipo not in [1, 2, 3]:
            #     opcion = input("Seleccione tipo: (1) Película (2) Serie (3) Documental: ").strip()
                
            #     match opcion:
            #         case "1":
            #             tipo = 1
            #         case "2":
            #             tipo = 2
            #         case "3":
            #             tipo = 3
            #         case _:
            #             print("Opcion invalida. Por favor, ingrese un numero del 1 al 3 (sin letras ni decimales)")
            
            # while True:
            #     titulo = input("Titulo: ").strip()

            #     if Contenido.verificarTituloRepetido(titulo):
            #         break


            # while True:
            #     fechaFormato = input("Año de publicación (dd/mm/yyyy): ")
            #     validarFecha = Contenido.validarAnioPublicacion(fechaFormato)
                
            #     if validarFecha is not None:
            #         anioDePublicacion = validarFecha
            #         break 

            # while True:
            #     sinopsis = input("Sinopsis (10-300 caracteres): ")
            #     if Contenido.validarCaracteres(sinopsis, "Sipnosis"):
            #         break

            # genero = Contenido.seleccionarGenero()

            # if tipo == 1:
            #     while True:
            #         duracionMinutos = input("Duración (minutos enteros): ").strip()
            #         duracionValida = Contenido.validarEnteroPositivo(duracionMinutos)
            #         if duracionValida is not None:
            #             break
                
            #     contenido = Pelicula(titulo, anioDePublicacion, sinopsis, genero, duracionValida)
            #     contenido.listarPelicula()

            # elif tipo == 2:
            #     while True:
            #         temporadas = input("Número de temporadas: ").strip()
            #         temporadasValida = Contenido.validarEnteroPositivo(temporadas)

            #         if temporadasValida is not None:
            #             break
            
            #     contenido = Serie(titulo, anioDePublicacion, sinopsis, genero, temporadasValida)
            #     contenido.listarSerie()

            # elif tipo == 3:
            #     while True:
            #         tema = input("Tema (5-35 caracteres): ")
            #         if Contenido.validarCaracteres(tema, "Tema", 5, 35):
            #             break

            #     contenido = Documental(titulo, anioDePublicacion, sinopsis, genero, tema)
            #     contenido.listaDocumental()

            # print("Registro completado con exito.")

        case 2:
            print("Mostrando Contenido...")
            time.sleep(2)
            menuUsuario.mostrar()

        #     print("\n--- CATALOGO DE CONTENIDOS ---")
        #     if not Contenido.catalogo_general:
        #         print("No se ha registrado contenido en el catalogo.")
        #     else:
        #         contenido.mostrar()
        
        # case 5:
        #     print("hasta luego esperamos verte pronto 👋"``)
        #     break

        # case _:
        #     print("Numero o dato ingresa es invalido, por favor intente de nuevo!")