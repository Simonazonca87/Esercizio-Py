def saluta():
    print("Ciao, benvuto nel cotso di Python!")

    saluta() # Output: Ciao, benvenuto nel corso di Python!

    def saluta(nome):
        print (f"Ciao {nome} , benvenuto nel corso di Python")

    saluta ("Simona") # Output: Ciao Marco, benvenuto nel corso di Python!
