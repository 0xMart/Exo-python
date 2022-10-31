
from random import randrange
import random, string

#Alphanumérique aléatoire
randomalpha = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
print("Chaîne alphanumérique aléatoire :", randomalpha)

# Random valeur entre 0 et 50
randomentier = random.randint(0, 50)
print ("Valeur aléatoire entre deux entiers : ",randomentier)

mutiple = randrange (7,70 ,7)

print ("multiple de 7 :",mutiple)

