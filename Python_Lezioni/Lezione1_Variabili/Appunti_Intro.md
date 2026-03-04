# Lezione Introduttiva a Python

**Corso di Programmazione**  
*Docente: Dario IEL*  
*Data: 4 Marzo 2026*

---

## Indice

1. Introduzione a Python
2. Installazione e Setup
3. Sintassi di Base
4. Variabili e Tipi di Dati
5. Operatori
6. Strutture di Controllo
7. Funzioni
8. Esercizi Pratici

---

## 1. Introduzione a Python

Python è un linguaggio di programmazione ad alto livello, interpretato e general-purpose. Creato da Guido van Rossum e rilasciato per la prima volta nel 1991, Python si distingue per la sua sintassi chiara e leggibile.

### Caratteristiche Principali

\begin{itemize}
\item \textbf{Sintassi semplice e leggibile}: il codice Python è facile da scrivere e comprendere
\item \textbf{Linguaggio interpretato}: non richiede compilazione
\item \textbf{Tipizzazione dinamica}: non è necessario dichiarare il tipo delle variabili
\item \textbf{Multiparadigma}: supporta programmazione procedurale, object-oriented e funzionale
\item \textbf{Ampia libreria standard}: ricco ecosistema di moduli e package
\end{itemize}

### Utilizzi Comuni

\begin{itemize}
\item Sviluppo web (Django, Flask)
\item Data Science e Machine Learning (pandas, NumPy, scikit-learn)
\item Automazione e scripting
\item Analisi dati e visualizzazione
\item Intelligenza Artificiale
\end{itemize}

---

## 2. Installazione e Setup

### Verificare l'installazione

Aprire il terminale (o command prompt su Windows) e digitare:

python --version

oppure

python3 --version

### Primo programma

Creare un file chiamato `hello.py`:

print("Ciao, benvenuto in Python!")

Eseguire il programma dal terminale:

python hello.py

**Output:**
Ciao, benvenuto in Python!

---

## 3. Sintassi di Base

Python utilizza l'**indentazione** (spazi o tab) per definire i blocchi di codice, non le parentesi graffe come altri linguaggi.

### Commenti

# Questo è un commento su singola riga

"""
Questo è un commento
su più righe
"""

'''
Anche questo è un commento
su più righe
'''

### Indentazione

# Corretto
if 5 > 2:
    print("Cinque è maggiore di due")

# Errato (genera IndentationError)
if 5 > 2:
print("Cinque è maggiore di due")

---

## 4. Variabili e Tipi di Dati

### Dichiarazione di Variabili

In Python non è necessario dichiarare esplicitamente il tipo di una variabile.

nome = "Mario"          # Stringa
eta = 25                # Intero
altezza = 1.75          # Float
studente = True         # Booleano

### Tipi di Dati Principali

#### 4.1 Numeri

# Interi
numero_intero = 42
negativo = -10

# Float
numero_decimale = 3.14
scientifico = 2.5e3  # 2500.0

# Operazioni base
somma = 10 + 5          # 15
sottrazione = 10 - 5    # 5
moltiplicazione = 10 * 5 # 50
divisione = 10 / 3      # 3.333...
divisione_intera = 10 // 3  # 3
modulo = 10 % 3         # 1
potenza = 2 ** 3        # 8

print(f"Somma: {somma}, Divisione: {divisione}")

**Output:**
Somma: 15, Divisione: 3.3333333333333335

#### 4.2 Stringhe

# Definizione
nome = "Python"
cognome = 'Programmazione'

# Concatenazione
messaggio = nome + " " + cognome
print(messaggio)  # Python Programmazione

# F-strings (Python 3.6+)
eta = 30
presentazione = f"Ho {eta} anni"
print(presentazione)  # Ho 30 anni

# Metodi utili
testo = "ciao mondo"
print(testo.upper())        # CIAO MONDO
print(testo.capitalize())   # Ciao mondo
print(testo.replace("ciao", "hello"))  # hello mondo
print(len(testo))           # 10

# Slicing
parola = "Python"
print(parola[0])      # P
print(parola[1:4])    # yth
print(parola[-1])     # n
print(parola[:3])     # Pyt

**Output:**
CIAO MONDO
Ciao mondo
hello mondo
10
P
yth
n
Pyt

