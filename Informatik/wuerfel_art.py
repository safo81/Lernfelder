# Wir holen uns ein Werkzeug, um zufällig zu würfeln
import random

# Wir bauen eine "Übersetzungs-Box" (ein Dictionary) für die Würfelbilder.
# Jeder Würfel hat genau 5 Zeilen Höhe und 9 Zeichen Breite!
wuerfel_bilder = {
    1: ["+-------+", "|       |", "|   o   |", "|       |", "+-------+"],
    2: ["+-------+", "| o     |", "|       |", "|     o |", "+-------+"],
    3: ["+-------+", "| o     |", "|   o   |", "|     o |", "+-------+"],
    4: ["+-------+", "| o   o |", "|       |", "| o   o |", "+-------+"],
    5: ["+-------+", "| o   o |", "|   o   |", "| o   o |", "+-------+"],
    6: ["+-------+", "| o   o |", "| o   o |", "| o   o |", "+-------+"],
}

# 1. ZUFÄLLIG WÜRFELN (Zahl von 1 bis 6)
geworfen = random.randint(1, 6)
print(f"Du hast eine {geworfen} gewürfelt!\n")

# 2. DEN PASSENDEN WÜRFEL ANZEIGEN
# Wir holen uns die 5 Zeilen für die gewürfelte Zahl
bild_zeilen = wuerfel_bilder[geworfen]

# Mit einer Schleife drucken wir die Zeilen untereinander aus
for zeile in bild_zeilen:
    print(zeile)
