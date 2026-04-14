import pandas as pd
listaUsuarios = {}

class Usuario:

    def __init__(self, nombre, apellido, correo, fechaN, cedula, contra, isCeV = False):

        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fechaN = fechaN
        self.cedula = cedula
        self.contra = contra
        self.isCeV = isCeV
        

    def registroUsuario(self):

        for clave in listaUsuarios.keys():
            if clave == self.cedula:
                print("Ese numero de cedula ya existe")
                self.isCeV == True
                return

        listaUsuarios[self.cedula] = {
        "nombre": self.nombre,
        "apellido": self.apellido,
        "correo": self.correo,
        "fecha": self.fechaN,
        "contraseña": self.contra
        } 
        print("El usuario a sido registrado")  
    
    def verUsuarios(self):
        if listaUsuarios:
            df_usuarios = pd.DataFrame(listaUsuarios)
            df_usuarios = df_usuarios.T
            print(df_usuarios)
        else:
            print("No se han registrado usuarios")           

    def actUsuario(self):
            cedulaE = int(input("Digite la cedula del usuario al cual desea modificar la informacion: "))
            k = 0
            for clave in listaUsuarios.keys():
                if clave == cedulaE:
                    eleccionUp = int(input("Que informacion desea modificar: \n (1) Nombre/s \n (2) Correo \n (3) Todas las anteriores \n (4) ir atras \n Elija: "))
                    match eleccionUp:
                            case 1:
                                listaUsuarios[clave]["nombre"] = input("Ingrese el nombre nuevo para el usuario: ")
                                listaUsuarios[clave]["apellido"] = input("Ingrese el apellido nuevo para el usuario: ")
                            case 2:
                                correoNuevo = input("Ingrese el correo nuevo para el usuario: ")

                                for arrova in correoNuevo:
                                    if arrova == " ":
                                        print("Recuerde que el correo electronico no puede tener espacios!!!")
                                        return
                                    
                                    elif arrova == "@":
                                        listaUsuarios[clave]["correo"] = correoNuevo

                                    else:
                                        k += 1

                                if len(correoNuevo) == k:
                                    print("Recuerde que el correo electronico debe tener un arrova")
                                    return

                            case 3:
                                listaUsuarios[clave]["nombre"] = input("Ingrese el nombre nuevo para el usuario: ")
                                listaUsuarios[clave]["apellido"] = input("Ingrese el apellido nuevo para el usuario: ")
                                correoNuevo = input("Ingrese el correo nuevo para el usuario: ")

                                for arrova in correoNuevo:
                                    if arrova == " ":
                                        print("Recuerde que el correo electronico no puede tener espacios!!!")
                                        return
                                    
                                    elif arrova == "@":
                                        listaUsuarios[clave]["correo"] = correoNuevo

                                    else:
                                        k += 1

                                if len(correoNuevo) == k:
                                    print("Recuerde que el correo electronico debe tener un arrova")
                                    return

                            case 4:
                                break
                                
    def borrarUsuario(self):
            cedulaE = int(input("Digite la cedula del usuario que desea eliminar: "))
            for clave in list(listaUsuarios.keys()):
                if clave == cedulaE:
                    print(f"Se a eliminado a el usuario con \n nombre: {listaUsuarios[clave]["nombre"]} {listaUsuarios[clave]["apellido"]} \n correo: {listaUsuarios[clave]["correo"]} \n Fecha: {listaUsuarios[clave]["fecha"]} \n Contraseña: {listaUsuarios[clave]["contraseña"]}")
                    del listaUsuarios[clave]

eleccion = 0
def validarCorreo():
    
    global correo
    i = 0
    k = 0 
    while i != 1:
        correo = input("Ingrese el correo del usuario nuevo: ")
        for arrova in correo:
                        if arrova == " ":
                            break
                        elif arrova == "@":
                            correo = correo
                        else: 
                            k += 1
                             
        if k == len(correo):
            print("Recuerde que el correo NO permite caracteres especiales y debe tener contener un arrova")
        else:
            i = 1
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
            usu1 = Usuario(nombre, apellido, correo, fechaN, cedula, contra)
            usu1.registroUsuario()

        case 2: 
            usu1.verUsuarios()
        case 3:  
            if len(nombre) == 0:
                print("No se han registrado usuarios")
            else:       
                usu1.actUsuario()
        case 4:
            if len(nombre) == 0:
                print("No se han registrado usuarios")
            else: 
                usu1.borrarUsuario()
        case 5:
            print("Hasta luego esperamos verte de nuevo :)")
            eleccion = 5

        
        