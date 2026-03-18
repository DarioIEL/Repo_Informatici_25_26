#Chiedi di inserire qualcosa
nome = input("Come ti chiami ?")
eta = int( input("Quanti anni hai ?") )

if eta <= 0 or eta > 120:
    print("Età non valida")
else:
    etaNuova = eta + 5
    print(f"Ciao{nome}, tra 5 anni avrai {etaNuova}")