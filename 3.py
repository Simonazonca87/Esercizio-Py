print ("Benvenuto al Ristorante Magico!")
# Chiediamo i dati ell'utente
nome = input ("Come ti chami? ")
num_piatti = int(input ("Quanti piatti hai ordinato "))
costo_medio = float (input("Quanto costa mediamente un piatto? "))
servizio =(input("Il servizio è stato buono? (si/no): ")).strip().lower()
 # Calcoliamo il totale del conto totale = num_piatti * costo_medio
totale =num_piatti * costo_medio   
# Determiniamo la mancia
if servizio == "si":
    mancia = totale * 0.15
    print("Grazie per il tuo feecback positivo!")
else:
    mancia = totale * 0.05
    print("Ci dispaice che il servizio non sia stato all'altezza.")
  # Calcoliamo il totale da pagare
totale_finale = totale + mancia
  #Stampiamo il riepilogo
print("\n **Riepilogo del tuo conto**")
print(f"Nome cliente:{nome}")
print(f"Totale cibo: {totale:.2f}€")
print(f"Mancia aggiunta: {mancia:.2f}€")
print(f"Totale da pagare: {totale_finale:.2f}€")
print("\nGrazie per aver scelto il Ristorante Magico!")