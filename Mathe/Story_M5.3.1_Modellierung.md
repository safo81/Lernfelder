
# Story M5.3.1 - Das System aufstellen

## 1. Text zu Mathe (Modellierung & Matrixform)

**Variablen:**
* $x_1 =$ Preis für eine Cola
* $x_2 =$ Preis für eine Tüte Chips

**Klassische Gleichungen:**
* I (Paket A): $2 \cdot x_1 + 3 \cdot x_2 = 8$
* II (Paket B): $1 \cdot x_1 + 4 \cdot x_2 = 7$

**Form $M \cdot \vec{x} = \vec{c}$:**

$$
\begin{pmatrix}
2 & 3 \\
1 & 4
\end{pmatrix}
\cdot
\begin{pmatrix}
x_1 \\
x_2
\end{pmatrix}
=
\begin{pmatrix}
8 \\
7
\end{pmatrix}
$$

---

## 2. Lücken füllen (Koeffizientenmatrix)

*Hinweis: Wo Variablen fehlen (z. B. kein $y$ in Gleichung III oder kein $x$ in Gleichung II), schreiben wir eine $0$.*

**Gegebenes LGS:**
* I: $1x - 1y + 1z = 0$
* II: $0x + 2y - 1z = 5$
* III: $3x + 0y + 4z = 10$

**Koeffizientenmatrix $A$:**

$$
A = 
\begin{pmatrix}
1 & -1 & 1 \\
0 & 2 & -1 \\
3 & 0 & 4
\end{pmatrix}
$$

---

## 3. Reverse Engineering (Zurückübersetzen)

Aus der Matrixform machen wir wieder normale Gleichungen mit $x$ (erste Spalte) und $y$ (zweite Spalte):

* I: $1x + 0y = 5 \implies x = 5$
* II: $2x + 1y = 6 \implies 2x + y = 6$

---

## 4. Python-Vorarbeit

Hier ist die Matrix $A$ aus Aufgabe 2 sauber als Liste von Listen (Zeile für Zeile) in Python definiert:

```python
# Koeffizientenmatrix A aus Aufgabe 2
matrix_A = [
    [1, -1, 1],   # Erste Zeile (I)
    [0, 2, -1],   # Zweite Zeile (II)
    [3, 0, 4]     # Dritte Zeile (III)
]