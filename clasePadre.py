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
            idE = int(input("Digite la cedula del usuario que desea eliminar: "))
            for clave in list(self.vector.keys()):
                if clave == idE:
                    del self.vector[clave]
    

    
