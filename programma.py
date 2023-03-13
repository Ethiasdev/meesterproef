from functions import *
from lingowords import *
poging = 1

te_raden_woord = selecteer_woord(woordenlijst)
print(te_raden_woord)


beginletter = pak_beginletter(te_raden_woord)
print(print_beginletter(beginletter))


while poging != 6:
    geraden_woord = vraag_om_gok(poging)
    
    if check_goed(geraden_woord, te_raden_woord):
        print(print_win_af())
        break
    
    feedback = geef_feedback(geraden_woord, te_raden_woord)
    print(feedback)

    poging += poging_checker(feedback)

    if check_verloren(poging):
        print(print_einde_af(te_raden_woord))
