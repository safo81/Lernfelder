# 1. UNSERE DATEN (Eine Liste mit Spielern und ihren Punkten)
spieler_daten = [
    {"name": "Safouan", "punkte": 450},
    {"name": "Alex", "punkte": 950},
    {"name": "Mia", "punkte": 720}
]

# 2. SORTIERUNG (Die höchsten Punkte sollen nach oben)
# Das sorgt dafür, dass Platz 1 ganz oben steht
spieler_daten.sort(key=lambda x: x["punkte"], reverse=True)

# 3. DIE TABELLE ZEICHNEN
# Tabellenkopf (Abgesetzter Bereich)
print("+------+------------+---------+")
print("| Platz| Spieler    | Punkte  |")
print("+------+------------+---------+")

# Spieler nacheinander ausgeben mit einer Schleife
platz = 1
for spieler in spieler_daten:
    # {:<11} reserviert festen Platz, damit die Rahmenstriche sauber untereinander stehen
    print(f"| {platz:<5}| {spieler['name']:<11}| {spieler['punkte']:<8}|")
    platz = platz + 1

# Tabellenboden
print("+------+------------+---------+")