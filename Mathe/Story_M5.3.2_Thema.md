
# Story M5.3.2 - Das Gauß-Verfahren

## 1. Operation (Analog)

**Gegeben:**
* Zeile I: $(2, 4, | 8)$
* Zeile II: $(1, 5, | 7)$

**Ziel:** Eine $0$ an der ersten Stelle von Zeile II erzeugen.

**Operation:** Wir rechnen: **Zeile II minus (0,5 mal Zeile I)** oder verdoppeln Zeile II: **$2 \cdot \text{Zeile II} - \text{Zeile I}$**

**Berechnung:**
$$
\begin{aligned}
2 \cdot (1, 5, | 7) &= (2, 10, | 14) \\
- (2, 4, | 8) &= (-2, -4, | -8) \\
\hline
\text{Neue Zeile II} &= (0, 6, | 6)
\end{aligned}
$$

**Ergebnis für die neue Zeile II:** $(0, 6, | 6) \implies 6 \cdot x_2 = 6$

---

## 2. Durchführung (Analog - Kiosk-System lösen)

**Ausgangssystem aus Story M5.3.1:**
* I: $2 \cdot x_1 + 3 \cdot x_2 = 8$
* II: $1 \cdot x_1 + 4 \cdot x_2 = 7$

**Schritt 1: Matrix aufstellen**
$$
\left(
\begin{array}{cc|c}
2 & 3 & 8 \\
1 & 4 & 7
\end{array}
\right)
$$

**Schritt 2: Null erzeugen in Zeile II**
Operation: $2 \cdot \text{Zeile II} - \text{Zeile I}$
$$
\begin{aligned}
2 \cdot (1, 4, | 7) &= (2, 8, | 14) \\
- (2, 3, | 8) &= (-2, -3, | -8) \\
\hline
\text{Neue Zeile II} &= (0, 5, | 6)
\end{aligned}
$$

Neue Matrix in Stufenform:
$$
\left(
\begin{array}{cc|c}
2 & 3 & 8 \\
0 & 5 & 6
\end{array}
\right)
$$

**Schritt 3: Rückwärtseinsetzen**
* Aus Zeile II folgt: $5 \cdot x_2 = 6 \implies x_2 = \frac{6}{5} = 1,2$ (Preis für Chips = 1,20 €)
* Einsetzen in Zeile I: 
  $$
  \begin{aligned}
  2 \cdot x_1 + 3 \cdot 1,2 &= 8 \\
  2 \cdot x_1 + 3,6 &= 8 \quad | - 3,6 \\
  2 \cdot x_1 &= 4,4 \quad | : 2 \\
  x_1 &= 2,2
  \end{aligned}
  $$

**Lösung:** $x_1 = 2,2$ (Cola = 2,20 €) und $x_2 = 1,2$ (Chips = 1,20 €)

---

## 3. Dreiecksform (Analog)

**Gegebenes System in Stufenform:**
1. $1x + 2y + 3z = 6$
2. $0x + 4y + 2z = 8$
3. $0x + 0y + 5z = 10$

**Schritt 1: $z$ bestimmen aus Gleichung 3**
$$5z = 10 \implies z = 2$$

**Schritt 2: $y$ bestimmen aus Gleichung 2 (mit $z = 2$)**
$$
\begin{aligned}
4y + 2 \cdot 2 &= 8 \\
4y + 4 &= 8 \quad | - 4 \\
4y &= 4 \implies y = 1
\end{aligned}
$$

**Schritt 3: $x$ bestimmen aus Gleichung 1 (mit $y = 1$ und $z = 2$)**
$$
\begin{aligned}
1x + 2 \cdot 1 + 3 \cdot 2 &= 6 \\
x + 2 + 6 &= 6 \\
x + 8 &= 6 \quad | - 8 \\
x &= -2
\end{aligned}
$$

**Ergebnis:** $x = -2$, $y = 1$, $z = 2$

---

## 4. Algorithmus-Entwurf

Um eine $3 \times 3$ Matrix auf Stufenform (Nullen unten links) zu bringen, nutzt man folgenden Ablauf in Worten:

1. **Spalten-Schleife:** Wir gehen von links nach rechts durch die Spalten (Spalte 1, dann Spalte 2).
2. **Pivot-Element bestimmen:** Das "Pivot" (Drehpunkt) ist das Element auf der Hauptdiagonale der aktuellen Spalte (z. B. Zeile 1, Spalte 1 für die erste Runde).
3. **Nullen erzeugen:** Für alle Zeilen, die *unter* dem Pivot liegen:
   * Berechne einen Faktor: $\text{Faktor} = \frac{\text{Zahl unter dem Pivot}}{\text{Pivot-Zahl}}$
   * Ziehe das $\text{Faktor}$-fache der Pivot-Zeile von der aktuellen Zeile ab, sodass dort eine $0$ entsteht.
4. **Wiederholung:** Gehe zur nächsten Spalte und wiederhole den Schritt für die Zeilen darunter.

---

## 5. Probe (Analog)

Wir setzen unsere Lösung $x_1 = 2,2$ und $x_2 = 1,2$ in die Originalgleichungen ein:

**Gleichung I (Paket A):**
$$2 \cdot 2,2 + 3 \cdot 1,2 = 4,4 + 3,6 = 8 \quad \checkmark (\text{Stimmt})$$

**Gleichung II (Paket B):**
$$1 \cdot 2,2 + 4 \cdot 1,2 = 2,2 + 4,8 = 7 \quad \checkmark (\text{Stimmt})$$

Die gefundene Lösung ist mathematisch zu 100 % korrekt.