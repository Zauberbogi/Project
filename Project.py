import random

while 1==1:
    te=input("írj valamit: ")

    if ("Szia")or("Heló")or("Helo") in te:
        valasz=("Szia!","Helo!")
        print(random.choice(valasz))

    elif ("Szereted")or("Szeretnéd") in te:
        valasz=("Igen!","Nem","Nemtudom")
        print(random.choice(valasz))


