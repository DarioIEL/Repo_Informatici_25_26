#OPeratori Logici

eta = 20
ha_biglietto = True

# if eta >= 18 and ha_biglietto:
#     print("Puoi entrare")
# else:
#     print("NON puoi entrare")

if eta >= 18 and ha_biglietto:
    print("Puoi entrare")
elif eta < 18 and ha_biglietto:
    print("Non puoi entrare, non hai ancora 18 anni. Questo anche se hai il biglietto")
elif eta >= 18 and not ha_biglietto:
    print("Anche se sei maggiorenne senza biglietto non entri")
else:
    print("Ma tu, senza avere 18 anni e senza biglietto, dove vuoi andare ? ")
    