#### 4.3 Liste

Le liste sono collezioni ordinate e modificabili.

# Creazione
frutti = ["mela", "banana", "arancia"]
numeri = [1, 2, 3, 4, 5]
mista = [1, "due", 3.0, True]

# Accesso
print(frutti[0])        # mela
print(frutti[-1])       # arancia

# Modifica
frutti[1] = "pera"
print(frutti)           # ['mela', 'pera', 'arancia']

# Aggiungere elementi
frutti.append("kiwi")
print(frutti)           # ['mela', 'pera', 'arancia', 'kiwi']

# Rimuovere elementi
frutti.remove("pera")
print(frutti)           # ['mela', 'arancia', 'kiwi']

# Lunghezza
print(len(frutti))      # 3

# Slicing
print(numeri[1:4])      # [2, 3, 4]

**Output:**
mela
arancia
['mela', 'pera', 'arancia']
['mela', 'pera', 'arancia', 'kiwi']
['mela', 'arancia', 'kiwi']
3
[2, 3, 4]

#### 4.4 Tuple

Le tuple sono collezioni ordinate ma **immutabili**.

# Creazione
coordinate = (10, 20)
dati = ("Mario", 25, "Milano")

# Accesso
print(coordinate[0])    # 10
print(dati[1])          # 25

# Unpacking
x, y = coordinate
print(f"x={x}, y={y}")  # x=10, y=20

# Le tuple non possono essere modificate
# coordinate[0] = 15  # Errore!

**Output:**
10
25
x=10, y=20

#### 4.5 Dizionari

I dizionari sono collezioni di coppie chiave-valore.

# Creazione
studente = {
    "nome": "Luca",
    "eta": 22,
    "corso": "Informatica"
}

# Accesso
print(studente["nome"])           # Luca
print(studente.get("eta"))        # 22

# Modifica
studente["eta"] = 23
studente["matricola"] = "12345"
print(studente)

# Chiavi e valori
print(studente.keys())            # dict_keys(['nome', 'eta', 'corso', 'matricola'])
print(studente.values())          # dict_values(['Luca', 23, 'Informatica', '12345'])

# Iterazione
for chiave, valore in studente.items():
    print(f"{chiave}: {valore}")

**Output:**
Luca
22
{'nome': 'Luca', 'eta': 23, 'corso': 'Informatica', 'matricola': '12345'}
dict_keys(['nome', 'eta', 'corso', 'matricola'])
dict_values(['Luca', 23, 'Informatica', '12345'])
nome: Luca
eta: 23
corso: Informatica
matricola: 12345

#### 4.6 Set

I set sono collezioni non ordinate di elementi unici.

# Creazione
numeri = {1, 2, 3, 4, 5}
frutti = {"mela", "banana", "mela"}  # duplicati rimossi
print(frutti)  # {'banana', 'mela'}

# Operazioni sui set
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))         # {1, 2, 3, 4, 5, 6}
print(a.intersection(b))  # {3, 4}
print(a.difference(b))    # {1, 2}

**Output:**
{'banana', 'mela'}
{1, 2, 3, 4, 5, 6}
{3, 4}
{1, 2}

---

## 5. Operatori

### Operatori Aritmetici

\begin{table}[h]
\centering
\begin{tabular}{|l|l|l|}
\hline
\textbf{Operatore} & \textbf{Descrizione} & \textbf{Esempio} \\
\hline
+ & Addizione & 5 + 3 = 8 \\
- & Sottrazione & 5 - 3 = 2 \\
* & Moltiplicazione & 5 * 3 = 15 \\
/ & Divisione & 5 / 2 = 2.5 \\
// & Divisione intera & 5 // 2 = 2 \\
\% & Modulo & 5 \% 2 = 1 \\
** & Potenza & 5 ** 2 = 25 \\
\hline
\end{tabular}
\end{table}

### Operatori di Confronto

x = 10
y = 5

print(x == y)    # False (uguale)
print(x != y)    # True (diverso)
print(x > y)     # True (maggiore)
print(x < y)     # False (minore)
print(x >= y)    # True (maggiore o uguale)
print(x <= y)    # False (minore o uguale)

### Operatori Logici

a = True
b = False

print(a and b)   # False
print(a or b)    # True
print(not a)     # False

# Esempio pratico
eta = 20
ha_patente = True

