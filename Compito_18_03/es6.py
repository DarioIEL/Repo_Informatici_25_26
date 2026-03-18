parola = input("Inserisci una parola...")

lunghParola = len(parola)

if lunghParola >= 5 and lunghParola <= 8:
    print("Parola Media lunghezza")
elif lunghParola < 5:
    print("Parola Corta")
else:
    print("Parola Lunga")