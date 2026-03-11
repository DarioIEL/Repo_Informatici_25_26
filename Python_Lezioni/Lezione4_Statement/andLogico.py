#AND Logico: questo mi permette di unire più condizioni creandone una più grande
etaStud = 18
esameTeorico = True

if esameTeorico and etaStud >= 18:
    print("Puoi fare richiesta del foglio rosa")
elif esameTeorico and etaStud < 18:
    print("Hai passato l'esame ma non hai ancora 18 anni, aspetta un altro po' per richiedere il foglio rosa")
elif not esameTeorico and etaStud >= 18:
    print("Mi spiace, hai 18 e più anni ma non hai passato l'esame. Per avere il foglio rosa devi rifarlo")
else:
    print("Ma tu, senza esame e senza avere 18 anni quale foglio rosa speri di avere???")