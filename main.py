#### Imports et définition des variables globales
""" import """
import sys

#### Fonctions secondaires
sys.setrecursionlimit(1100)

def artcode_i(s):
    """
    iterative
    """

    # votre code ici

    occurrences = [1]
    caracteres = [s[0]]

    for i in range(1, len(s)):
        if s[i] == s[i-1] :
            occurrences[-1] += 1
        else :
            caracteres.append(s[i])
            occurrences.append(1)  # Ajouter un nouveau caractère et initialiser son compteur

    return list(zip(caracteres, occurrences))

def artcode_r(s):
    """
    recursive
    """

    # votre code ici
    if not s:  # Cas de base : chaîne vide
        return []
    if len(s) == 1:  # Cas de base
        return [(s[0], 1)]
    # Identifie les occurrences
    premier_char = s[0]
    compteur = 1
    while compteur < len(s) and s[compteur] == premier_char:
        compteur += 1

    # Construire le résultat en concaténant le tuple courant avec l'appel récursif
    return [(premier_char, compteur)] + artcode_r(s[compteur:])

#### Fonction principale


def main():
    """
    main test
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
