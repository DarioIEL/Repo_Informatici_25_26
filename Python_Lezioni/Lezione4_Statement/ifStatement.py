# IF STATEMENT. Questo costrutto serve a controllare e prendere una scelta
# Operatori di confronto
# == (uguale a )
# != (diverso da)
# > (maggiore)
# < (minore)
# >= (maggiore uguale)
# <= (minore uguale)

#Tutte le volte che uso un operatore di confronto sto generando un valore booleano

#I valori boolean mi servono proprio negli if statement

#SINTASSI:
# if condizione:
#      corpo dell'if che viene eseguito se la condizione è true
# else:
#       corpo dell'else che viene eseguito se tutte le  condizioni precedenti sono false

# Esempio 1
piove = False

if piove:
    print("Porto l'ombrello")
else:
    print("Non porto l'ombrello")

# Esempio 2
miaEta = 5

if miaEta >= 18:
    print(f"Io ho {miaEta} anni e quindi sono maggiorenne")
elif miaEta < 0:
    print(f"Mi dispiace ma {miaEta} anni è un'età non valida")
else: 
    print(f"Io ho {miaEta} anni quindi sono minorenne")

# Esempio 3

etaLorenzo = 18
etaSanna = 18

if etaLorenzo > etaSanna:
    print(f"Lorenzo ha {etaLorenzo} anni ed è più grande di Sanna che ha {etaSanna} anni")
elif etaLorenzo < etaSanna:
    print(f"Sanna è più grande di Lorenzo")
else:
    print(f"Sanna e Lorenzo sono coetanei e hanno {etaLorenzo} anni")


#Esempio 4 - Confronto tra stringhe
parola1 = "ciao"
parola2 = "ciao"
parola3 = "Ciao"

if parola1 == parola3:
    print("Le due parole sono uguali")
elif parola1 != parola3:
    print("Le due parole sono diverse")
else:
    print("Non mi hai fornito due parole")

#Esempio 5 - Confronto tra stringhe senza tenere conto dell'uppercase o lowercase

stringa1 = "Caffè"
stringa2 = "caffè"

if stringa1.lower() == stringa2.lower():
    print(f"Le due stringhe sono uguali: {stringa1}")
else:
    print(f"Le due stringhe sono diverse: {stringa1} e {stringa2}")

#Esempio 6 - Altri confronti tra stringhe
#Possiamo confrontare porzioni di stringhe

frase = "Ciao Dario, come stai ?"

print(frase.startswith("Cia")) #True
print(frase.endswith("?")) #True
print("Dario" in frase) #True

if "Dario" in frase:
    print("La stringa Dario si trova nella frase")
else:
    print("La parola Dario non si trova nella frase")

if frase.startswith("Cia"):
    print("La frase comincia con Cia")
else:
    print("La frase non comincia con Cia")


# Esempio 7 - Voto e valutazione
# Patente di guida. Per iscrivermi all'esame devo aver compiuto 18 anni
# Utilizzo il metodo input per recuperare unvalore dal terminale

etaStudente = int( input("Quanti anni hai ? ") ) #ATT all'età perché tutto quello che recupero da un input tastiera è considerato una stringa

nomeStudente = input("Come ti chiami ? " ) 

if etaStudente >= 18 and etaStudente < 80:
    print(f"Benvenuto {nomeStudente}, puoi iscriverti all'esame di scuola guida")
elif etaStudente < 18 and etaStudente >= 15:
    print(f"Benvenuto {nomeStudente}, con la tua età puoi solo accedere all'esame per la patente AM")
else:
    print(f"Benvenuto {nomeStudente}, con la tua età non puoi ancora iscriverti a nessuna scuola guida")

