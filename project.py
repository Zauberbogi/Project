import random
nev=input("Nevezd el a botot:")
while True:
    te=input("írj valamit: ")

    if ("Szia" in te) or ("szia" in te) or ("Heló" in te) or ("heló" in te) or ("Helo" in te)or ("helo" in te):
        valasz=("Szia!","Helo!")
        print(random.choice(valasz))

    elif ("Szereted" in te) or ("szereted" in te) or ("Szeretnéd" in te) or ("szeretnéd" in te):
        valasz=("Igen!","Nem","Nem tudom")
        print(random.choice(valasz))

    elif ("Neved" in te) or ("neved" in te) or ("Hívnak" in te) or ("hívnak" in te):
        valasz=("Anyád :)",nev,"Nem tudom")
        print(random.choice(valasz))

    elif ("Éves" in te) or ("éves" in te) or ("Idős" in te) or ("idős" in te):
        valasz=("69","Most születtem","420")
        print(random.choice(valasz))

    elif ("Filmet" in te) or ("Film" in te) or ("film" in te) or ("filmet" in te)or("filmed" in te)or("Filmed" in te):
        valasz=("Anyád! <3 ","Nincs","Terminátor")
        print(random.choice(valasz))

    elif ("Szupererő" in te) or ("Szupererő" in te) or ("szupererőd" in te) or ("Szupererőd" in te):
        valasz=("Anyád! <3 ","Repülés","Telekinézis","Láthatatlanság")
        print(random.choice(valasz))

    elif ("Segítséget" in te) or ("segítséget" in te) or ("Tanácsot" in te) or ("tanácsot" in te)or("Segíteni" in te)or("segíteni" in te):
            valasz=("Anyád! <3 ","Nem","Miben?")
            print(random.choice(valasz))
            if valasz=="Miben?":
                kerdes=input=("")
        
    elif ("Származol" in te) or ("származol" in te):
        valasz=("Anyád! <3 ","A fejedből ;)","Sehonnan")
        print(random.choice(valasz))

    elif ("Hogy vagy" in te) or ("Hogy érzed magad" in te)or("hogy érzed magad" in te)or("hogy vagy" in te):
            valasz=("Anyád! <3 ","Csodálatosan, te?","Xarul, te?")
            print(random.choice(valasz))

    elif ("Nyelv" in te) or ("nyelv" in te)or("Nyelven" in te)or("nyelven" in te):
            valasz=("Хьау","Nee","Indi","Jo","Ĵok")
            print(random.choice(valasz))

    elif ("Viszlát" in te) or ("viszlát" in te):
                valasz=("Szia!","Viszlát!","További csodálatosan szép napot kívánok!")
                print(random.choice(valasz))

    elif te=="vége":
        break
