
# Story M5.3.3 - Sonderfälle linearer Gleichungssysteme

## 1. Diagnose (Analog)

**Gegeben:** Letzte Zeile nach dem Gauß-Verfahren: $0 \cdot x_3 = 7$ (bzw. $0 = 7$).

**Bedeutung für das LGS:**
Das LGS hat **keine Lösung** (leere Lösungsmenge $\mathbb{L} = \emptyset$). Mathematisch entsteht hier ein Widerspruch, da $0$ niemals $7$ sein kann. Das System ist somit unlösbar.

---

## 2. Freiheitsgrade (Analog)

**Gegeben:** Letzte Zeile $0 = 0$. Wir haben 3 Variablen ($x_1, x_2, x_3$), aber effektiv nur 2 Gleichungen. Das bedeutet: Es gibt unendlich viele Lösungen.

Wir setzen den freien Parameter: $x_3 = t$ (wobei $t$ eine beliebige reelle Zahl ist).

*Beispielhafte Herleitung (basierend auf einer Standard-Stufenform wie $x_2 + x_3 = 1$ und $x_1 + x_2 + x_3 = 1$):*

* **$x_3$ ausgedrückt durch $t$:**
  $$x_3 = t$$
* **$x_2$ ausgedrückt durch $t$:**
  $$x_2 + t = 1 \implies x_2 = 1 - t$$
* **$x_1$ ausgedrückt durch $t$:**
  $$x_1 + (1 - t) + t = 1 \implies x_1 + 1 = 1 \implies x_1 = 0$$

**Allgemeine Lösungsform:** Die Variablen $x_1$ und $x_2$ hängen direkt vom gewählten Wert für $t$ ab.

---

## 3. Geometrie (Analog)

Im zweidimensionalen Raum (2D) entsprechen lineare Gleichungen Geraden. Je nach Anzahl der Lösungen unterscheidet man drei Lagen:

* **1 Lösung:** Die Geraden **schneiden sich** in genau einem Punkt.
* **0 Lösungen:** Die Geraden verlaufen **echt parallel** zueinander. Da sie sich niemals berühren, gibt es keinen gemeinsamen Punkt.
* **Unendlich viele Lösungen:** Die Geraden sind **identisch** (sie liegen exakt aufeinander). Jeder Punkt auf der Geraden ist eine Lösung.

---

## 4. Szenario-Check

**Problem:** Ein Kunde möchte eine Mischung mit **0g Fett**, aber beide verfügbaren Rohstoffe (A und B) enthalten Fett.

**Warum das LGS keine Lösung liefert:**
Da beide Rohstoffe Fett enthalten, erhöht jede Zunahme von Rohstoff A oder Rohstoff B automatisch den Gesamtfettgehalt der Mischung. Es ist mathematisch und physikalisch unmöglich, eine positive Menge der Rohstoffe zu mischen und am Ende bei exakt $0\text{g}$ Fett zu landen. Die mathematische Forderung führt auf einen Widerspruch im System.

---

## 5. Python-Exception

Wenn man versucht, ein unlösbares oder unterbestimmtes Gleichungssystem mit der Standard-Bibliothek **NumPy** (`numpy.linalg.solve()`) zu lösen, erwartet man folgende Fehlermeldung:

```python
LinAlgError: Singular matrix