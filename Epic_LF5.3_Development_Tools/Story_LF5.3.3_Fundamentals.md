# LF 5.3.3: Git Basics & States

## 1. Die drei Zustände einer Datei in Git (K1)
In einem lokalen Git-Repository befindet sich eine Datei immer in einem von drei Zuständen:

1. **Working Directory (Arbeitsverzeichnis):** Man hat die Datei auf der Festplatte liegen. Man bearbeitet den Inhalt ganz normal. Die Änderungen sind noch ungesichert und für Git "unsichtbar".
2. **Staging Area (Index / Wartesaal):** Mit dem Befehl `git add` markiert man die Datei und setzt sie auf die virtuelle Packliste für den nächsten Speicherpunkt.
3. **Repository (Committed / Sicherer Speicher):** Mit dem Befehl `git commit` speichert man die vorbereiteten Dateien dauerhaft, unveränderlich und sicher in der lokalen Git-Datenbank ab.

---

## 2. Der Zweck der Staging Area (K2)
Die Staging Area dient als Vorbereitungszone (oder "Packtisch"), bevor Änderungen dauerhaft gespeichert werden. Ihr Zweck lässt sich wie folgt zusammenfassen:

* **Gezieltes Auswählen:** Man muss nicht alle geänderten Dateien auf einmal speichern. Man wählt präzise aus, welche Dateien bereit für das Repository sind.
* **Thematische Ordnung:** Man kann verschiedene Änderungen sauber trennen. Es werden nur die Dateien verpackt, die zu einer bestimmten Aufgabe gehören, was die Historie übersichtlich hält.
* **Sicherheitsnetz:** Man kann seine Auswahl im Wartesaal noch einmal in Ruhe kontrollieren, bevor man den finalen Speicher-Befehl absendet.

---

## 3. Praktische Terminal-Befehle (K3)

**Eine Datei (z. B. `index.html`) in die Staging Area bewegen:**
```bash
git add index.html

Aufgabe 4: Befehl für den Commit (K3)
Der exakte Terminal-Befehl, um die vorbereiteten Änderungen dauerhaft mit der Nachricht "Add login button" zu speichern, lautet:

Bash

git commit -m "Add login button"
Aufgabe 5: Unterschied zwischen git push und git pull (K2)
Man nutzt diese beiden Befehle, um den Code zwischen dem eigenen PC (lokal) und dem Server im Internet (GitHub) abzugleichen:

git push (Hochladen): Man sendet seine lokal gespeicherten Commits hoch zu GitHub. Man teilt seine fertige Arbeit mit dem Team oder sichert sie in der Cloud. (Richtung: Lokal → GitHub)
git pull (Herunterladen): Man holt sich die neuesten Änderungen von GitHub herunter auf den eigenen PC. Man aktualisiert seinen lokalen Stand, damit man auf dem gleichen Stand wie das Team ist. (Richtung: GitHub → Lokal)