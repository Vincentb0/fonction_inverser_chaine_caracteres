"""
Fonction qui permet d'inverser l'ordre des caractères d'une
chaîne quelconque passé en paramètre.
"""

def inverse(chaine):
    longueur_chaine = len(chaine)
    i = longueur_chaine - 1  # pour commencer à la fin de la chaîne
    while i >= 0:
        chaine_inverser = chaine[i]
        print(chaine_inverser, end="")
        i -= 1


inverse("vincent")

"""
Le programme renvoi : tnecniv
"""


# ****** AUTRE METHODE ******


def inverse(chaine):
    ch = chaine[::-1]
    return ch

print(inverse("elena"))

"""
La fonction renvoi : anele
"""