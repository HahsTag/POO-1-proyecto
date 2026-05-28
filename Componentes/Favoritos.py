from Componentes.Usuario import Usuario
import pandas as pd

class Favoritos(Usuario):

    lista_favoritos = {}

    def __init__(self, id_usuario, datos_contenido):
        self.id_usuario = id_usuario
        self.datos_contenido = datos_contenido
        

    def registrar(self, id):
        
        self.lista_favoritos[f"favorito {id} Usuario: {self.id_usuario}"] = self.datos_contenido
        print(f"'{self.datos_contenido['titulo']}' ha sido añadido a tus favoritos con éxito.")
        id += 1
        return True
    
    def mostrar(self):
        if self.lista_favoritos:

            df_favoritos = pd.DataFrame(self.lista_favoritos).T

            df_favoritos.fillna("No Aplica", inplace=True)

            pd.set_option("display.width", 180)
            pd.set_option("display.max_columns", None)

            print("\n======= USUARIOS FUTIMEDIA =======\n")
            print(df_favoritos)
        else:
            print("No se han registrado favoritos de usuarios")