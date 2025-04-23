import random
def juego_adivinanza():
    numero_secreto = random.randint(1,100)
    intentos = 0
    adivinado = False
    
    print("¡Bienvenido al juego de adivinanza de numeros!")
    print("Estoy pensando en un numero entre 1 y 100.")
    
    while not adivinado:
        experimento = int(input("Adivina el numero:"))
        intentos += 1
        
        
        if experimento < numero_secreto:
            print("El numero es mayor.")
        elif experimento > numero_secreto:
            print("El numero es menor.")
            
        else:
            adivinado = True
            print("Felicidades Adivinaste el numero en {intentos} intentos.")
            
juego_adivinanza()