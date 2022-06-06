from clases.rockhola import Rockhola
from clases.songs import Songs
from clases.albums import Album
from clases.artistas import Artista
from os import system
#Crear Objeto
def menu():
    opcionMenu = 0
    opcionRockhola = 0

    arrCanciones = ['La chona','Dos monedas','Tamarindo','El sinaloense','Quien te quiera','Terrenal','Salir']
    iExitMenu = 3
    iExitRock = 5
    miRockhola = Rockhola("Mexicana","Mix")
    while opcionMenu != iExitMenu:
        print("---------Menu---------")
        print("1.- Registrar Cancion")
        print("2.- Elimiar Cancion")
        print("3.- Mostrar Canciones")
        print("4.- Apagar Rockhola")
        print("--------------------------")

        opcionMenu = input("Seleccione una opcion: ")
        system("cls")
        if opcionMenu == '1':
            print("Espere...")
            sSong = input("Escriba el nombre de la cancion que desea registrar: ")
            arrCanciones.pop()
            arrCanciones.append(sSong)
            arrCanciones.append('Salir')
            system("cls")
        elif opcionMenu == '2':
            sSong = input("Escriba el nombre de la cancion que desea eliminar: ")
            arrCanciones.remove(sSong)
            system("cls")
        elif opcionMenu == '3':
            i = 1
            print("------Lista de Canciones-------")
            for cancion in arrCanciones:
                if cancion == "":
                    print("No hay canciones para Mostrar")
                else:
                    print(i,".- ",cancion)
                    i += 1

            iCancion = int(input("Seleccione Opcion: "))
            system("cls")
            if iCancion == len(arrCanciones):
                print("Volviendo al menu anterior...")
            else:
                sShowSong = arrCanciones[iCancion-1]
                while opcionRockhola != iExitRock:
                    opcionRockhola = subMenu1(miRockhola,sShowSong,arrCanciones,iCancion)
        elif opcionMenu == '4':
            exit()
        else:
            exit()

def subMenu1(miRockhola,sSong: str,arrCanciones,iCancion):
    opcion = 0
    opcionCancion = 0
    print("--------- ",sSong," ---------")
    print("1.- Reproducir Cancion")
    print("2.- Siguiente Cancion")
    print("3.- Cancion Anterior")
    print("4.- Apagar Rockhola")
    print("-----------------------------")
    opcion = input("Seleccione una opcion: ")
    system("cls")
    if opcion == '1':
        miRockhola.playMusic(sSong)
        while opcionCancion != 4:
            opcionCancion = subMenu2(miRockhola,sSong,arrCanciones,iCancion)
    elif opcion == '2':
        iCancion += 1
        if iCancion == len(arrCanciones):
            iCancion = 1
        sSong = arrCanciones[iCancion-1]
        miRockhola.nextSong(sSong)
        while opcionCancion != 4:
            opcionCancion = subMenu2(miRockhola,sSong,arrCanciones,iCancion)
    elif opcion == '3':
        iCancion -= 1
        if iCancion == 0:
            iCancion = len(arrCanciones)
        sSong = arrCanciones[iCancion-1]
        miRockhola.previousSong(sSong)
        while opcionCancion != 4:
            opcionCancion = subMenu2(miRockhola,sSong,arrCanciones,iCancion)
    elif opcion == '4':
        exit()
    return int(opcion)

def subMenu2(miRockhola,sSong: str,arrCanciones,iCancion):
    opcion = 0
    opcionCancion = 0
    print("--------- ",sSong," ---------")
    print("1.- Detener Cancion")
    print("2.- Siguiente Cancion")
    print("3.- Cancion Anterior")
    print("4.- Apagar Rockhola")
    print("-----------------------------")
    opcion = input("Seleccione una opcion: ")
    system("cls")
    if opcion == '1':
        miRockhola.stopMusic()
        while opcionCancion != 4:
            opcionCancion = subMenu1(miRockhola,sSong,arrCanciones,iCancion)
    elif opcion == '2':
        iCancion += 1
        if iCancion == len(arrCanciones):
            iCancion = 1
        sSong = arrCanciones[iCancion-1]
        miRockhola.nextSong(sSong)
        opcionCancion = subMenu2(miRockhola,sSong,arrCanciones,iCancion)
    elif opcion == '3':
        iCancion -= 1
        if iCancion == 0:
            iCancion = len(arrCanciones)
        sSong = arrCanciones[iCancion-1]
        miRockhola.previousSong(sSong)
        opcionCancion = subMenu2(miRockhola,sSong,arrCanciones,iCancion)
    elif opcion == '4':
        exit()
    return int(opcion)
try:
    menu()
except:
    print("Hubo un error inesperado")