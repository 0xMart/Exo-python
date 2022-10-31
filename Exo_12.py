import random, string


taillepassword = 8
taillerandomdigit=2
taillerandommaj = 1
taillerandomponct = 1
password=""

while True :
    password=""
    randommaj = ''.join(random.choice(string.ascii_uppercase) for _ in range(1))
    password = password + randommaj
    randomdigit = ''.join(random.choice(string.digits) for _ in range(2))
    password = password + randomdigit
    randomponct = ''.join(random.choice(string.punctuation ) for _ in range(1))
    password = password + randomponct
    randomletter = ''.join(random.choice(string.ascii_lowercase) for _ in range(taillepassword - taillerandomdigit - taillerandommaj - taillerandomponct))
    password = password + randomletter
    print("")
    print("mot de passe ",password)
    input("tape sur enter pour continuer...\n")
    



