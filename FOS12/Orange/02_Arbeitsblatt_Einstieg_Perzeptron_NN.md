# Arbeitsblatt: Neuronale Netze mit Orange
### KIT | Technik | Jahrgangsstufe 12 | Unterrichtseinheit 1 (90 min)

**Lernziele:** Sie können das Perzeptron-Modell in Orange nachbilden, einen Datensatz klassifizieren und den Einfluss von Trainingsparametern beobachten.

---

## A | Wiederholung: Das Perzeptron (15 min)

Beantworten Sie die folgenden Fragen in Stichpunkten:

**1.** Welche drei Bestandteile hat ein Perzeptron? Beschriften Sie die Skizze.

```
        w₁
  x₁ ──────┐
            │
        w₂  ├──► [ Σ ] ──► f(net) ──► ŷ
  x₂ ──────┘
            │
        w₃  │
  x₃ ──────┘
     (Bias)
```

*Beschriftungen:* `x₁, x₂` = \_\_\_\_\_\_\_\_ | `w₁, w₂` = \_\_\_\_\_\_\_\_ | `f(net)` = \_\_\_\_\_\_\_\_

---

**2.** Was versteht man unter der **Delta-Lernregel**? Ergänzen Sie die Lücken:

Das Gewicht wird um den Anteil **η · (y – ŷ) · xᵢ** angepasst, wobei:
- η (Eta) = \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ (Lernrate)
- y = \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ (tatsächlicher Wert)
- ŷ = \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ (Vorhersage des Modells)

---

**3.** Welche Art von Daten kann ein **einzelnes Perzeptron** korrekt klassifizieren?

☐ beliebige Daten  
☐ linear separierbare Daten  
☐ nur numerische Daten  

---

## B | Orange einrichten: Erster Workflow (20 min)

### Aufgabe B1 – Datensatz laden

Bauen Sie folgenden Workflow in Orange auf, indem Sie die Widgets per Drag & Drop auf das Canvas ziehen und verbinden:

```
[ File ] ──► [ Data Table ] ──► [ Scatter Plot ]
```

1. **File-Widget** öffnen → **„Browse documentation datasets"** → Datensatz **`iris.tab`** auswählen.
2. **Data Table** öffnen: Wie viele Zeilen und Spalten hat der Datensatz? 

   Zeilen: \_\_\_\_\_\_ | Spalten: \_\_\_\_\_\_ | Klassen (Zielwerte): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

3. **Scatter Plot** öffnen: Setzen Sie die Achsen auf `petal length` (x) und `petal width` (y).
   
   Sind die drei Klassen **linear separierbar**? Begründen Sie kurz:
   
   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

### Aufgabe B2 – Das Perzeptron in Orange (Add-on: Educational)

Erweitern Sie den Workflow um das Perzeptron-Widget:

```
[ File ] ──► [ Perceptron ] ──► [ Confusion Matrix ]
```

> Das Widget **„Perceptron"** finden Sie in der Kategorie **Educational** (linke Leiste).

1. Öffnen Sie das Perceptron-Widget. Welche Einstellungen können Sie vornehmen?

   ☐ Lernrate (Learning Rate)  ☐ Anzahl Schichten  ☐ Epochen (Max Iterations)  ☐ Aktivierungsfunktion

2. Starten Sie das Training mit den Standardwerten. Was zeigt die **Confusion Matrix**?

   | | vorhergesagt: Iris-setosa | vorhergesagt: Iris-versicolor | vorhergesagt: Iris-virginica |
   |---|---|---|---|
   | tatsächlich: Iris-setosa | | | |
   | tatsächlich: Iris-versicolor | | | |
   | tatsächlich: Iris-virginica | | | |

3. Wie hoch ist die **Klassifikationsgenauigkeit** (Accuracy)? \_\_\_\_\_\_\_\_ %

---

## C | Technischer Datensatz: Fehlerklassifikation (25 min)

Im Bereich Technik ist die **automatische Fehlererkennung** ein typisches Anwendungsfeld neuronaler Netze (z. B. Qualitätskontrolle in der Fertigung).

### Aufgabe C1 – Datensatz „ionosphere"

Laden Sie den Datensatz **`ionosphere.tab`** (Klassifikation von Radarsignalen: „good" vs. „bad").

