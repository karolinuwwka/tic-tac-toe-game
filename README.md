# tic-tac-toe-game
klasiskā ''krusta un nulles'' spēle python valodā

# Tic-Tac-Toe (Krusta un Nulles)

Šī ir divu spēlētāju klasiskā spēle **"Krusta un Nulles"**, uzrakstīta Python programmēšanas valodā. Spēlētāji mainās ar gājieniem, ievadot koordinātas 3x3 spēles laukuma pozīcijās. Spēles mērķis ir iegūt trīs savus simbolus (`X` vai `O`) rindā, kolonnā vai pa diagonāli.

---

## Kā spēlēt

1. Kad programma tiek palaista, tiks ģenerēts tukšs 3x3 spēles laukums.
2. Spēlētājs 1 izmanto simbolu `X`, un Spēlētājs 2 izmanto simbolu `O`.
3. Katrs spēlētājs pēc kārtas ievada **rindas numuru** un **kolonnas numuru** (no 0 līdz 2), lai veiktu savu gājienu.
4. Programma pārbauda:
   - Vai kāds spēlētājs ir uzvarējis.
   - Vai spēle ir beigusies ar neizšķirtu.
5. Spēle beidzas, kad ir uzvarētājs vai visi lauciņi ir aizpildīti.

---

## Prasības

- Python 3.6 vai jaunāka versija.

---

## Kā palaist

1. Lejupielādējiet failu `tic_tac_toe.py` savā datorā.
2. Atveriet termināli vai konsoli un pārvietojieties uz mapi, kur atrodas fails.
3. Izpildiet komandu:

   ```bash
   python tic_tac_toe.py
   ```

4. Sekojoši, ievadiet savus gājienus atbilstoši norādījumiem uz ekrāna.

---

## Spēles noteikumi

1. Spēles laukums ir 3x3 režģis.
2. Spēlētāji pēc kārtas ievada gājiena koordinātas (rindu un kolonnu), piemēram:
   - Rinda: `1`
   - Kolonna: `2`
3. Gājienu var veikt tikai uz tukšiem laukiem.
4. Uzvarētājs ir tas, kurš pirmais iegūst 3 simbolus (`X` vai `O`) vienā rindā, kolonnā vai pa diagonāli.
5. Ja visi lauciņi ir aizpildīti un nav uzvarētāja, spēle beidzas ar neizšķirtu.

---

## Piemērs

### Spēles sākums:
```
  0   1   2
0    |   |  
  ---+---+---
1    |   |  
  ---+---+---
2    |   |  
```

### Pēc dažiem gājieniem:
```
  0   1   2
0  X |   | O
  ---+---+---
1    | X |  
  ---+---+---
2  O |   |  
```

---

## Autors

Šī spēle tika veidota kā piemērs Python algoritma un spēles loģikas izstrādei. Ceru,ka tā būs patīkama

--- 
