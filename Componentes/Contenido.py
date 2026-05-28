import pandas as pd
from datetime import datetime

class Contenido:
    #Vector/lista donde se almacena el contenido
    catalogo_general = {}

    #Atributos de la clase Contenido
    def __init__(self, titulo, anioDePublicacion, sinopsis, genero, tipo):
        self.titulo = titulo.strip()
        self.genero = genero
        self.sinopsis = sinopsis.strip()
        self.anioDePublicacion = anioDePublicacion
        self.tipo = tipo

    #Metodos de validacion
    @classmethod
    def verificarTituloRepetido(cls, titulo_ingresado):

        #Recorre los valores del vector
        for contenido in cls.catalogo_general.values():

            if contenido["titulo"].lower() == titulo_ingresado.strip().lower(): 
                print("El título del contenido ya existe, no se puede duplicar")
                return False
                
        return True
    
    @staticmethod
    def validarAnioPublicacion(fechaFormato):
        try:

            fecha_ingresada = datetime.strptime(fechaFormato, "%d/%m/%Y").date()
            fecha_actual = datetime.now().date() #Fecha actual
            
            if fecha_ingresada.year < 1850:
                print("El anio de publicacion no puede ser menor a 1850")
                return None
            
            if fecha_ingresada > fecha_actual:
                print("Recuerde que no puede ingresar fechas de estreno mayores al 2028")
                return None
                
            return fecha_ingresada
        
        except ValueError:
            print("Formato de fecha invalido, debe ser dd/mm/yyyy (Ej: 16/02/2000)")
            return None
    
    @staticmethod
    #Funcion con parametros reutilizables
    def validarCaracteres(texto, nombre, min = 10, max = 300):
        longitud = len(texto.strip())

        if longitud < min or longitud > max:
            print(f"{nombre} debe tener entre {min} y {max} caracteres (Ingresaste: {longitud}).")
            return False
        
        return True
    

    @staticmethod
    #Mini-menu para el atributo Genero
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

        #Condicional que verifica si no esta en valores numericos
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

            
            df_contenido.fillna("No aplica", inplace=True)

            pd.set_option("display.width", 180) 
            pd.set_option("display.max_columns", None)

            print("\n======= CATALOGO FUTIMEDIA =======\n")
            print(df_contenido)

        else:
            print("No se ha registrado ningun contenido")


#Clases hijas: 

class Pelicula(Contenido):
    contadorPeli = 1 #Contador del id Pelicula

    def __init__(self, titulo, anioDePublicacion, sinopsis, genero, duracionMinutos):
        self.titulo = titulo
        self.anioDePublicacion = anioDePublicacion
        self.sinopsis = sinopsis
        self.genero = genero
        self.id = Pelicula.contadorPeli
        Pelicula.contadorPeli += 1
        self.tipo = "Película"
        self.duracionMinutos = duracionMinutos #Atributo propio

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
    contadorSerie = 1 #Contador id Serie

    def __init__(self, titulo, anioDePublicacion, sinopsis, genero, temporadas):
        self.titulo = titulo
        self.anioDePublicacion = anioDePublicacion
        self.sinopsis = sinopsis
        self.id = Serie.contadorSerie
        Serie.contadorSerie += 1 
        self.genero = genero
        self.tipo = "Serie"
        self.temporadas = temporadas #Atributo propio

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
    contadorDocumental = 1 #Contador del id Documental

    def __init__(self, titulo, anioDePublicacion, sinopsis, genero, tema):
        self.titulo = titulo
        self.anioDePublicacion = anioDePublicacion
        self.sinopsis = sinopsis
        self.genero = genero
        self.id = Documental.contadorDocumental
        Documental.contadorDocumental += 1 
        self.tipo = "Documental"
        self.tema = tema #Atributo propio

    def listaDocumental(self):
        self.catalogo_general[f"Documental {self.id}"] = {
            "titulo": self.titulo,
            "anioDePublicacion": self.anioDePublicacion,
            "sinopsis": self.sinopsis,
            "genero": self.genero,
            "tema": self.tema,
            "tipo": self.tipo
        }