try:
    numero= int(input("Inserisci un numero:"))
    print(f"Hai inserito:{numero}")
except ValueError:
    print("Errore: Devi inserire un numero!")