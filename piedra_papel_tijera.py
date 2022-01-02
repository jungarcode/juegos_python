import random

def jugar():
    
    opcion_usuario = input("Escoja su opcion 'pi' para piedra, 'pa' para papel, y 'ti' para tijera.\n").lower()
    
    opcion_computadora = random.choice(['pi','pa','ti'])
    
    
    if opcion_usuario == opcion_computadora:
        print(opcion_computadora)
        return 'Empate¡¡¡¡'
        
    
    if gano_jugador(opcion_usuario,opcion_computadora):
        
        return 'Ganaste¡¡¡'
        
    print(opcion_computadora)
    return 'Perdiste¡¡'
    


def gano_jugador(jugador,oponente):
    
    # retorna True si gana el jugador
    
    #piedra gana a tijera (pi>ti)
    
    #tijera gana a papel (ti>pa)
    
    #papel gana a piedra (pa>pi)
    
    if ((jugador == 'pi' and oponente == 'ti')
        or(jugador == 'ti' and oponente == 'pa')
        or(jugador == 'pa' and oponente == 'pi')):
        
        return True
    
    else:
        
        return False
    
    
print(jugar())
