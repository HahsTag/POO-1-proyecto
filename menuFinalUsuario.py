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
        case 2:
            menuUsuario.mostrar()
        case 3:
            print("hasta luego esperamos verte pronto 👋")
            break