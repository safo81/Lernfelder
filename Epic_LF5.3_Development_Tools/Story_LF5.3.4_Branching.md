# LF 5.3.4: Git Branching & Workflows

## Aufgabe 1: Definition "Branch" (K1)
Ein **Branch** (Zweig) ist eine unabhängige Entwicklungslinie innerhalb eines Git-Repositories. Er ist im Grunde ein beweglicher Zeiger auf einen bestimmten Speicherpunkt (Commit). Man nutzt einen Branch, um an neuen Funktionen (Features) oder Fehlerbehebungen zu arbeiten, ohne den stabilen Hauptcode (`master` oder `main`) zu beeinflussen.

---

## Aufgabe 2: Konzept des "Feature Branch Workflow" (K2)
Man nutzt diesen Workflow, um die Zusammenarbeit im Team oder die Arbeit an verschiedenen Aufgaben sauber zu strukturieren. Das Grundprinzip funktioniert wie folgt:

* **Der Kern:** Alle neuen Funktionen, Fehlerbehebungen oder Stories werden niemals direkt auf dem Hauptzweig (`master` / `main`) entwickelt.
* **Der Ablauf:** 1. Für jede neue Aufgabe erstellt man einen eigenen, separaten Zweig (den Feature-Branch). 
  2. Auf diesem Zweig arbeitet und speichert man seine Änderungen ungestört ab. 
  3. Erst wenn die Aufgabe komplett fertig und getestet ist, führt man diesen Zweig wieder mit dem Hauptzweig zusammen (Merge).
* **Der Vorteil:** Der Hauptzweig bleibt zu jeder Zeit stabil, sauber und voll funktionsfähig.

---

## Aufgabe 3: Philosophie von "Trunk-based Development" (K2)
Man nutzt diese Methode für schnelle und kontinuierliche Software-Veröffentlichungen. Sie basiert auf zwei Kernpunkten:

* **Ein zentraler Hauptzweig (Trunk):** Alle Entwickler arbeiten auf einem einzigen Hauptzweig oder nutzen nur sehr kurzlebige Branches.
* **Hohe Commit-Frequenz:** Man speichert seine Änderungen mehrmals täglich direkt im Hauptzweig ab. Die Code-Schritte sind dabei bewusst klein.
* **Das Ziel:** Große Konflikte beim Zusammenführen ("Merge-Hell") werden verhindert, da der Code des gesamten Teams ständig miteinander verschmolzen wird.

---

## Aufgabe 4: Definition & Ursache eines "Merge Conflict" (K2)
* **Definition:** Ein Merge-Konflikt tritt auf, wenn Git zwei verschiedene Zweige (Branches) zusammenführen soll, dies aber nicht automatisch schafft und die Hilfe des Entwicklers braucht.
* **Warum er entsteht:** Er entsteht, wenn in beiden Zweigen dieselbe Zeile in derselben Datei verändert wurde oder wenn eine Datei in einem Zweig gelöscht, aber im anderen Zweig bearbeitet wurde. Git weiß dann nicht, welche Version die richtige ist, stoppt den Vorgang und überlässt dem Entwickler die Entscheidung.

---

## Aufgabe 5: Zweck eines "Pull Request" (K2)
Man nutzt einen Pull Request (auf GitLab auch Merge Request genannt), um dem Team vorzuschlagen, die Änderungen von einem Feature-Branch in den Hauptzweig (`master` / `main`) zu übernehmen. Er erfüllt drei Kernzwecke:

* **Code Review (Vier-Augen-Prinzip):** Das Team kann den geschriebenen Code prüfen, Feedback geben und Fehler finden, bevor er live geht.
* **Diskussionsplattform:** Man kann Fragen stellen, Änderungen besprechen und den Code direkt im Browser optimieren.
* **Qualitätssicherung:** Automatische Tests (CI/CD) können prüfen, ob der neue Code fehlerfrei läuft, bevor er mit dem Hauptzweig verschmolzen wird.