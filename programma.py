from functions import *
from lingowords import *





te_raden_woord = selecteer_woord(woordenlijst)


beginletter = te_raden_woord[0]
print(f"Het te raden woord begint met een '{beginletter}'.")


for poging in range(1, 6):
    print(f"\nPoging {poging}:")
    geraden_woord = input("Raad het woord: ").lower()
    
    if geraden_woord == te_raden_woord:
        print("Gefeliciteerd, je hebt het woord geraden!")
        break
    
    feedback = geef_feedback(geraden_woord, te_raden_woord)
    print(feedback)
    
    if poging == 5:
        print(f"\nHelaas, het woord was '{te_raden_woord}'. Volgende keer beter!")
