import random

def selecteer_woord(woordenlijst):
    
    return random.choice(woordenlijst)

def geef_feedback(geraden_woord, te_raden_woord):
    geraden_woord = list(geraden_woord)
    feedback = ""
    letters = {}  # dictionary om het aantal exemplaren van elke letter in het te raden woord bij te houden
    
    # tel het aantal exemplaren van elke letter in het te raden woord
    for letter in te_raden_woord:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    
    # verwerk de geraden letters
    for i, letter in enumerate(geraden_woord):
        if letter == te_raden_woord[i]:
            feedback += "\033[32m{}\033[0m".format(letter) # groen
            letters[letter] -= 1
        elif letter in letters and letters[letter] > 0:
            feedback += "\033[33m{}\033[0m".format(letter) # geel
            letters[letter] -= 1
        else:
            feedback += "-"
    
    return feedback



