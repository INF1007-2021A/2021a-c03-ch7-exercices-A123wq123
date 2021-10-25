#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import collections


# TODO: Définissez vos fonction ici
#exercice 1:
def masse_volume_ellipsoide(massevolumique, a, b, c):
    return ((4/3)*math.pi*a*b*c, massevolumique*(4/3)*math.pi*a*b*c)

#exercice 2:
def frequence(sentence: str) -> dict:
    letters = {letter: (sentence.lower()).count(letter) for letter in sentence.lower() if letter.isalpha()}

    letters_croissant = dict(sorted(letters.items(), key=lambda x: x[1], reverse=True))

    return letters_croissant



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
