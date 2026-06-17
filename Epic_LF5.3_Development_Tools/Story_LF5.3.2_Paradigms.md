# LF 5.3.2: Version Control Systems (VCS)

## 1. Definition: Was ist ein VCS? (K1)
Ein **Version Control System** (Versionsverwaltungssystem) ist eine Software, die alle Änderungen am Quellcode eines Projekts lückenlos protokolliert und verwaltet, sodass Entwickler jederzeit zu älteren Code-Ständen zurückkehren und problemlos im Team gleichzeitig an denselben Dateien arbeiten können.

---

## 2. Architektur-Vergleich (K2)

### Zentralisiertes VCS (z. B. SVN)
* **Wo liegt die Historie?** Die komplette Projekthistorie liegt exklusiv auf einem einzigen, zentralen Server.
* **Wie arbeiten die Clients?** Die Entwickler-PCs (Clients) besitzen lokal nur eine reine Arbeitskopie des aktuellen Stands – komplett ohne die Vergangenheit des Projekts.
* **Das Risiko:** Fällt dieser zentrale Server aus oder hat man kein Backup, ist die gesamte Projekthistorie für immer verloren.

### Dezentralisiertes / Verteiltes VCS (z. B. Git)
* **Wo liegt die Historie?** Jeder einzelne Arbeitsplatz (Client) besitzt eine vollständige, lokale Kopie des gesamten Repositories. Das bedeutet: die komplette Historie, alle Branches und alle Metadaten sind auf jedem PC gesichert.
* **Die Unabhängigkeit:** Es gibt keinen *Single Point of Failure*. Jeder Entwickler kann komplett autark offline arbeiten, Commits erstellen und die Historie durchsuchen.

---

## 3. Der Hauptnachteil eines zentralisierten VCS (K2)
Der größte Schwachpunkt (*Single Point of Failure*) tritt auf, wenn die Netzwerkverbindung abbricht oder der Server offline ist:
* Der Entwickler ist sofort **komplett blockiert**.
* Man kann weder ältere Code-Versionen vergleichen, noch aktuelle Änderungen im System abspeichern (Commit).
* Das Arbeiten ist nur noch isoliert auf der Festplatte möglich, ohne jede schützende Versionskontrolle.

---

## 4. Der exakte Unterschied zwischen Git und GitHub (K1)

| Werkzeug / Plattform | Beschreibung & Funktion |
| :--- | :--- |
| **Git** *(Das Werkzeug)* | Die eigentliche Software (das Versionsverwaltungssystem), die lokal auf deinem PC läuft. Git trackt deine Änderungen, speichert deine Commits und verwaltet die Historie auf deiner Festplatte. Es funktioniert zu 100 % ohne Internet. |
| **GitHub** *(Die Plattform)* | Ein Cloud-Dienst im Internet (eine Webseite). GitHub bietet Online-Speicherplatz für deine lokalen Git-Repositories, damit du deinen Code sichern, teilen und im Team gemeinsam via Pull Requests bearbeiten kannst. |
