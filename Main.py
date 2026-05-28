from Componentes.Contenido import Pelicula, Serie, Documental, Contenido
from Componentes.Usuario import Usuario, validarCorreo
from Componentes.Favoritos import Favoritos
import time

k = 1

print("\n===============================")
print("      BIENVENIDO A FUTIMEDIA      ")
print("===============================")
time.sleep(2)         

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
                fechaFormato = input("Año de nacimiento (dd/mm/yyyy): ")
                validarFecha = Usuario.validarAnioNacimiento(fechaFormato)

                if validarFecha is not None:
                    fechaN = validarFecha
                    break  

            usuario = Usuario(nombre, apellido, correo, fechaN) 
            instancias_usuarios = usuario.registrar()


        case 2:

            print("Mostrando Usuarios...")
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
                print("Mostrando Contenido...")
                time.sleep(2)
                contenido.mostrar()


        case 7:
            print("\n--- AGREGAR A FAVORITOS ---")

            if not Contenido.catalogo_general:
                print("No hay contenido registrado en el catálogo general para agregar.")
                continue
                
            id_u = input("Digite el ID del Usuario al cual le desea ingresar las peliculas favoritas: ").strip()

            if (id_u.isdigit() and int(id_u)) not in Usuario.usuarios:
                print("El ID del usuario no se a encontrado vuelva a digitarlo por favor")
                continue           
                
            id_cont = input("\nIngrese el ID del contenido a agregar (Ej: 'Pelicula 1', 'Serie 1'): ").strip()
            
            if id_cont in Contenido.catalogo_general:
                favoritos = Favoritos(id_u, Contenido.catalogo_general[id_cont])
                favoritos.registrar(k)
                k += 1
            else:
                print("El ID del contenido no se a encontrado vuelva a digitarlo por favor")
                continue

        case 8:
            print("Mostrando favoritos...")
            time.sleep(2)
            favoritos.mostrar()
        case 9: 
            print("Hasta Luego esperamos verte pronto 👋")
            break