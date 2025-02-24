saldo = 500 # Saldo iniziale
prelievo = float (input ("Quanto vuoi prelevare? "))
if prelievo > saldo:
    print("Saldo insufficiente!")
else:
    saldo -= prelievo
    print(f" Prelievo effettuato! Nuovo saldo: {saldo:.2f}€")
    