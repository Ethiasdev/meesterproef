import random

def selecteer_woord(woordenlijst):
    
    return random.choice(woordenlijst)

def pak_beginletter(geselecteerd):
    beginletter = geselecteerd[0]
    return beginletter

def geef_feedback(geraden_woord, te_raden_woord):
    if len(geraden_woord) != 5:
        return "Het geraden woord moet uit precies 5 letters bestaan. Probeer opnieuw."
        
    geraden_woord = list(geraden_woord)
    feedback = ""
    letters = {}  
    

    for letter in te_raden_woord:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    

    for i, letter in enumerate(geraden_woord):
        if letter == te_raden_woord[i]:
            feedback += "\033[32m{}\033[0m".format(letter) 
            letters[letter] -= 1
        elif letter in letters and letters[letter] > 0:
            feedback += "\033[33m{}\033[0m".format(letter) 
            letters[letter] -= 1
        else:
            feedback += "-"
    
    return feedback


def vraag_om_gok(poging):
    print(f"\nPoging {poging}:")
    geraden_woord = input("Raad het woord: ").lower()
    return geraden_woord

def check_verloren(poging):
    if poging == 5:
        return True

def check_goed(geraden_woord, te_raden_woord):
    if geraden_woord == te_raden_woord:
        return True

def print_einde_af(te_raden_woord):
    return f"\nHelaas, het woord was '{te_raden_woord}'. Volgende keer beter!"

def print_win_af():
    return "Gefeliciteerd, je hebt het woord geraden!"

def print_beginletter(beginletter):
    return f"Het te raden woord begint met een '{beginletter}'."

def poging_checker(feedback, poging):
    if feedback == "Het geraden woord moet uit precies 5 letters bestaan. Probeer opnieuw.":
        return 0
    else:
        return 1

    




