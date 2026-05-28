import pandas as pd
from datetime import datetime

class Usuario:
    contador = 1 #Contador id Usuario
    usuarios = {} #Vector/lista usuarios

    #Atributos
    def __init__(self, nombre, apellido, email, fecha):
        self.nombre = nombre.strip()
        self.apellido = apellido.strip() 
        self.email = email
        self.fecha = fecha
        self.id = Usuario.contador
        Usuario.contador += 1
        
    
    #Metodo de validacion
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

    
    #Metodos
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
    
    def registrar(self):
            
        self.usuarios[self.id] = {
        "nombre": self.nombre,
        "apellido": self.apellido,
        "correo": self.email,
        "fecha de nacimiento": self.fecha
        } 
        print("El usuario a sido registrado") 



def validarCorreo():

    #Convierte la variable propia de la funcion a publica ya que se usa en metodos de la clase
    global correo
    while True:
        correo = input("Ingrese el correo del usuario nuevo: ")

        #Verifica si el correo tiene espacios
        if " " in correo:
            print("Recuerde que el correo no puede tener espacios!!!")
            continue
        
        #Verifica si el correo tiene arrova 
        if correo.count("@") != 1:
            print("Recuerde que el correo debe tener exactamente un @")
            continue

        #Separamos el directorio, el nombre, y el arrova del correo para verificar si el punto existe en el correo    
        nombre, arrova, directorio = correo.partition("@")
        if directorio.count(".") != 1:
            print("Recuerde que el correo debe tener un directorio por ejemplo (.com)")
            continue
            
        return correo.strip()