if eta >= 18 and ha_patente:
    print("Può guidare")
else:
    print("Non può guidare")

**Output:**
Può guidare

---

## 6. Strutture di Controllo

### 6.1 If, Elif, Else

voto = 85

if voto >= 90:
    giudizio = "Eccellente"
elif voto >= 75:
    giudizio = "Buono"
elif voto >= 60:
    giudizio = "Sufficiente"
else:
    giudizio = "Insufficiente"

print(f"Voto: {voto} - Giudizio: {giudizio}")

**Output:**
Voto: 85 - Giudizio: Buono

### 6.2 Ciclo For

# Iterazione su lista
frutti = ["mela", "banana", "arancia"]
for frutto in frutti:
    print(f"Mi piace la {frutto}")

print("\n")

# Range
for i in range(5):
    print(f"Numero: {i}")

print("\n")

# Range con start e stop
for i in range(2, 8):
    print(i, end=" ")  # 2 3 4 5 6 7

print("\n\n")

# Range con step
for i in range(0, 10, 2):
    print(i, end=" ")  # 0 2 4 6 8

**Output:**
Mi piace la mela
Mi piace la banana
Mi piace la arancia

Numero: 0
Numero: 1
Numero: 2
Numero: 3
Numero: 4

2 3 4 5 6 7 

0 2 4 6 8

### 6.3 Ciclo While

# Contatore
contatore = 0
while contatore < 5:
    print(f"Contatore: {contatore}")
    contatore += 1

print("\n")

# Esempio pratico: somma numeri fino a limite
somma = 0
numero = 1
limite = 100

while somma < limite:
    somma += numero
    numero += 1

print(f"La somma è {somma} dopo {numero-1} iterazioni")

**Output:**
Contatore: 0
Contatore: 1
Contatore: 2
Contatore: 3
Contatore: 4

La somma è 105 dopo 14 iterazioni

### 6.4 Break e Continue

# Break: esce dal ciclo
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")  # 0 1 2 3 4

print("\n\n")

# Continue: salta all'iterazione successiva
for i in range(10):
    if i % 2 == 0:  # salta i numeri pari
        continue
    print(i, end=" ")  # 1 3 5 7 9

**Output:**
0 1 2 3 4 

1 3 5 7 9

---

## 7. Funzioni

Le funzioni permettono di organizzare e riutilizzare il codice.

### 7.1 Definizione Base

# Funzione semplice
def saluta():
    print("Ciao!")

saluta()  # Chiamata della funzione

# Funzione con parametri
def saluta_persona(nome):
    print(f"Ciao, {nome}!")

saluta_persona("Mario")
saluta_persona("Luigi")

# Funzione con return
def somma(a, b):
    risultato = a + b
    return risultato

totale = somma(5, 3)
print(f"La somma è: {totale}")

**Output:**
Ciao!
Ciao, Mario!
Ciao, Luigi!
La somma è: 8

### 7.2 Parametri Predefiniti

def potenza(base, esponente=2):
    return base ** esponente

print(potenza(5))       # 25 (usa esponente=2)
print(potenza(5, 3))    # 125 (usa esponente=3)

**Output:**
25
125

### 7.3 Parametri Multipli

def calcola_media(*numeri):
    if len(numeri) == 0:
        return 0
    return sum(numeri) / len(numeri)

print(calcola_media(10, 20, 30))           # 20.0
print(calcola_media(5, 10, 15, 20, 25))    # 15.0

**Output:**
20.0
15.0

### 7.4 Funzioni Lambda

Funzioni anonime per operazioni semplici.

# Funzione tradizionale
def quadrato(x):
    return x ** 2

# Equivalente lambda
quadrato_lambda = lambda x: x ** 2

print(quadrato(5))         # 25
print(quadrato_lambda(5))  # 25

# Lambda con map
numeri = [1, 2, 3, 4, 5]
quadrati = list(map(lambda x: x ** 2, numeri))
print(quadrati)  # [1, 4, 9, 16, 25]

# Lambda con filter
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pari = list(filter(lambda x: x % 2 == 0, numeri))
print(pari)  # [2, 4, 6, 8, 10]

**Output:**
25
25
[1, 4, 9, 16, 25]
[2, 4, 6, 8, 10]

---

## 8. Esercizi Pratici

