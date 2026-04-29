while (True):
    eleccion = int(input("Digite la eleccion \n (1) Registrar Usuarios \n (2) Listar usuarios \n (3) Registrar Contenido \n (4) Listar Contenido \n (5) Registrar los favoritos para un usuario \n (6) Listar los Favoritos de los usuarios \n (7) salir \n ingresa tu opcion: "))
    match eleccion:
        case 1:
            print("---------REGISTRAR A UN USUARIO---------")
            nombre = input("Ingrese el nombre del usuario nuevo: ")
            apellido = input("Ingrese el apellido del usuario nuevo: ")
            validarCorreo()
            fechaN = input("Ingrese la fecha de nacimiento del usuario nuevo: ")
            contra = input("Ingrese la contraseña del usuario nuevo: ")      
            menuUsuario = Usuario(nombre, apellido, correo, fechaN, contra)
            menuUsuario.registrar()
        case 2:
            menuUsuario.mostrar()
        # case 3:
            # menuPelicula.registrar()
        # case 4:
            # menuPelicula.mostrar()
        # case 5:
            # menuFavoritos.registrar()
        # case 6:
            # menufavoritos.mostrar()
        case 7:
            print("Adios administrador picha peque")   
            break
