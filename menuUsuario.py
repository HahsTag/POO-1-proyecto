nombre = []
apellido = []
correo = []
fecha_nacimiento = []
cedula = []
contra = []


class InfUsuario:
    def usuarioNuevo(self):
        print("---------REGISTRAR A UN USUARIO---------")

        nombreU = input("Ingrese el nombre del usuario nuevo: ")
        nombre.append(nombreU)

        apellidoU = input("Ingrese el apellido del usuario nuevo: ")
        apellido.append(apellidoU)
        
        #confirmar con @
        correoU = input("Ingrese el correo del usuario nuevo: ")
        correo.append(correoU)

        fecha_nacimientoU = input("Ingrese la fecha de naciemiento del usuario nuevo: ")
        fecha_nacimiento.append(fecha_nacimientoU)

        #verificar cedula existencia
        cedulaU = int(input("Ingrese la cedula del usuario nuevo: "))
        cedula.append(cedulaU)

        contraU = input("Digite la contraseña que va a tener esta cuenta de este usuario: ")
        contra.append(contraU)

    
    def verUsuarios(self):
        if len(nombre) == 0:
            print("No se han registrado usuarios")
        else: 
            for i in range(len(nombre)):
                print(f"el usuario {i} \n Nombre: {nombre[i]} {apellido[i]} \n Fecha: {fecha_nacimiento[i]} \n Correo: {correo[i]} \n Cedula: {cedula[i]}")


    def actUsuario(self):
            cedulaE = int(input("Digite la cedula del usuario al cual desea modificar la informacion: "))
            k = 0
            for i in cedula:
                if i == cedulaE:
                    eleccionUp = int(input("Que informacion desea modificar: \n (1) Nombre/s \n (2) Apellido/s \n (3) Correo \n (4) Ir atras \n Elija: "))
                    match eleccionUp:
                            case 1:
                                nombre[k] = input("Ingrese el nombre nuevo del usuario: ")
                            case 2:
                                apellido[k] = input("Ingrese el apellido nuevo del usuario: ")
                            case 3:
                                #confirmar con @
                                correo[k] = input("Ingrese el correo nuevo del usuario: ")
                            case 4:
                                break
                k =+ 1

    def borrarUsuario(self):
            
            cedulaE = int(input("Digite la cedula del usuario que desea eliminar: "))
            k = 0
            for i in cedula:
                if i == cedulaE:
                    print(f"Se a eliminado a el usuario con \n nombre: {nombre[k]} {apellido[k]} \n correo: {correo[k]} \n Fecha: {fecha_nacimiento[k]} \n Cedula: {cedula[k]} \n Contraseña: {contra[k]}")
                    del nombre[k]
                    del apellido[k]
                    del correo[k]
                    del fecha_nacimiento[k]
                    del cedula[k]
                k =+ 1



usu1 = InfUsuario()               


eleccion = 0


while eleccion != 5:
    eleccion = int(input("Digite la eleccion \n (1) Si desea Ingresar un usuario nuevo \n (2) Si desesa ver cuantos usuarios hay registrados \n (3) Si desea actualizar la informacion de un usuario ya existente \n (4) Si desea Borrar a un usuario \n (5) salir \n ingresa tu opcion: "))
    match eleccion:
        case 1:
            usu1.usuarioNuevo()
            print("El usuario se a registrado exitosamente")
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

        
        