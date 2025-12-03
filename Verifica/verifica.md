# Verifica Linux - Versione Light
## Creare File e Cartelle e Navigare con cd

### Comandi Principali
- `pwd` - mostra la directory corrente
- `mkdir` - crea una nuova cartella
- `touch` - crea un file vuoto
- `cd` - cambia directory
- `ls` - elenca il contenuto
- `cp` - copia file o cartelle
- `mv` - sposta o rinomina
- `rm` - rimuovi

**Comandi Utili:**
- `mkdir -p` - crea cartelle annidate
- `cp -r` - copia cartelle ricorsivamente
- `cd -` - torna alla directory precedente
- `cd ..` - vai indietro di un livello

---

## Parte 1: Preparazione
**Esercizio 1.1**
- Verifica dove ti trovi con `pwd`
- Vai nella tua home directory
- Crea una cartella chiamata `lab_linux`
- Entra nella cartella e verifica la posizione

---

## Parte 2: Creare Struttura
**Esercizio 2.1**

Crea questa struttura:
```
lab_linux/
├── progetti/
│   ├── app_a/
│   └── app_b/
├── documenti/
└── backup/
```

**Esercizio 2.2**

Crea questi file:
- `main.py` in `progetti/app_a/`
- `note.txt` in `progetti/app_b/`
- `report.doc` in `documenti/`

---

## Parte 3: Navigazione con Percorsi Relativi
**Esercizio 3.1**
- Da `lab_linux`, vai in `progetti/app_a` con un percorso relativo
- Torna indietro di due livelli in un comando
- Vai in `documenti` e poi torna a `lab_linux` con percorso assoluto

**Esercizio 3.2**
- Da `lab_linux`, vai in `progetti/app_b`
- Da lì, vai in `documenti` usando `../..`
- Usa `cd -` per tornare alla directory precedente

---

## Parte 4: Copiare File (cp)
**Esercizio 4.1**
- Copia `progetti/app_a/main.py` nella cartella `backup`
- Copia `documenti/report.doc` in `backup` rinominandolo `report_backup.doc`
- Copia l'intera cartella `progetti/app_a` chiamandola `progetti/app_a_backup`

---

## Parte 5: Spostare e Rinominare (mv)
**Esercizio 5.1**
- Rinomina `progetti/app_b/note.txt` in `appunti.txt`
- Sposta `documenti/report.doc` nella cartella `backup`
- Rinomina la cartella `progetti/app_b` in `progetti/app_beta`

---

## Parte 6: Esercizio Finale
**Crea questa struttura completa:**
```
progetto_web/
├── frontend/
│   ├── css/
│   │   └── style.css
│   └── index.html
├── backend/
│   └── server.py
└── docs/
    └── README.md
```

Poi:
1. Copia `server.py` in `backup/`
2. Sposta la cartella `progetto_web` dentro `backup/`
3. Rinomina `backup` in `backup_finale`

---

