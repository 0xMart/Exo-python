chaine = input("entrer votre mot ?")

repl = chaine[0] + chaine[1:].replace(chaine[0],"*")

print (str(repl))
