import pandas as pd
from datetime import datetime
from Contenido import Pelicula, Serie, Documental, Contenido

class Usuario:
    contador = 1
    usuarios = {}

    def __init__(self, nombre, apellido, email, fecha):
        self.nombre = nombre.strip()
        self.apellido = apellido.strip() 
        self.email = email
        self.fecha = fecha
        self.id = Usuario.contador
        Usuario.contador += 1
        self.favoritos = []
        

    def registrar(self):
            
        self.usuarios[self.id] = {
        "nombre": self.nombre,
        "apellido": self.apellido,
        "correo": self.email,
        "fecha de nacimiento": self.fecha
        } 
        print("El usuario a sido registrado") 
            
    @staticmethod       
    def validarAnioNacimiento(fechaFormato):
            try:

                    fecha_ingresada = datetime.strptime(fechaFormato, "%d/%m/%Y").date()


                    if fecha_ingresada.year < 1920:
                        print("El año de publicación no puede ser menor a 1920 ")
                        return None

                    if fecha_ingresada.year > 2016:
                        print("La fecha ingresada no puede ser mayor a la fecha actual")
                        return None

                    return fecha_ingresada
            
            except ValueError:
                    print("Formato de fecha inválido, debe ser dd/mm/yyyy (Ej: 16/02/2000)")
                    return None

    def mostrar(self):
        if self.usuarios:

            df_usuarios = pd.DataFrame(self.usuarios).T

            df_usuarios.fillna("No Aplica", inplace=True)

            pd.set_option("display.width", 180)
            pd.set_option("display.max_columns", None)

            print("\n======= USUARIOS FUTIMEDIA =======\n")
            print(df_usuarios)
        else:
            print("No se han registrado ningun usuario")
            


class Favoritos(Usuario):

    def __init__(self, nombre, apellido, email, fecha):
        super().__init__(nombre, apellido, email, fecha)
        self.lista_favoritos = {}  

    def agregarFavorito(self, id_contenido, datos_contenido):
        if id_contenido in self.lista_favoritos:
            print(f"'{datos_contenido['titulo']}' ya está en tus favoritos.")
            return False
        
        self.lista_favoritos[id_contenido] = datos_contenido
        print(f"'{datos_contenido['titulo']}' ha sido añadido a tus favoritos con éxito.")
        return True
    
    def mostrar(self):
        if self.lista_favoritos:

            df_favoritos = pd.DataFrame(self.lista_favoritos).T

            df_favoritos.fillna("No Aplica", inplace=True)

            pd.set_option("display.width", 180)
            pd.set_option("display.max_columns", None)

            print("\n======= USUARIOS FUTIMEDIA =======\n")
            print(df_favoritos)
        else:
            print("No se han registrado ningun usuario")
    

def validarCorreo():
    global correo
    while True:
        correo = input("Ingrese el correo del usuario nuevo: ")

        if " " in correo:
            print("Recuerde que el correo no puede tener espacios!!!")
            continue

        if correo.count("@") != 1:
            print("Recuerde que el correo debe tener exactamente un @")
            continue
        
        nombre, arrova, directorio = correo.partition("@")
        if directorio.count(".") != 1:
            print("Recuerde que el correo debe tener un directorio por ejemplo (.com)")
            continue
        
        return correo.strip()
