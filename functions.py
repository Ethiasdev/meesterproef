import random

def selecteer_woord(woordenlijst):
    
    return random.choice(woordenlijst)

def geef_feedback(geraden_woord, te_raden_woord):
    
    feedback = ""
    
    for i, letter in enumerate(geraden_woord):
        if letter == te_raden_woord[i]:
            feedback += "\033[32m{}\033[0m".format(letter) # groen
        elif letter in te_raden_woord:
            feedback += "\033[33m{}\033[0m".format(letter) # geel
        else:
            feedback += "-"
    
    return feedback
