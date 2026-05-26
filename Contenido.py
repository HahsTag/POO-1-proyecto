import pandas as pd
from datetime import datetime

#Clase Padre
class Contenido:
    catalogo_general = {}

    def __init__(self, titulo, anioDePublicacion, sinopsis, genero, tipo):
        self.titulo = titulo.strip()
        self.genero = genero
        self.sinopsis = sinopsis.strip()
        self.anioDePublicacion = anioDePublicacion
        self.tipo = tipo

    @classmethod
    def verificarTituloRepetido(cls, titulo_ingresado):

        for contenido in cls.catalogo_general.values():
            if contenido["titulo"].lower() == titulo_ingresado.strip().lower():
                print("El título del contenido ya existe, no se puede duplicar")
                return False
                
        return True
    

    @staticmethod
    def validarAnioPublicacion(fechaFormato):
        try:
            # Intentar convertir la cadena en una fecha real
            fecha_ingresada = datetime.strptime(fechaFormato, "%d/%m/%Y").date()
            fecha_actual = datetime.now().date() #Fecha actual
            
            if fecha_ingresada.year < 1850:
                print("El anio de publicacion no puede ser menor a 1850")
                return None
            
            if fecha_ingresada > fecha_actual:
                print("La fecha ingresada no puede ser mayor a la fecha actual")
                return None
                
            return fecha_ingresada
        
        except ValueError:
            print("Formato de fecha invalido, debe ser dd/mm/yyyy (Ej: 16/02/2000)")
            return None
    
    @staticmethod
    def validarCaracteres(texto, nombre, min = 10, max = 300):
        longitud = len(texto.strip())

        if longitud < min or longitud > max:
            print(f"{nombre} debe tener entre {min} y {max} caracteres (Ingresaste: {longitud}).")
            return False
        
        return True
    

    @staticmethod
    def seleccionarGenero():
        while True:

            print("\n--- Seleccione el Genero ---")
            print("1. Accion\n2. Comedia\n3. Drama\n4. Ciencia Ficcion\n5. Terror\n6. Informativo")

            opcion = input("Digite el número de la opción: ").strip()     
            match opcion:

                case "1": 
                    return "Acción"
                case "2": 
                    return "Comedia"
                case "3": 
                    return "Drama"
                case "4": 
                    return "Ciencia Ficción"
                case "5": 
                    return "Terror"
                case "6": 
                    return "Informativo"
                case _:
                    print("Opcion invalida, ingrese un número del 1 al 6.")

    @staticmethod
    def validarEnteroPositivo(valor):
        if not valor.isdigit():
            print(f"Debe ser un numero entero positivo (Ingresaste: {valor})")
            return None
        
        numero = int(valor)
        if numero <= 0:
            print(f"Debe ser mayor que cero (Ingresaste: {numero})")
            return None
        
        return numero

    
    def mostrar(self):
        if self.catalogo_general:
            df_contenido = pd.DataFrame(self.catalogo_general).T
            print(df_contenido)
        else:
            print("No se ha registrado contenido.")


#Estas son las clases hijas
class Pelicula(Contenido):
    contadorPeli = 1
    def __init__(self, titulo, anioDePublicacion, sinopsis, genero, duracionMinutos):
        self.titulo = titulo
        self.anioDePublicacion = anioDePublicacion
        self.sinopsis = sinopsis
        self.genero = genero
        self.duracionMinutos = duracionMinutos
        self.id = Pelicula.contadorPeli
        Pelicula.contadorPeli += 1
        self.tipo = "Película"

    def listarPelicula(self):
        self.catalogo_general[f"Pelicula {self.id}"] = {
            "titulo": self.titulo,
            "anioDePublicacion": self.anioDePublicacion,
            "sinopsis": self.sinopsis,
            "genero": self.genero,
            "duracionMinutos": self.duracionMinutos,
            "tipo": self.tipo
        }


