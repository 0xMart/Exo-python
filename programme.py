## Text menu in Python
      
def print_menu():       ## Your menu design here
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. –f pour spécifier un fichier")
    print ("2. –c pour créer le fichier")
    print ("3. –r pour renommer")
    print ("4. –l pour afficher son contenu")
    print ("5. -e Exit")
    print (67 * "-")
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("entrer votre choix")
     
    if choice=="f":     
        print ("spécifier un fichier")
        ## You can add your code or functions here
    elif choice=="c":
        print ("crée un fichier")
        ## You can add your code or functions here
    elif choice=="r":
        print ("pour renommer un fichier")
        ## You can add your code or functions here
    elif choice=="l":
        print ("afficher le contenu d'un fichier")
        ## You can add your code or functions here
    elif choice=="e":
        print ("Exit")
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Mauvaise selection.")