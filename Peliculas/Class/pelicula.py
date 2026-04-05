class Pelicula: 

    contadorId = 1 

    def __init__ (self, tituloPeli, autorPeli, descripcionPeli, anioPeli, generoPeli, favorito= False):
        self.idPeli = Pelicula.contadorId
        Pelicula.contadorId +=1
        
        self.tituloPeli = tituloPeli
        self.autorPeli = autorPeli
        self.descripcionPeli = descripcionPeli
        self.anioPeli = anioPeli
        self.generoPeli = generoPeli
        self.favorito = favorito