# Epic P2.4: Konsolen-Design & ASCII Art (Anwendungsfall: Item-Shop)

## 1. Ausgangslage & Ziel
Im Rahmen des Spieleprojekts soll ein interaktiver Marktplatz (Item-Shop) für den Spieler bereitgestellt werden. Um eine hohe Benutzerfreundlichkeit (UX) und ein immersives Spielerlebnis direkt in der Konsole zu erzielen, darf dieser Shop nicht aus unstrukturiertem Text bestehen. 

Das Ziel dieses Epics ist die visuelle und strukturelle Gestaltung eines professionellen Terminal-Interfaces für den Shop unter Anwendung von dynamischen Farben, geometrischen Symbolen und tabellarischen Strukturen.

## 2. Gesamtaufgabe & Kernanforderungen

### 1. Farbcodierte Benutzeroberfläche (Semantische Farben)
* **Anforderung:** Das System muss den Zustand des Spielers (z. B. das verbleibende Guthaben oder Systemereignisse) farblich signalisieren.
* **Verhalten:** Ist genug Gold für Einkäufe vorhanden, wird eine positive Bestätigung in **Grün** ausgegeben. Fällt das Gold unter ein kritisches Limit oder tritt ein Fehler auf, schlägt das System visuell in **Rot** Alarm.

### 2. Dynamische, strukturierte Datenpräsentation (Tabelle)
* **Anforderung:** Die kaufbaren Gegenstände dürfen nicht lose untereinanderstehen, sondern müssen in einer klar abgegrenzten Tabellenstruktur gerendert werden.
* **Verhalten:** Die Tabelle muss über saubere Rahmenlinien (`+`, `-`, `|`) und einen visuell abgesetzten Kopfbereich (Header) verfügen. Die Gegenstände müssen vor der Anzeige automatisch logisch nach ihrem Preis aufsteigend sortiert werden, sodass das günstigste Item immer ganz oben steht.

### 3. Geometrisch konsistente Grafiken (ASCII Art)
* **Anforderung:** Zur visuellen Aufwertung wird ein zentrales Icon (z. B. eine Schatztruhe) als mehrzeilige 2D-Zeichengrafik im Terminal ausgegeben.
* **Verhalten:** Das grafische Element muss eine feste Breite und Höhe besitzen (formstabil sein), damit das Interface bei der Aktualisierung oder beim Rendern niemals verzerrt wird oder verrutscht.