> Dieser Datensatz enthält 34 Merkmale (Messwerte einer Radaranlage) und 351 Messpunkte.

Erstellen Sie folgenden Workflow:

```
[ File ] ──► [ Data Sampler ] ──► [ Neural Network ] ──► [ Test and Score ]
                                                    ▲
                                  [ File ] ──────────┘
```

> **Vereinfachung:** Nutzen Sie stattdessen Cross-Validation direkt im **„Test and Score"**-Widget.

**Vereinfachter Workflow:**

```
[ File ] ──► [ Test and Score ] ──► [ Confusion Matrix ]
                     ▲
            [ Neural Network ]
```

So verbinden Sie korrekt:
- **File** → Port „Data" von **Test and Score**
- **Neural Network** → Port „Learner" von **Test and Score**

---

### Aufgabe C2 – Neuronales Netz konfigurieren

1. Öffnen Sie das **Neural Network**-Widget. Notieren Sie die Standardkonfiguration:

   | Parameter | Standardwert | Ihre Einstellung (Aufgabe C3) |
   |---|---|---|
   | Hidden Layer Neurons | | |
   | Activation | | |
   | Max Iterations | | |
   | Regularization (α) | | |

2. Führen Sie die Auswertung durch. Notieren Sie die Ergebnisse aus **Test and Score**:

   | Metrik | Wert |
   |---|---|
   | Accuracy (CA) | |
   | AUC | |
   | F1-Score | |

---

### Aufgabe C3 – Einfluss der Netzarchitektur untersuchen

Verändern Sie die Netzarchitektur im Neural Network-Widget und notieren Sie jeweils die Accuracy:

| Hidden Layers / Neuronen | Accuracy (CA) | Beobachtung |
|---|---|---|
| 1 Schicht, 10 Neuronen | | |
| 1 Schicht, 100 Neuronen | | |
| 2 Schichten, je 50 Neuronen | | |
| 3 Schichten, je 20 Neuronen | | |

**Frage:** Ab welcher Netzgröße beobachten Sie keine weitere Verbesserung oder sogar eine Verschlechterung? Was könnte die Ursache sein?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## D | Vergleich: Perzeptron vs. neuronales Netz (15 min)

### Aufgabe D1 – Beide Modelle im direkten Vergleich

Ergänzen Sie den Workflow, sodass **Perceptron** und **Neural Network** gleichzeitig ausgewertet werden:

```
[ File ] ──► [ Test and Score ] ──► [ Confusion Matrix ]
                  ▲        ▲
      [ Perceptron ]    [ Neural Network ]
```

Tragen Sie die Ergebnisse ein:

| Modell | Accuracy | Stärken | Schwächen |
|---|---|---|---|
| Perzeptron | | | |
| Neural Network | | | |

---

### Aufgabe D2 – Reflexion

Beantworten Sie folgende Fragen in vollständigen Sätzen:

1. Warum erzielt das neuronale Netz bei nicht-linear separierbaren Daten bessere Ergebnisse als das Perzeptron?

   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

2. Welche Rolle spielen die **versteckten Schichten** (Hidden Layers) im neuronalen Netz?

   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

3. Nennen Sie ein weiteres technisches Anwendungsbeispiel, bei dem ein neuronales Netz sinnvoll eingesetzt werden könnte:

   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## E | Sicherung & Ergebnissicherung (15 min)

- Speichern Sie Ihren fertigen Orange-Workflow: **Datei → Speichern unter** → `KIT_Neuronale_Netze_<IhrName>.ows`
- Machen Sie einen **Screenshot** der Confusion Matrix und fügen Sie ihn in Ihr Heft/Portfolio ein.

### Zusammenfassung der heutigen Stunde – ergänzen Sie:

| Begriff | Erklärung (eigene Worte) |
|---|---|
| Perzeptron | |
| Aktivierungsfunktion | |
| Hidden Layer | |
| Overfitting | |
| Accuracy | |

---

### Verwendete Datensätze heute:
- **`iris.tab`** – Klassifikation von Blumenarten (eingebettet in Orange)
- **`ionosphere.tab`** – Radarsignal-Klassifikation (eingebettet in Orange)

---

*KIT | Technik | Jahrgangsstufe 12 | Berufliche Oberschule Bayern*
