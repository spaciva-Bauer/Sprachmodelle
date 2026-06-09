# Arbeitsblatt: Neuronale Netze – Vertiefung
### KIT | Technik | Jahrgangsstufe 12 | Unterrichtseinheit 2 (90 min)

**Lernziele:** Sie analysieren Trainingsqualität, erkennen Über- und Unteranpassung, wählen technisch geeignete Datensätze aus und interpretieren Modellgüte differenziert mit verschiedenen Metriken.

---

## A | Einstieg: Trainingsdaten und ihre Qualität (15 min)

### Aufgabe A1 – Gedankenexperiment

Ein Ingenieur möchte ein neuronales Netz trainieren, das aus Sensordaten vorhersagt, ob eine Maschine in den nächsten 24 Stunden ausfallen wird (**Predictive Maintenance**).

Beurteilen Sie die folgenden Trainingsdatensätze:

| Datensatz | Beschreibung | Geeignet? | Begründung |
|---|---|---|---|
| A | 10.000 Messungen, davon 9.950 „kein Ausfall", 50 „Ausfall" | | |
| B | 5.000 Messungen, gleichmäßig verteilt, aus einem Maschinentyp | | |
| C | 20.000 Messungen, 5 verschiedene Maschinentypen, gleich verteilt | | |
| D | 1.000 Messungen aus einem einzigen Produktionstag | | |

**Frage:** Was ist das Problem mit Datensatz A, obwohl er viele Daten enthält?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

### Aufgabe A2 – Begriffe klären

Ordnen Sie die Begriffe den Definitionen zu:

| Begriff | Definition |
|---|---|
| Überanpassung (Overfitting) | |
| Unteranpassung (Underfitting) | |
| Trainings-/Testdaten-Aufteilung | |
| Kreuzvalidierung (Cross-Validation) | |

*Definitionen (zum Zuordnen):*
- Das Modell lernt die Trainingsdaten auswendig und versagt bei neuen Daten.
- Das Modell ist zu simpel, um Muster zu erkennen – schlechte Ergebnisse bei Trainings- **und** Testdaten.
- Daten werden mehrfach in verschiedene Blöcke geteilt, jeder Block dient einmal als Testmenge.
- Ein Teil der Daten wird nur zur Evaluation verwendet, nicht zum Training.

---

## B | Vertiefung mit technischen Datensätzen (35 min)

### Aufgabe B1 – Energieverbrauch von Gebäuden (Regression)

> **Datensatz:** Laden Sie die Datei **`ENB2012_data.csv`** herunter (UCI Machine Learning Repository) oder nutzen Sie den eingebetteten Datensatz **`housing.tab`** als Alternative.
>
> **Hintergrund:** Der ENB2012-Datensatz enthält 8 bauphysikalische Merkmale von Gebäuden (z. B. Wandfläche, Dachfläche, Verglasungsanteil) und die gemessene Heizlast (Y1) sowie Kühllast (Y2). Ziel: Regression – Vorhersage der Heizlast.

**Workflow aufbauen:**

```
[ File ]
   │
   ▼
[ Data Sampler ] ─── (70% Training) ──► [ Neural Network ] ──► [ Predictions ]
        │                                                              ▲
        └───── (30% Test) ──────────────────────────────────────────►─┘
                                                                       │
                                                                  [ Scatter Plot ]
                                                             (vorhergesagt vs. tatsächlich)
```

> **Vereinfachung:** Nutzen Sie **Test and Score** mit Cross-Validation (k=5).

**Empfohlener Workflow:**
```
[ File ] ──► [ Test and Score ] ──► [ Predictions ] ──► [ Scatter Plot ]
                    ▲
           [ Neural Network ]
```

Konfigurieren Sie das Neural Network für **Regression** (Orange erkennt den Zieltyp automatisch):
- Hidden Layers: `100, 50`
- Activation: **ReLU**
- Max Iterations: 200

Tragen Sie die Regressionsergebnisse ein:

