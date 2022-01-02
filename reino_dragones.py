import random
import time


def intro():
    print('Estás en una tierra llena de dragones. Frente a tí')
    print('hay dos cuevas. En una de ellas, el dragón es generoso y')
    print('amigable y compartirá su tesoro contigo. El otro dragón')
    print('es codicioso y está hambriento, y te devorará inmediatamente.')
    print()
    
def elegir_cueva():

    cueva = ''

    while cueva != '1' and cueva != '2':
    
        cueva = input("!! Aque cueva quieres ingresar 1 o 2?? : \n")
    

    return cueva

def explorar_cueva(seleccionCueva):

    print('Te aproximas a la cueva...')
    
    time.sleep(2)

    print('Es oscura y espeluznante...')

    time.sleep(2)

    print('¡Un gran dragon aparece súbitamente frente a tí! Abre sus fauces y...')

    print()

    time.sleep(2)


    cuevaAmigable = random.randint(1, 2)


    if seleccionCueva == str(cuevaAmigable):

        print('¡Te regala su tesoro!')

    else:

        print('¡Te come de un bocado!')

seguir_jugando = 'si'

while seguir_jugando == 'si' or seguir_jugando == 's':
        
    intro()
    numero_cueva = elegir_cueva()
    explorar_cueva(numero_cueva)
    
    seguir_jugando =input("! Quieres seguir jugando ?? Si o No: \n").lower()