### Esercizio 1: Calcolatrice Base

Creare una semplice calcolatrice che esegue operazioni base.

def calcolatrice(num1, num2, operazione):
    if operazione == "+":
        return num1 + num2
    elif operazione == "-":
        return num1 - num2
    elif operazione == "*":
        return num1 * num2
    elif operazione == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Errore: divisione per zero"
    else:
        return "Operazione non valida"

print(calcolatrice(10, 5, "+"))   # 15
print(calcolatrice(10, 5, "-"))   # 5
print(calcolatrice(10, 5, "*"))   # 50
print(calcolatrice(10, 5, "/"))   # 2.0
print(calcolatrice(10, 0, "/"))   # Errore: divisione per zero

**Output:**
15
5
50
2.0
Errore: divisione per zero

### Esercizio 2: Lista Numeri Pari

Creare una funzione che restituisce solo i numeri pari da una lista.

def filtra_pari(lista):
    numeri_pari = []
    for numero in lista:
        if numero % 2 == 0:
            numeri_pari.append(numero)
    return numeri_pari

# Versione con list comprehension
def filtra_pari_v2(lista):
    return [n for n in lista if n % 2 == 0]

numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtra_pari(numeri))      # [2, 4, 6, 8, 10]
print(filtra_pari_v2(numeri))   # [2, 4, 6, 8, 10]

**Output:**
[2, 4, 6, 8, 10]
[2, 4, 6, 8, 10]

### Esercizio 3: Conta Vocali

Contare il numero di vocali in una stringa.

def conta_vocali(testo):
    vocali = "aeiouAEIOU"
    contatore = 0
    for carattere in testo:
        if carattere in vocali:
            contatore += 1
    return contatore

frase = "Python è un linguaggio fantastico"
numero_vocali = conta_vocali(frase)
print(f"La frase contiene {numero_vocali} vocali")

**Output:**
La frase contiene 11 vocali

### Esercizio 4: Temperatura Converter

Convertire temperature tra Celsius e Fahrenheit.

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Test
temp_c = 25
temp_f = celsius_a_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

temp_f = 77
temp_c = fahrenheit_a_celsius(temp_f)
print(f"{temp_f}°F = {temp_c}°C")

**Output:**
25°C = 77.0°F
77°F = 25.0°C

### Esercizio 5: Tabellina

Stampare la tabellina di un numero.

def tabellina(numero):
    print(f"Tabellina del {numero}:")
    for i in range(1, 11):
        risultato = numero * i
        print(f"{numero} x {i} = {risultato}")

tabellina(7)

**Output:**
Tabellina del 7:
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70

### Esercizio 6: Palindromo

Verificare se una parola è un palindromo.

def is_palindromo(parola):
    parola = parola.lower().replace(" ", "")
    return parola == parola[::-1]

# Test
parole = ["radar", "python", "anna", "civic", "hello"]
for parola in parole:
    if is_palindromo(parola):
        print(f"{parola} è un palindromo")
    else:
        print(f"{parola} NON è un palindromo")

**Output:**
radar è un palindromo
python NON è un palindromo
anna è un palindromo
civic è un palindromo
hello NON è un palindromo

### Esercizio 7: FizzBuzz

Classico esercizio di programmazione.

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(15)

**Output:**
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz

---

## Conclusioni

In questa lezione abbiamo coperto i fondamenti di Python:

\begin{itemize}
\item Sintassi base e indentazione
\item Tipi di dati (numeri, stringhe, liste, tuple, dizionari, set)
\item Operatori aritmetici, di confronto e logici
\item Strutture di controllo (if/elif/else, for, while)
\item Funzioni e parametri
\item Esercizi pratici
\end{itemize}

### Prossimi Passi

Per continuare l'apprendimento:

\begin{enumerate}
\item Praticare con gli esercizi proposti
\item Esplorare la programmazione object-oriented
\item Studiare moduli e package
\item Gestione file e eccezioni
\item Lavorare con librerie esterne (requests, pandas, etc.)
\end{enumerate}

### Risorse Utili

\begin{itemize}
\item Documentazione ufficiale Python: python.org/doc
\item Tutorial interattivi: codecademy.com, realpython.com
\item Esercizi pratici: hackerrank.com, leetcode.com
\end{itemize}
