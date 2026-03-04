# Questo è un commento
# Cos'è una variabile ? E' un contenitore che memorizza un valore. Questo valore può cambiare (arbitrariamente) durante l'esecuzione del codice

#Assegno una variabile
nome = "Dario" #String
eta = 36       #Intero
corso = "tecnico informatico" #String
altezza = 1.78 # Float (numero con la virgola)

#indipendentemente dal tipo che scelgo non viene dichiarato da nessuna parte. questo comportamento è tipico dei linguaggi debolmente tipizzati

# ESERCIZIO: Istanzia 2 variabili (nome a tua scelta) di tipo intero. Con queste 2 variabili elabora le 4 operazioni matematiche (+ - * /). Stampa in console con un print i risultati
num1 = 4
num2 = 15

somma = num1 + num2
prod = num1 * num2
diff = num1 - num2
quoz = round(num1 / num2 , 2)

print("La somma vale", somma)
print("Il prodotto vale", prod)
print("La differenza vale", diff)
print("Il quoziente vale", quoz)

#NUMERI CON LA VIRGOLA o FLOAT
pi = 3.14159
temperatura = 21.5

#voglio controllare di che tipo sono pi e temperatura
print(type(pi))
print(type(temperatura))

calcolo = 0.1 + 0.2 
print(calcolo) #0.3000000000004 Attenti alla precisione
print(round(calcolo, 2)) #round(numero, precisione) questo metodo arrotonda

#STRINGHE : sono sequenze immutabili di caratteri. Le stringhe sono il modo umano di comunicare

nomeUser = "Anna99"
emailUser = "anna@mail.com"
etaUser = 25
corsoUser = "Tecnico Informatico"

#Concatenazione tra stringhe

print(nomeUser + " - " + emailUser) #Posso utilizzare il simbolo + per concatenare solo stringhe. Se tra queste variabili c'è un numero non posso più utilizzare il simbolo +

print(nomeUser, "-", emailUser, "eta:", etaUser, "anni") #Visto che etaUser è un numero utilizzo la , per concatenare le stringhe

#f-string è il modo moderno di formattare le stringhe
#la stringa comincia con la f all'esterno delle "" e richiamo attraverso le {} il nome delle variabili. Anche in questo caso posso miscelare le variabili
print(f"{nomeUser} - email: {emailUser} - età: {etaUser}")

#ESERCIZIO: presenta te stesso: mioNome, mioCognome, miaEta, mioCorso. Stampa tutte le info utilizzando il metodo fstring (5 minuti)