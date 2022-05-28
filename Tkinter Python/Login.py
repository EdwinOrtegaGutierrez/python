#archivo para imprimir contrasenas con asteriscos
 
# Importacion de Librerias
import getpass
 
#declaracion de variables
registeredUser = ['KathyDally','KimCol','GuestUser']
registeredPW = ['code2016']

def login(usuario, passw):
    if usuario in registeredUser:
        if passw in registeredPW:
            return 1
        else:
            print("\nYour password does not match...\n")
            return 2
    else:
        print('ERROR! User is not registered.')
        return 3

def Main():
    #inicializacion de procesos
    usuario = input('User: ')
    passw = getpass.getpass('Password: ')

    if login(usuario, passw) == 1:
        print('Welcome ', usuario)

    return Main()

Main()