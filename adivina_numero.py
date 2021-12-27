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
adivina_numero(10)