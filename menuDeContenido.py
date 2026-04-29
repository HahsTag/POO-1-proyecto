import pandas as pd
import time

#Clase Padre
class Contenido:
    vector = {}
    contador = 1
    def __init__(self, titulo, anioDePublicacion, sinopsis, genero, tipo, isId=False):
        self.titulo = titulo
        self.genero = genero
        self.sinopsis = sinopsis
        anioFormato = time.strftime(anioDePublicacion, "%d/%m/%Y")
        self.anioDePublicacion = anioFormato
        self.id = Contenido.contador
        Contenido.contador += 1   #Aumenta el id consecutivamente sin repetirse
        self.tipo = tipo  
        self.isId = isId

    def registrar(self):
        for clave in self.vector.keys():
            if self.vector[clave]["titulo"].lower() == self.titulo.lower():
                print("Ese contenido ya existe, no se puede duplicar.")
                self.isId = True
                return

        self.vector[self.id] = {
            "titulo": self.titulo,
            "anioDePublicacion": self.anioDePublicacion,
            "sinopsis": self.sinopsis,
            "genero": self.genero,
            "tipo": self.tipo
        }

        print("El contenido ha sido registrado.")

    def mostrar(self):
        if self.vector:
            df_contenido = pd.DataFrame(self.vector).T
            print(df_contenido)
        else:
            print("No se ha registrado contenido.")


#Estas son las clases hijas
class Pelicula(Contenido):
    def __init__(self, titulo, anioDePublicacion, sinopsis, genero, duracionMinutos):
        self.titulo = titulo
        self.anioDePublicacion = anioDePublicacion
        self.sinopsis = sinopsis
        self.genero = genero
        self.duracionMinutos = duracionMinutos
        self.id = Contenido.contador
        Contenido.contador += 1
        self.tipo = "Película"
        self.isId = False

        self.vector[self.id] = {
            "titulo": titulo,
            "anioDePublicacion": anioDePublicacion,
            "sinopsis": sinopsis,
            "genero": genero,
            "duracionMinutos": duracionMinutos,
            "tipo": "Película"
        }

class Serie(Contenido):
    def __init__(self, titulo, anioDePublicacion, sinopsis, genero, temporadas):
        self.titulo = titulo
        self.anioDePublicacion = anioDePublicacion
        self.sinopsis = sinopsis
        self.genero = genero
        self.id = Contenido.contador
        Contenido.contador += 1
        self.tipo = "Serie"
        self.isId = False

        self.temporadas = temporadas

        self.vector[self.id] = {
            "titulo": titulo,
            "anioDePublicacion": anioDePublicacion,
            "sinopsis": sinopsis,
            "genero": genero,
            "temporadas": temporadas,
            "tipo": "Serie"
        }

class Documental(Contenido):
    def __init__(self, titulo, anioDePublicacion, sinopsis, genero, tema):
        self.titulo = titulo
        self.anioDePublicacion = anioDePublicacion
        self.sinopsis = sinopsis
        self.genero = genero
        self.id = Contenido.contador
        Contenido.contador += 1
        self.tipo = "Documental"
        self.isId = False

        self.tema = tema

        self.vector[self.id] = {
            "titulo": titulo,
            "anioDePublicacion": anioDePublicacion,
            "sinopsis": sinopsis,
            "genero": genero,
            "tema": tema,
            "tipo": "Documental"
        }


# Menú principal
eleccion = 0
while eleccion != 5:
    eleccion = int(input("\nMenú de Contenido\n (1) Registrar nuevo contenido \n (2) Mostrar contenido \n (3) Actualizar contenido \n (4) Eliminar contenido \n (5) Salir \n Opción: "))
    match eleccion:
        case 1:
            print("---- REGISTRAR CONTENIDO ----")
            tipo = int(input("Seleccione tipo: (1) Película (2) Serie (3) Documental: "))
            titulo = input("Título: ")
            anioDePublicacion = input("Año de publicacion (dd/mm/yyyy): ")
            sinopsis = input("Sinopsis: ")
            genero = input("Género: ")

            if tipo == 1:
                duracionMinutos = input("Duración (minutos): ")
                contenido = Pelicula(titulo, anioDePublicacion, sinopsis, genero, duracionMinutos)
            elif tipo == 2:
                temporadas = int(input("Número de temporadas: "))
                contenido = Serie(titulo, anioDePublicacion, sinopsis, genero, temporadas)
            elif tipo == 3:
                tema = input("Tema principal del documental: ")
                contenido = Documental(titulo, anioDePublicacion, sinopsis, genero, tema)

            print("Registro completado.")

        case 2:
            contenido.mostrar()
       
        case 5:
            print("Hasta luego, administrador polla peque.")
            break
