import pandas as pd

class Menu:
    vector = {}
    def __init__(self, nombre, fecha, id, isId = False):
        self.nombre = nombre
        self.fecha = fecha 
        self.id = id
        self.isId = isId

    def registrar(self):
        for clave in self.vector.keys():
            if clave == self.cedula:
                print("Ese numero de cedula ya existe")
                self.isCeV == True
                return

        self.vector[self.id] = {
        "nombre": self.nombre,
        "id": self.id,
        "fecha": self.fecha
        } 

        print("El usuario a sido registrado")

    
    def mostrar(self):
        if self.vector:
            df_usuarios = pd.DataFrame(self.vector)
            df_usuarios = df_usuarios.T
            print(df_usuarios)
        else:
            print("No se han registrado usuarios")           

    def actualizar(self):
            idE = int(input("Digite el identificador del cual desea modificar la informacion: "))
            k = 0
            for clave in self.vector.keys():
                if clave == idE:
                    pass

    def eliminar(self):
            idE = int(input("Digite el identifcador del cual eliminar: "))
            for clave in list(self.vector.keys()):
                if clave == idE:
                    print(f"Se a eliminado correctamente el dato con id: {self.vector[clave]}")
                    del self.vector[clave]



class Usuario(Menu):
    def __init__(self, nombre, apellido, correo, fecha, id, contra, isId = False):
        self.nombre = nombre
        self.apellido = apellido 
        self.correo = correo
        self.fecha = fecha 
        self.id = id
        self.contra = contra
        self.isId = isId

    def registrar(self):

        for clave in self.vector.keys():
            if clave == self.id:
                print("Ese numero de cedula ya existe vuelva a digitar nuevamente los datos!!!")
                self.isId == True
                return

        self.vector[self.id] = {
        "nombre": self.nombre,
        "apellido": self.apellido,
        "correo": self.correo,
        "fecha": self.fecha,
        "contraseña": self.contra
        } 
        print("El usuario a sido registrado")           

    def actualizar(self):
            idE = int(input("Digite la cedula del usuario al cual desea modificar la informacion: "))

            for clave in self.vector.keys():
                if clave == idE:
                    eleccionUp = int(input("Que informacion desea modificar: \n (1) Nombre/s \n (2) Correo \n (3) Todas las anteriores \n (4) ir atras \n Elija: "))
                    match eleccionUp:
                            case 1:
                                self.vector[clave]["nombre"] = input("Ingrese el nombre nuevo para el usuario: ")
                                self.vector[clave]["apellido"] = input("Ingrese el apellido nuevo para el usuario: ")
                            case 2:
                                

                                while True:
                                    correoNuevo = input("Ingrese el correo nuevo para el usuario: ")

                                    if " " in correoNuevo:
                                        print("Recuerde que el correo no puede tener espacios!!!")
                                        continue

                                    if correoNuevo.count("@") != 1:
                                        print("Recuerde que el correo debe tener exactamente un @")
                                        continue
                                    
                                    self.vector[clave]["correo"] = correoNuevo
                                    break

                            case 3:
                                self.vector[clave]["nombre"] = input("Ingrese el nombre nuevo para el usuario: ")
                                self.vector[clave]["apellido"] = input("Ingrese el apellido nuevo para el usuario: ")
                            

                                while True:
                                    correoNuevo = input("Ingrese el correo nuevo para el usuario: ")

                                    if " " in correoNuevo:
                                        print("Recuerde que el correo no puede tener espacios!!!")
                                        continue

                                    if correoNuevo.count("@") != 1:
                                        print("Recuerde que el correo debe tener exactamente un @")
                                        continue
                                    
                                    self.vector[clave]["correo"] = correoNuevo
                                    break


                            case 4:
                                break


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

        return correo
    

while eleccion != 5:
    eleccion = int(input("Digite la eleccion \n (1) Si desea Ingresar un usuario nuevo \n (2) Si desesa ver cuantos usuarios hay registrados \n (3) Si desea actualizar la informacion de un usuario ya existente \n (4) Si desea Borrar a un usuario \n (5) salir \n ingresa tu opcion: "))
    match eleccion:
        case 1:
            print("---------REGISTRAR A UN USUARIO---------")
            nombre = input("Ingrese el nombre del usuario nuevo: ")
            apellido = input("Ingrese el apellido del usuario nuevo: ")
            validarCorreo()
            fechaN = input("Ingrese la fecha de nacimiento del usuario nuevo: ")
            contra = input("Ingrese la contraseña del usuario nuevo: ")
            cedula = int(input("Ingrese la cedula del usuario nuevo: "))       
            menuUsuario = Usuario(nombre, apellido, correo, fechaN, cedula, contra)
            menuUsuario.registrar()
        case 2:
            menuUsuario.mostrar()
        case 3:
            menuUsuario.actualizar()
        case 4:
            menuUsuario.eliminar
        case 5:
            print("hasta luego esperamos verte pronto 👋")
            break