class Rockhola():
    #Constructor de la Clase
    def __init__(self,marca,genero):
        self.marca = marca
        self.genero = genero
    #Metodos de funcionamiento de la Rockola
    def playMusic(self,cancion):
        print(f"Reproduciendo Cancion {cancion}")
    def stopMusic(self):
        print("Pausa")
    def nextSong(self,cancion):
        print(f"Mostrando {cancion}...")
    def previousSong(self,cancion):
        print(f"Mostrando {cancion}...")