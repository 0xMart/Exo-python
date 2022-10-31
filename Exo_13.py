start=str(input("Bienvenu dans le jeu du juste prix ! (OK POUR COMMENCER LA PARTIE): "))
while start != "ok":
    start=str(input("Bienvenu dans le jeu du juste prix ! (OK POUR COMMENCER LA PARTIE): "))        
import random  
number=random.randint (0,100)
number1 = int(input("Devinez un nombre : "))
while number != number1:
    if number < number1:
        print("Moins ")
        number1 = int(input("Devinez un nombre : "))
    elif number > number1:
        print("Plus")
        number1 = int(input("Devinez un nombre : "))
else:
    print("let's go t fort frero")