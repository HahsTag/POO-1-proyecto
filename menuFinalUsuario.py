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
                
                    fecha_objeto = datetime.strptime(fechaFormato, "%d/%m/%Y").date()
                    fecha_actual = datetime.now().date()

                    if fecha_objeto.year < 1920:
                        print("El año de publicación no puede ser menor a 1920 ")
                        return None

                    if fecha_objeto > fecha_actual:
                        print("La fecha ingresada no puede ser mayor a la fecha actual")
                        return None

                    return fecha_objeto
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

    


eleccion = 0
import time

class Usuario:
    vector = {}
    contador = 0

    def __init__(self, nombre, apellido, correo, fecha, contra):
        self.nombre = nombre
        self.apellido = apellido 
        self.correo = correo
        self.contra = contra
        fechaNacimiento = time.strptime(fecha, "%d/%m/%Y")
        self.fecha = time.strftime("%d/%m/%Y", fechaNacimiento)

    def registrar(self):
        
        Usuario.contador += 1
        id = Usuario.contador
        self.vector[id] = {
        "nombre": self.nombre,
        "apellido": self.apellido,
        "correo": self.correo,
        "fecha de nacimiento": self.fecha,
        "contraseña": self.contra
        } 
        print("El usuario a sido registrado")
    
    def listar(self):
            if self.vector:
                df_usuarios = pd.DataFrame(self.vector)
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
    

while eleccion != 5:
    eleccion = int(input("Digite la eleccion \n (1) Si desea Ingresar un usuario nuevo \n (2) Si desesa ver cuantos usuarios hay registrados \n (3) salir \n ingresa tu opcion: "))
=======
while (True):
    try:
        eleccion = int(input("Digite la eleccion \n (1) Si desea Ingresar un usuario nuevo \n (2) Si desesa ver cuantos usuarios hay registrados \n (3) Si desea actualizar la informacion de un usuario ya existente \n (4) Si desea Borrar a un usuario \n (5) salir \n ingresa tu opcion: "))
    except ValueError:
        print("El dato ingresado no es valido porfavor ingrese otro: ") 
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
            fechaN = input("Ingrese la fecha de nacimiento del usuario (DD/MM/AAAA): ")
            contra = input("Ingrese la contraseña del usuario nuevo: ")      
            menuUsuario = Usuario(nombre, apellido, correo, fechaN, contra)
            menuUsuario.registrar()
        case 2:
            menuUsuario.listar()
            time.sleep(3)
        case 3:
            print("hasta luego esperamos verte pronto 👋")
            break
    