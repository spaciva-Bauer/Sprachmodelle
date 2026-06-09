# Lösungshinweise: Neuronale Netze mit Orange
### KIT | Technik | Jahrgangsstufe 12 | Unterrichtseinheit 1 – NUR FÜR LEHRKRÄFTE

---

## A | Wiederholung: Das Perzeptron

**Aufgabe A1 – Skizzenbeschriftung**

- `x₁, x₂` = **Eingabewerte** (Eingabeneuronen / Features)
- `w₁, w₂` = **Gewichte** (bestimmen die Stärke des Einflusses jedes Eingangs)
- `f(net)` = **Aktivierungsfunktion** (entscheidet, ob das Neuron „feuert")

> Der Bias-Eingang `x₃` mit Gewicht `w₃` verschiebt die Aktivierungsschwelle und ist immer 1. Damit verhält er sich wie der y-Achsenabschnitt einer Geraden.

---

**Aufgabe A2 – Delta-Lernregel**

- η (Eta) = **Lernrate** – ein frei wählbarer Hyperparameter, typisch zwischen 0,01 und 0,5; bestimmt, wie stark die Gewichte pro Schritt angepasst werden
- y = **tatsächlicher (korrekter) Zielwert** aus den Trainingsdaten
- ŷ = **Vorhersage des Modells** (Ausgabe des Perzeptrons für den aktuellen Eingabevektor)

> Hinweis für die Klasse: Wenn y = ŷ (Vorhersage korrekt), dann ist (y – ŷ) = 0, es findet also **keine Gewichtsanpassung** statt. Nur Fehler führen zu einer Korrektur.

---

**Aufgabe A3 – Welche Daten kann das Perzeptron klassifizieren?**

✅ **linear separierbare Daten**

> Das Perzeptron repräsentiert eine lineare Entscheidungsgrenze (Gerade in 2D, Hyperebene in höheren Dimensionen). Klassen, die sich nicht durch eine solche Grenze trennen lassen (z. B. das XOR-Problem), können vom einfachen Perzeptron nicht korrekt klassifiziert werden. Erst mehrschichtige Netze überwinden diese Einschränkung.

---

## B | Orange – Entscheidungsgrenze und Perzeptron

**Aufgabe B1 – Datensatz iris.tab**

- Zeilen: **150** | Spalten: **5** (4 Features + 1 Zielklasse)
- Klassen: **Iris-setosa, Iris-versicolor, Iris-virginica**

**Lineare Separierbarkeit im Scatter Plot (`petal length` vs. `petal width`):**

*Iris-setosa* ist von den beiden anderen Klassen **klar linear trennbar** (links unten im Plot). *Iris-versicolor* und *Iris-virginica* überlappen leicht – **nicht vollständig linear separierbar**. Das Gesamtproblem ist daher **nicht strikt linear separierbar**.

> Tipp: Lassen Sie die SuS die Achsenwahl ausprobieren. Mit `sepal length`/`sepal width` ist die Überlappung noch stärker. `petal length`/`petal width` zeigt die klarste Trennung.

---

**Aufgabe B2 – Polynomial Classification (Educational)**

1. **Bedeutung der farbigen Flächen:** Jede Farbe entspricht dem Bereich, den das Modell einer Klasse zuordnet – die Farbflächen sind die **Entscheidungsregionen**, die Grenzen dazwischen die **Entscheidungsgrenzen**.

2. **Veränderung bei höherem Degree:**
   - Degree 1: gerade Linie (linear) – entspricht einem Perzeptron
   - Degree 2: gebogene Kurve (quadratisch) – kann einfache Krümmungen modellieren
   - Degree 3+: zunehmend komplexere, gewundene Grenzen

3. **Ab welchem Degree korrekte Trennung:** Bereits ab Degree 2 verbessert sich die Trennung deutlich; ab Degree 3 sind alle drei Klassen in der Regel korrekt getrennt (abhängig von der Achsenwahl).

   **Schlussfolgerung für das Perzeptron (Degree 1):** Eine einzelne Gerade kann beim Iris-Datensatz nicht alle drei Klassen gleichzeitig korrekt trennen, da *versicolor* und *virginica* überlappen. Das Perzeptron versagt hier an der fehlenden linearen Separierbarkeit.

> Didaktischer Hinweis: Das Widget eignet sich gut für eine kurze Klassendiskussion – „Warum reicht eine Gerade nicht?" ist eine produktive Einstiegsfrage.

---

**Aufgabe B3 – Neural Network als Perzeptron (kein Hidden Layer)**

1. **Verfügbare Einstellungen im Neural Network-Widget:**

   ✅ Lernrate *(über Regularisierung indirekt steuerbar)*  
   ✅ Anzahl Hidden Layers *(auf leer setzen = Perzeptron-Modus)*  
   ✅ Max. Iterationen  
   ✅ Aktivierungsfunktion  
   ✅ Regularisierung (α)

2. **Confusion Matrix (Neural Network ohne Hidden Layer, Logistic, iris.tab, 10-fache CV):**

   Typische Accuracy: ca. **75–85 %**. Iris-setosa wird nahezu perfekt erkannt; Verwechslungen fast ausschließlich zwischen *versicolor* und *virginica* – konsistent mit dem Polynomial-Classification-Bild bei Degree 1.

3. **Accuracy:** Typisch ca. **78–85 %**.

   **Übereinstimmung mit B2 Degree 1:** Ja – beide modellieren eine lineare Entscheidungsgrenze; die Accuracy sollte in ähnlichem Bereich liegen.

---

## C | Technischer Datensatz: Ionosphere

**Aufgabe C2 – Standardkonfiguration des Neural Network-Widgets in Orange**

> Die genauen Standardwerte können je nach Orange-Version leicht variieren. Typische Standardwerte:

| Parameter | Typischer Standardwert |
|---|---|
| Hidden Layer Neurons | `100` (eine verdeckte Schicht) |
| Activation | `ReLU` |
| Max Iterations | `200` |
| Regularization (α) | `0.0001` |

**Typische Testergebnisse mit Standardkonfiguration (10-fache CV, ionosphere.tab):**

| Metrik | Typischer Wert |
|---|---|
| Accuracy (CA) | ca. 0,93–0,96 |
| AUC | ca. 0,97–0,99 |
| F1-Score | ca. 0,93–0,96 |

> Der ionosphere-Datensatz ist für neuronale Netze gut geeignet – die hohen Werte sind realistisch und motivieren die SuS.

---

**Aufgabe C3 – Einfluss der Netzarchitektur**

Exakte Werte hängen vom Zufalls-Seed ab. Folgende **Tendenzen** sind zu erwarten:

| Hidden Layers / Neuronen | Erwartete Accuracy | Erwartete Beobachtung |
|---|---|---|
| 1 Schicht, 10 Neuronen | ca. 88–92 % | Gut, aber noch etwas unter Optimum |
| 1 Schicht, 100 Neuronen | ca. 93–96 % | Gutes Ergebnis, nahe optimal |
| 2 Schichten, je 50 Neuronen | ca. 93–96 % | Vergleichbar oder leicht besser |
| 3 Schichten, je 20 Neuronen | ca. 90–95 % | Kein klarer Vorteil, ggf. etwas schlechter |

**Erklärung für stagnierende/schlechtere Ergebnisse bei größeren Netzen:**

Ab einer bestimmten Netzgröße beginnt das Modell, **Overfitting** zu zeigen: Es lernt Besonderheiten der Trainingsdaten auswendig, statt allgemeine Muster zu erkennen. Bei Cross-Validation fällt dies weniger stark auf als bei einem einfachen Train/Test-Split. Zusätzlich steigt die Trainingsdauer.

> Kernaussage für die SuS: „Mehr Neuronen ist nicht immer besser."

---

## D | Vergleich: Einzel-Neuron vs. neuronales Netz

**Aufgabe D1 – Erwartete Ergebnisse (ionosphere.tab)**

| Modell | Konfiguration | Typische Accuracy | Stärken | Schwächen |
|---|---|---|---|---|
| NN (Perzeptron-Modus) | kein Hidden Layer, Logistic | ca. 80–87 % | Einfach, schnell, interpretierbar | Nur lineare Entscheidungsgrenzen |
| Neural Network | 1 Schicht, 100 Neuronen, ReLU | ca. 93–96 % | Nicht-lineare Muster, flexibel | Weniger interpretierbar, Overfitting-Risiko |

> Hinweis: Beide Konfigurationen laufen im selben Neural Network-Widget – der Unterschied ist ausschließlich das Vorhandensein bzw. Fehlen der Hidden Layer. Das macht den Vergleich besonders anschaulich.

---

**Aufgabe D2 – Reflexionsfragen**

**1. Warum ist das neuronale Netz bei nicht-linear separierbaren Daten besser?**

Das neuronale Netz besitzt **versteckte Schichten** mit nichtlinearen Aktivierungsfunktionen (z. B. ReLU). Dadurch kann es **beliebig komplexe Entscheidungsgrenzen** erlernen, nicht nur Geraden. Das einfache Perzeptron hingegen bildet immer nur eine einzelne lineare Trennfläche ab.

**2. Welche Rolle spielen die Hidden Layers?**

Jede versteckte Schicht erlernt **abstraktere Repräsentationen** der Eingabedaten. Die erste Schicht erkennt einfache Muster (z. B. Merkmalskombinationen), spätere Schichten kombinieren diese zu komplexeren Strukturen. Erst durch diese Hierarchie können nichtlineare Zusammenhänge modelliert werden.

**3. Technische Anwendungsbeispiele (Erwartungshorizont, mehrere Möglichkeiten):**

- Erkennung von Defekten in Bauteilen (Bildverarbeitung / Qualitätssicherung)
- Vorhersage von Maschinenwartungsbedarf (Predictive Maintenance)
- Klassifikation von Vibrationssignalen (Schadenserkennung in Motoren)
- Erkennung handgeschriebener Zahlen auf Messgeräten (OCR)
- Klassifikation von Stromsignalen (Anomalieerkennung in elektrischen Netzen)

---

## E | Begriffssicherung – Musterlösungen

| Begriff | Erklärung |
|---|---|
| Perzeptron | Einfachstes künstliches Neuron: gewichtete Summe der Eingaben + Aktivierungsfunktion → Ausgabe; Grundbaustein neuronaler Netze |
| Aktivierungsfunktion | Funktion, die die gewichtete Summe der Eingaben in einen Ausgabewert umwandelt (z. B. Stufenfunktion, ReLU, Sigmoid); entscheidet, ob und wie stark ein Neuron „feuert" |
| Hidden Layer | Verdeckte Schicht zwischen Ein- und Ausgabeschicht; erlernt interne Repräsentationen der Daten; ermöglicht nichtlineare Klassifikation |
| Overfitting | Überanpassung: Das Modell lernt die Trainingsdaten „auswendig" und generalisiert schlecht auf neue Daten → hohe Trainings-, niedrige Testgenauigkeit |
| Accuracy | Anteil der korrekt klassifizierten Instanzen an der Gesamtzahl; Wert zwischen 0 und 1 (bzw. 0 % und 100 %) |

---

*Lösungshinweise | KIT | Technik | Jahrgangsstufe 12 | Berufliche Oberschule Bayern*
