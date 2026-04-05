nombre = []
apellido = []
correo = []
fecha_nacimiento = []

class MenuUsuario:

    def ingresarNuevoUsuario(self):
        
        print("---------REGISTRAR A UN USUARIO---------")
        nombreU = input("Ingrese el nombre del usuario nuevo: ")
        apellidoU = input("Ingrese el apellido del usuario nuevo: ")
        correoU = input("Ingrese el correo del usuario nuevo: ")
        fecha_nacimientoU = input("Ingrese la fecha de naciemiento del usuario nuevo: ")

        usu1.usuarioNuevo(nombreU, apellidoU, correoU, fecha_nacimientoU)

        print("El usuario se a registrado exitosamente")


    def leerUsuarioExis(self):
        usu1.verUsuarios()

class InfUsuario:

    def usuarioNuevo(self, nombreP, apellidoP, correoP, fecha_nacimientoP):
        
        #password, nickname??
        nombre.append(nombreP)
        apellido.append(apellidoP)
        correo.append(correoP)
        fecha_nacimiento.append(fecha_nacimientoP)
    
    def verUsuarios(self):
        for i in range(len(nombre)):
            print(f"el usuario {i} \n nombre: {nombre[i]} {apellido[i]} \n fecha: {fecha_nacimiento[i]} \n ccorreo: {correo[i]}")

usu1 = InfUsuario()        

         


eleccion = 0
menu1 = MenuUsuario()

while eleccion != 5:
    eleccion = int(input("Digite la eleccion \n (1) Si desea Ingresar un usuario nuevo \n (2) Si desesa ver cuantos usuarios hay registrados \n (3) Si desea actualizar la informacion de un usuario ya existente \n (4) Si desea Borrar a un usuario \n (5) salir \n ingresa tu opcion: "))
    match eleccion:
        case 1:
            menu1.ingresarNuevoUsuario()
        case 2: 
           menu1.leerUsuarioExis()
        # case 3:
        #     print("")
        # case 4:
        #     print("")
        
        