| Metrik | Wert | Bedeutung |
|---|---|---|
| MAE (Mean Absolute Error) | | Durchschnittlicher absoluter Fehler in [kWh/m²] |
| RMSE (Root Mean Squared Error) | | |
| R² (Bestimmtheitsmaß) | | Wert zwischen 0 und 1; 1 = perfekte Vorhersage |

**Interpretation:** Ein R² von \_\_\_\_\_ bedeutet, dass das Modell \_\_\_\_\_ % der Varianz in den Heizlastdaten erklären kann.

---

### Aufgabe B2 – Visualisierung: Vorhersage vs. Realität

1. Verbinden Sie **Predictions** mit einem **Scatter Plot**.
2. Setzen Sie auf der x-Achse den tatsächlichen Zielwert, auf der y-Achse den vorhergesagten.
3. Beschreiben Sie, was ein **ideales Modell** im Scatter Plot zeigen würde:

   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

4. Identifizieren Sie **Ausreißer** im Diagramm. Was könnte deren Ursache sein?

   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

### Aufgabe B3 – Über- und Unteranpassung sichtbar machen

Verwenden Sie denselben Datensatz (Regression). Variieren Sie die Modellgröße und notieren Sie getrennte Ergebnisse für **Trainings- und Testdaten**:

> Um separate Train/Test-Scores zu sehen: Im **Test and Score**-Widget → Reiter „Evaluation Results" → wählen Sie „Leave One Out" oder vergleichen Sie manuell mit **Data Sampler** (80/20-Split).

| Modellgröße | R² (Trainingsdaten) | R² (Testdaten) | Diagnose |
|---|---|---|---|
| 1 Schicht, 5 Neuronen | | | ☐ Underfitting  ☐ Gut  ☐ Overfitting |
| 1 Schicht, 50 Neuronen | | | ☐ Underfitting  ☐ Gut  ☐ Overfitting |
| 2 Schichten, 200+100 | | | ☐ Underfitting  ☐ Gut  ☐ Overfitting |
| 3 Schichten, 500+300+200 | | | ☐ Underfitting  ☐ Gut  ☐ Overfitting |

**Frage:** Woran erkennt man Überanpassung in der obigen Tabelle?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## C | Klassifikation: Ziffern- und Mustererkennung (20 min)

### Aufgabe C1 – Digits-Datensatz (Bilderkennung)

> **Datensatz:** Die Datei `digits_8x8.tab` wurde von Ihrer Lehrkraft vorbereitet und bereitgestellt (handgeschriebene Ziffern, 8×8 Pixel = 64 Features, 10 Klassen: 0–9). Laden Sie sie über das **File-Widget**.
>
> **Technischer Bezug:** Optische Zeichenerkennung (OCR) wird in der Industrie zur automatischen Erfassung von Seriennummern, Messwerten auf Anzeigen und Barcodes eingesetzt.

**Workflow:**
```
[ File ] ──► [ Test and Score ] ──► [ Confusion Matrix ]
                   ▲        ▲
       [ Neural Network ] [ Logistic Regression ] (Vergleich)
```

1. Wie viele Bilder enthält der Datensatz? \_\_\_\_\_\_ | Wie viele Features pro Bild? \_\_\_\_\_\_

2. Trainieren Sie ein Neural Network mit `100, 50` Neuronen in zwei versteckten Schichten.

3. Füllen Sie die **Confusion Matrix** (gekürzt) aus:

   > Notieren Sie, welche **Ziffer am häufigsten verwechselt** wird und mit welcher:

   Häufigste Verwechslung: Ziffer \_\_\_\_\_ wird verwechselt mit Ziffer \_\_\_\_\_ (\_\_\_\_\_ mal)

4. Warum ist es plausibel, dass gerade diese Ziffern verwechselt werden?

   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

### Aufgabe C2 – Feature-Relevanz analysieren

1. Fügen Sie das Widget **„Rank"** (Kategorie: Data) zwischen Datensatz und Modell ein:

   ```
   [ File ] ──► [ Rank ] ──► [ Test and Score ]
   ```

