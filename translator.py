#!/usr/bin/python3
unite =  ['', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf', 'dix',
                'onze', 'douze', 'treize', 'quatorze', 'quinze', 'seize', 'dix-sept', 'dix-huit', 'dix-neuf']

dizaine = [None, None, 'vingt', 'trente', 'quarante', 'cinquante', 'soixante', 'soixante-dix', 'quatre-vingt', 'quatre-vingt-dix']


def prints(arg): print(" ".join(arg.split()))

#Fonction qui traduit les nombres de 1 à 19 de la liste unite en lettres
def func_unite(arg): return unite[int(arg)]

#Fonction qui traduit les nombres de 2 chiffres supérieur à 19 en lettres
def func_dizaine(arg):
    #Pour dire 01=1=un,02=2=deux..........09=9=neuf
    if int(arg[0]) == 0: return func_unite(arg[1])

    if int(arg) < 20: return unite[int(arg)]
    else:
        if int(arg[1]) == 0: return dizaine[int(arg[0])]
        else:
        #Pour les chiffres du dizaines  qui ont comme chiffre  du dizaine 7 ou 9 la syntaxe est un peu différent (ex:70=soixante dix )
            if int(arg[0]) == 7 or int(arg[0]) == 9:
                unit_new = int(arg) - int(arg[0]+'0') + 10
                return dizaine[int(arg[0]) - 1] + ' ' + unite[unit_new]
            else: return dizaine[int(arg[0])] + ' ' + unite[int(arg[1])]

#Fonction qui traduit les nombres de 3 chiffres  en lettres
def func_centaine(arg):
    #Pour dire 001=1=un,002=2=deux..........009=9=neuf....099=99=.....
    if int(arg[0]) == 0: return main(arg[1:])

    if int(arg[0]) == 1: return 'cent ' + func_dizaine(arg[1:])
    else: return unite[int(arg[0])] + ' cents ' + func_dizaine(arg[1:])

#Fonction qui traduit les nombres de 4,5,6 chiffres (milles)  en lettres
def func_millieme(arg):
    #Pour dire 001=1=un,002=2=deux..........009=9=neuf....099=99=uatre-vingt dix-neuf.....0999=999=.....
    if int(arg[0]) == 0: return main((arg[1:]))

    #Pour les nombres à 4 chiffres:1000-9999 
    if len(arg) == 4:
        if int(arg[0]) == 0: return func_centaine(arg[1:])

        if int(arg[0]) == 1:  return 'mille ' + func_centaine(arg[1:])
        else: return unite[int(arg[0])] + ' milles ' + func_centaine(arg[1:])    

    #Pour les nombres à 5 chiffres:10 000--99 999        
    elif len(arg) == 5: return func_dizaine(arg[:2]) + ' milles ' + func_centaine(arg[2:])

    #Pour les nombres à 6 chiffres:100 000--999 999       
    elif len(arg) == 6: return func_centaine(arg[:3]) + ' milles ' + func_centaine(arg[3:])
    
#Fonction qui traduit les nombres de 7,8,9 chiffres(millions)  en lettres
def func_million(arg):
    #Pour dire 0000001=1=un,0000002=2=deux..........0000009=9=neuf.........0999999=999999=.....
    if int(arg[0]) == 0: return main(arg[1:])

    #Pour les nombres à 7 chiffres:1 000 000--9 999 999
    if len(arg) == 7:
        #1 000 000:On prononce le 1 de million
        if int(arg[0]) == 1: return 'un million ' + func_millieme(arg[1:])
        else: return unite[int(arg[0])] + ' millions ' + func_millieme(arg[1:])

    #Pour les nombres à 8 chiffres:10 000 000--99 999 999
    elif len(arg) == 8:  return func_dizaine(arg[:2]) + ' millions ' + func_millieme(arg[2:])

    #Pour les nombres à 9 chiffres:1 000 000--9 999 999
    elif len(arg) == 9: return func_centaine(arg[:3]) + ' millions ' + func_millieme(arg[3:])

#Fonction qui traduit les nombres de plus de 10 chiffres  en lettres
def func_milliard(arg):
    if int(arg[0]) == 0: return main(arg[1:])
    #Pour les nombres à 10 chiffres:1 000 000 000--9 999 999 999
    if len(arg) == 10:
        if int(arg[0]) == 1: return 'un milliard' + func_million(arg[1:])
        else: return unite[int(arg[0])] + ' milliards ' + func_million(arg[1:])

    #Pour les nombres à 11 chiffres:10 000 000 000--99 999 999 999
    elif len(arg) == 11: return func_dizaine(arg[:2]) + ' milliards ' + func_million(arg[2:])

    ##Pour les nombres à 12 chiffres:100 000 000 000--9 999 999 999
    elif len(arg) == 12: return func_centaine(arg[:3]) + ' milliards ' + func_million(arg[3:])
        
    ##Pour les nombres à plus de 12 chiffres, cela devient recursive et en boucle avec les autres fonctions ci-dessous
    else: return main(arg[:len(arg)-9]) + ' milliards ' + func_million(arg[len(arg)-9:])

#Fonction qui traduit la paramètre arg en lettres suivant son nombre de chiffres
def main(arg):
    
    arg = str(int(arg))
    
    if len(arg) == 1: return func_unite(arg)

    elif len(arg) == 2: return func_dizaine(arg)

    elif len(arg) == 3: return func_centaine(arg)

    elif len(arg) in [4, 5, 6]: return func_millieme(arg)

    elif len(arg) in [7, 8, 9]: return func_million(arg)

    elif len(arg) > 9 : return func_milliard(arg)
