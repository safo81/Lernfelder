# Epic P2.4 - Konsolen-Design & ASCII Art
## Story P2.4.2 - Tabellenstruktur & Rangliste

### 1. Akzeptanzkriterien (Gherkin Vorgabe)

* **Tabellenstruktur generieren**
  * **Gegeben** das Spiel hat die Platzierungen berechnet
  * **Wenn** die Rangliste auf dem Bildschirm ausgegeben wird
  * **Dann** wird eine klar unterteilte Tabelle mit Spalten für Platz, Spieler und Punkte gezeichnet

* **Visuelle Trennung anwenden**
  * **Gegeben** die Tabelle für die Rangliste wird erstellt
  * **Wenn** die grafische Formatierung angewendet wird
  * **Dann** verfügt die Tabelle über definierte Rahmenlinien und einen abgesetzten Kopfbereich

* **Korrekte Sortierung in der Ansicht**
  * **Gegeben** die berechneten Spielerdaten werden in die Tabelle eingetragen
  * **Wenn** die Tabelle gerendert wird
  * **Dann** ist der Spieler mit den meisten Punkten visuell ganz oben platziert

---

### 2. Technische Umsetzung (Python-Tricks)
* **Formatierung:** Mit `{:<11}` reservieren wir festen Platz in der Konsole, damit die Rahmenlinien (`|`) nicht verrutschen, egal wie lang ein Name ist.
* **Sortierung:** Mit `reverse=True` sortieren wir die Liste absteigend, sodass die größte Punktzahl ganz oben steht.

---

### 3. Unser Python-Code (`rangliste.py`)

```python
spieler_daten = [
    {"name": "Safouan", "punkte": 450},
    {"name": "Alex", "punkte": 950},
    {"name": "Mia", "punkte": 720}
]

# Höchste Punkte nach oben sortieren
spieler_daten.sort(key=lambda x: x["punkte"], reverse=True)

# Tabelle zeichnen
print("+------+------------+---------+")
print("| Platz| Spieler    | Punkte  |")
print("+------+------------+---------+")

platz = 1
for spieler in spieler_daten:
    print(f"| {platz:<5}| {spieler['name']:<11}| {spieler['punkte']:<8}|")
    platz = platz + 1

print("+------+------------+---------+")