2. Welche Features (Pixel-Positionen) haben die höchste Relevanz für die Klassifikation?

   Top-3-Features: \_\_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_\_

3. Interpretieren Sie: Welche Bereiche eines 8×8-Ziffernbildes sind besonders informativ?
   (Hinweis: Feature `pixel_1_1` = oben links, `pixel_8_8` = unten rechts)

   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## D | Vertiefung: Qualität der Trainingsdaten (10 min)

### Aufgabe D1 – Bewusste Datenreduktion

Verwenden Sie den **Data Sampler**, um nur einen **Bruchteil der Digits-Daten** zu trainieren:

```
[ File ] ──► [ Data Sampler ] ──► [ Test and Score ] ──► [ Confusion Matrix ]
                                          ▲
                                 [ Neural Network ]
```

Im **Data Sampler**: Samplingrate variieren.

| Trainingsanteil | Accuracy | Beobachtung |
|---|---|---|
| 10 % | | |
| 30 % | | |
| 70 % | | |
| 90 % | | |

**Schlussfolgerung:** Ab welchem Trainingsanteil wird die Qualität deutlich schlechter?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## E | Reflexion und Transfer (10 min)

### Aufgabe E1 – Eigenes Anwendungsszenario entwickeln

Wählen Sie ein technisches Szenario aus der Industrie oder Technik und planen Sie den Einsatz eines neuronalen Netzes:

**Szenario:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

| Aspekt | Ihre Planung |
|---|---|
| Eingabe-Features (x) | |
| Zielgröße (y) | |
| Typ: Klassifikation oder Regression? | |
| Geeignete Metrik zur Bewertung | |
| Mögliche Fehlerquellen bei den Trainingsdaten | |
| Risiko: Über- oder Unteranpassung? Warum? | |

---

### Aufgabe E2 – Kritische Fragen zur KI-Anwendung in der Technik

Diskutieren Sie kurz in Partnerarbeit und notieren Sie Ihre Antwort:

1. Ein neuronales Netz zur Maschinenüberwachung erreicht 98 % Accuracy. Ist das ausreichend für den Produktionseinsatz?

   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

2. Warum reicht Accuracy als einzige Metrik oft nicht aus? Nennen Sie ein Beispiel, bei dem F1-Score oder AUC wichtiger ist:

   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## Anhang: Verwendete Datensätze und Quellen

| Datensatz | Herkunft | Beschreibung | Typ |
|---|---|---|---|
| `housing.tab` | Orange (eingebettet) | Boston Housing-Daten (Mietpreise) | Regression |
| `ENB2012_data.csv` | UCI ML Repository | Gebäude-Energieverbrauch | Regression |
| `digits_8x8.tab` | UCI ML Repository (von Lehrkraft vorbereitet) | Handgeschriebene Ziffern 0–9, 8×8px | Klassifikation |
| `ionosphere.tab` | Orange (eingebettet) | Radarsignal-Klassifikation | Klassifikation |

### Empfohlene weitere Datensätze (für eigenständige Erkundung):

- **`autompg.tab`** (Orange, eingebettet): Kraftstoffverbrauch von Fahrzeugen → Regression
- **`heart_disease.tab`** (Orange, eingebettet): Herzerkrankung → Klassifikation (Medizintechnik-Bezug)
- **UCI: Wine Quality** (https://archive.ics.uci.edu/dataset/186): Qualitätskontrolle → Regression/Klassifikation

---

### Kompetenz-Check: Beurteilen Sie sich selbst

| Kompetenz | ☐ sicher | ☐ teilweise | ☐ noch unsicher |
|---|---|---|---|
| Ich kann in Orange einen Klassifikations-Workflow aufbauen | | | |
| Ich kann in Orange einen Regressions-Workflow aufbauen | | | |
| Ich erkenne Overfitting an Train/Test-Metriken | | | |
| Ich interpretiere Confusion Matrix und R² korrekt | | | |
| Ich kann den Einfluss der Trainingsdatenmenge beurteilen | | | |

---

*KIT | Technik | Jahrgangsstufe 12 | Berufliche Oberschule Bayern*
