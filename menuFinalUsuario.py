import pandas as pd
from datetime import datetime

class Usuario:
    contador = 1
    usuarios = {}
    def __init__(self, nombre, apellido, email, fecha):
        self.nombre = nombre.strip()
        self.apellido = apellido.strip() 
        self.email = email.strip()
        self.fecha = fecha
        self.id = Usuario.contador
        Usuario.contador += 1

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
                    fecha_actual = datetime.now().date()

                    if fecha_ingresada.year < 1920:
                        print("El año de publicación no puede ser menor a 1920 ")
                        return None

                    if fecha_ingresada > fecha_actual:
                        print("La fecha ingresada no puede ser mayor a la fecha actual")
                        return None

                    return fecha_ingresada
            except ValueError:
                    print("Formato de fecha inválido, debe ser dd/mm/yyyy (Ej: 16/02/2000)")
                    return None

         

    def mostrar(self):
        if self.usuarios:
            df_usuarios = pd.DataFrame(self.usuarios)
            df_usuarios = df_usuarios.T
            print(df_usuarios)
        else:
            print("No se han registrado usuarios")          

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
        
        return correo   