eleccionMenu = 0
while eleccionMenu != 3:
    eleccionMenu = int(input("Elija si desea \n (1) Ingresar a la base de datos de los usuarios \n (2) Ingresar a la base de datos del reproductor \n (3) salir \n Elija: "))
    match eleccionMenu:
        case 1:
            #parte del codigo el cual manda al usuario al menu de los usuarios
            print("Esta seccion esta actualmente en Mantenimiento")
        case 2:
            eleccionMenuP = int(input("Elija si desea \n (1) Ingresar a la base datos de las peliculas \n (2) Ingresar a la base datos de los usuarios que ven las peliculas \n Elija: "))
        case 3: 
            print("Hasta luego!!! Esperamos verte pronto")
            eleccionMenu = 3

    
