import random

# FARBEN (für die Übersicht im Terminal)
GRUEN = "\033[92m"
ROT = "\033[91m"
GELB = "\033[93m"
BLAU = "\033[94m"
FETT = "\033[1m"
RESET = "\033[0m"

# 1. GRAPHIC (ASCII Art) - Eine formstabile Schatztruhe (5 Zeilen hoch, 13 Zeichen breit)
schatztruhe = [
    "+-----------+",
    "|   [===]   |",
    "|  |  o  |  |",
    "|  +-----+  |",
    "+-----------+",
]

print(f"{FETT}{GELB}=== WILLKOMMEN IM ITEM-SHOP ==={RESET}\n")

# Zeige die formstabile Grafik
for zeile in schatztruhe:
    print(f"{BLAU}{zeile}{RESET}")
print()


# 2. STATUS-MELDUNGEN (Farbliche Hervorhebungen)
kontostand = random.choice([50, 500])  # Simuliert zufällig viel oder wenig Geld

print(f"{FETT}Dein Guthaben: {kontostand} Goldmünzen{RESET}")

if kontostand >= 200:
    print(f"{GRUEN}[INFO] Du hast genug Gold für Premium-Gegenstände!{RESET}\n")
else:
    print(f"{ROT}[WARNUNG] Dein Gold ist knapp! Sparsam sein!{RESET}\n")


# 3. STRUKTURIERTE TABELLE (Gegenstände nach Preis sortiert)
# Die Rohdaten im Hintergrund
shop_items = [
    {"name": "Heiltrank", "preis": 50},
    {"name": "Ausrüstung", "preis": 450},
    {"name": "Eisenschwert", "preis": 200},
]

# Sortierung: Günstigste Items zuerst (aufsteigend nach Preis)
shop_items.sort(key=lambda x: x["preis"])

print(f"{FETT}VERFÜGBARE GEGENSTÄNDE (Nach Preis sortiert):{RESET}")
print("+----------------------+---------+")
print(f"| {FETT}Gegenstand          {RESET} | {FETT}Preis   {RESET} |")
print("+----------------------+---------+")

for item in shop_items:
    # :20 zieht den Namen auf 20 Zeichen Breite, :7 zieht den Preis auf 7 Zeichen
    print(f"| {item['name']:20} | {item['preis']:7} |")

print("+----------------------+---------+")
