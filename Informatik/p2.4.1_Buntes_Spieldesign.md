
# Epic P2.4 - Konsolen-Design & ASCII Art
## Story P2.4.1 - Buntes und ansprechendes Spieldesign

### 1. Ziel der Aufgabe
Systemmeldungen in der Konsole (wie Erfolge oder Fehler) sollen für den Spieler optisch sofort erkennbar sein. Dafür nutzen wir farbige Hervorhebungen.

---

### 2. Technische Umsetzung (ANSI Escape Codes)
Um Text im Terminal einzufärben, nutzt man Steuercodes. In Python haben wir dafür Variablen angelegt:

* **Grün (Erfolg):** `\033[32m`
* **Rot (Fehler):** `\033[31m`
* **Reset (Ausschalten):** `\033[0m` (Ganz wichtig, damit nicht der gesamte Text danach farbig bleibt!)

---

### 3. Unser Python-Code (`spiel_design.py`)
Der Code verbindet die Farbcodes mit dem Text über das `+`-Zeichen:

```python
ROT = "\033[31m"
GRUEN = "\033[32m"
RESET = "\033[0m"

# Ausgabe Erfolg
print(GRUEN + "Erfolg: Du hast das Level bestanden!" + RESET)

# Ausgabe Fehler
print(ROT + "Fehler: Die Systemmeldung ist fehlgeschlagen!" + RESET)