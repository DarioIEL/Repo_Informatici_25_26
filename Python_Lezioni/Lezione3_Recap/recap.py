nome = "Dario"
cognome = "Mennillo"
eta = 36
corso = "Tecnico Informatico"
altezza = 1.78
presenza = True

# Con queste variabili crea una "presentazione" di te stesso utilizzando il metodo print con una f-string all'interno

print(f"Mi presento: \nMi chiamo {nome} {cognome} e ho {eta} anni")
print(f"Studio nel corso di {corso}")
print(f"Altezza {altezza} m")

if presenza:
    print("Oggi sono presente")
else:
    print("Oggi sono assente")

print("====== IL MIO AMICO ========")
#Adesso presenta un tuo compagno/amico di classe. Fai attenzione ad assegnare delle variabili con un altro nome

nomeAmica = "Tina"
cognomeAmica = "Ponte"
etaAmica = 42
corsoAmica = "Tecnico informatico"
altezzaAmica = 1.70
presenzaAmica = False

print(f"Ciao, la mia amica è {nomeAmica} {cognomeAmica}. Lei è la responsabile del corso di {corsoAmica} e ha {etaAmica} anni")

if presenzaAmica:
    print(f"Anche {nomeAmica} è presente")
else:
    print(f"Oggi {nomeAmica} non è presente")

if etaAmica < 60:
    print(f"{nomeAmica} è ancora giovane")
else:
    print(f"{nomeAmica} non è più così giovane")