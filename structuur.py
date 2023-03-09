#functions

def selecteer_woord(woordenlijst):
    pass

def geef_feedback(geraden_woord, te_raden_woord):
    pass

#programma:

te_raden_woord = selecteer_woord(woordenlijst)

geraden_woord = input("Raad het woord: ").lower()

if geraden_woord == te_raden_woord:
    print("Gefeliciteerd, je hebt het woord geraden!")

feedback = geef_feedback(geraden_woord, te_raden_woord)
print(feedback)

poging = 0
if poging == 5:
    pass