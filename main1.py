from cmath import sqrt


print("Programme Table de 7")
for i in range (1,11):
    print ("1x",i," = ", i*7)
print("---------------------")
# Calcul du périmetre 
print("Programme calcul du perimetre")
print("le perimetre d'un rectangle de 41 cm par 23 cm est", (2*41)+(2*23),)
print("---------------------")
print("Programme Hypotenuse")
a = 17
b = 12
hypo = sqrt((a*a)+(b*b))
print("Hypotenuse =", hypo,)
print("---------------------")
print("Programme identite")
prenom = input("quel est ton prenom ?")
nom = input("quel est ton prenom ?")
print ("Nom : "+ nom)
print ("Prenom : "+ prenom)
print (nom + " " + prenom)
print("---------------------")