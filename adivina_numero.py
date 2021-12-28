import random


def adivina_numero(num):
    
    print("=============================")
    
    print("comienza el juego!!")
    
    print("Tienes que adivinar el numero.")
    
    
    num_aleatorio = random.randint(1,num)
    
    prediccion = 0
    
    while prediccion != num_aleatorio:
        # se solicita al usuario el numero
        prediccion = int(input(f"Adivina un munero entre 1 y {num}: "))
        
        if prediccion < num_aleatorio:
            
            print("El numero es muy pequeño , intentalo de nuevo!!!")
        
        if prediccion > num_aleatorio:
            
            print("El numero es muy grande , intentalo de nuevo!!!")
            
    print(f"¡¡En hora buena!! Adivinaste el numero {num_aleatorio}")
    
# se hace llamada a la funcion con el numero superior a adivinar  
    
adivina_numero(5)
  
  
# Segunda Solucion sin funcion, se establece el maximo del numero aleatorio  

intentosRealizados = 0

print('¡Hola! ¿Cómo te llamas?')
miNombre = input()

número = random.randint(1, 20)
print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 20.')

while intentosRealizados < 6:
    print('Intenta adivinar.')
   
    estimación = int(input())
    intentosRealizados = intentosRealizados + 1
    if estimación < número:
        print('Tu estimación es muy baja.')
    

    if estimación > número:

        print('Tu estimación es muy alta.')

    if estimación == número:

        break

if estimación == número:

    intentosRealizados = str(intentosRealizados)

    print('¡Buen trabajo, ' + miNombre + '! ¡Has adivinado mi número en ' +
    intentosRealizados + ' intentos!')

if estimación != número:

    número = str(número)

    print('Pues no. El número que estaba pensando era ' + número)