class Serie(Contenido):
    contadorSerie = 1
    def __init__(self, titulo, anioDePublicacion, sinopsis, genero, temporadas):
        self.titulo = titulo
        self.anioDePublicacion = anioDePublicacion
        self.sinopsis = sinopsis
        self.id = Serie.contadorSerie
        Serie.contadorSerie += 1 
        self.genero = genero
        self.tipo = "Serie"
        self.temporadas = temporadas

    def listarSerie(self):    
        self.catalogo_general[f"Serie {self.id}"] = {
            "titulo": self.titulo,
            "anioDePublicacion": self.anioDePublicacion,
            "sinopsis": self.sinopsis,
            "genero": self.genero,
            "temporadas": self.temporadas,
            "tipo": self.tipo
        }


class Documental(Contenido):
    contadorDocumental = 1
    def __init__(self, titulo, anioDePublicacion, sinopsis, genero, tema):
        self.titulo = titulo
        self.anioDePublicacion = anioDePublicacion
        self.sinopsis = sinopsis
        self.genero = genero
        self.id = Documental.contadorDocumental
        Documental.contadorDocumental += 1 
        self.tipo = "Documental"
        self.tema = tema

    def listaDocumental(self):
        self.catalogo_general[f"Documental {self.id}"] = {
            "titulo": self.titulo,
            "anioDePublicacion": self.anioDePublicacion,
            "sinopsis": self.sinopsis,
            "genero": self.genero,
            "tema": self.tema,
            "tipo": self.tipo
        }

# Menú principal
eleccion = 0
while (True):
    print("\n===============================")
    print("       MENU DE CONTENIDO")
    print("===============================")
    print(" (1) Registrar nuevo contenido \n (2) Mostrar catalogo \n (3) Salir")

    try:
        eleccion = int(input("Ingresa una opcion: "))
    except ValueError:
        print("Por favor, ingrese solo números enteros")
        continue

    match eleccion:
        case 1:
            print("---- REGISTRAR CONTENIDO ----")

            tipo = 0

            while tipo not in [1, 2, 3]:
                opcion = input("Seleccione tipo: (1) Película (2) Serie (3) Documental: ").strip()
                
                match opcion:
                    case "1":
                        tipo = 1
                    case "2":
                        tipo = 2
                    case "3":
                        tipo = 3
                    case _:
                        print("Opcion invalida. Por favor, ingrese un numero del 1 al 3 (sin letras ni decimales)")
            
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

            if tipo == 1:
                while True:
                    duracionMinutos = input("Duración (minutos enteros): ").strip()
                    duracionValida = Contenido.validarEnteroPositivo(duracionMinutos)
                    if duracionValida is not None:
                        break
                
                contenido = Pelicula(titulo, anioDePublicacion, sinopsis, genero, duracionValida)
                contenido.listarPelicula()

            elif tipo == 2:
                while True:
                    temporadas = input("Número de temporadas: ").strip()
                    temporadasValida = Contenido.validarEnteroPositivo(temporadas)

                    if temporadasValida is not None:
                        break
            
                contenido = Serie(titulo, anioDePublicacion, sinopsis, genero, temporadasValida)
                contenido.listarSerie()

            elif tipo == 3:
                while True:
                    tema = input("Tema (5-35 caracteres): ")
                    if Contenido.validarCaracteres(tema, "Tema", 5, 35):
                        break

                contenido = Documental(titulo, anioDePublicacion, sinopsis, genero, tema)
                contenido.listaDocumental()

            print("Registro completado con exito.")

        case 2:
            print("\n--- CATALOGO DE CONTENIDOS ---")
            if not Contenido.catalogo_general:
                print("No se ha registrado contenido en el catalogo.")
            else:
                contenido.mostrar()
        
        case 5:
            print("Hasta luego, administrador polla peque.")
            break

        case _:
            print("Numero o dato ingresa es invalido, por favor intente de nuevo!")