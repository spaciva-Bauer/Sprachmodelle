# Lösungshinweise: Neuronale Netze – Vertiefung
### KIT | Technik | Jahrgangsstufe 12 | Unterrichtseinheit 2 – NUR FÜR LEHRKRÄFTE

---

## A | Einstieg: Trainingsdaten und ihre Qualität

**Aufgabe A1 – Gedankenexperiment: Datensatz-Beurteilung**

| Datensatz | Geeignet? | Begründung |
|---|---|---|
| A | ❌ Nein | **Klassenungleichgewicht (class imbalance):** 99,5 % der Daten zeigen keinen Ausfall. Das Modell lernt, stets „kein Ausfall" vorherzusagen und erreicht trotzdem 99,5 % Accuracy – erkennt aber echte Ausfälle nicht. |
| B | ⚠️ Bedingt | Ausgewogene Verteilung ist gut; aber nur ein Maschinentyp → schlechte Generalisierbarkeit auf andere Maschinen |
| C | ✅ Ja | Großer, ausgewogener Datensatz aus verschiedenen Maschinentypen → beste Generalisierbarkeit |
| D | ❌ Nein | Zu wenige Daten (1.000) und nur ein einziger Tag → kein repräsentatives Abbild möglicher Betriebszustände, Gefahr der Überanpassung |

**Frage: Problem mit Datensatz A**

Das Problem heißt **Klassenungleichgewicht** (class imbalance). Ein Modell, das immer „kein Ausfall" vorhersagt, erreicht 99,5 % Accuracy – obwohl es vollständig nutzlos ist, da echte Ausfälle nicht erkannt werden. Die Accuracy als Metrik ist bei unbalancierten Daten irreführend; hier wären **Recall, Precision oder F1-Score** deutlich aussagekräftiger.

> Didaktischer Hinweis: Dieses Phänomen lässt sich hervorragend mit dem Digits-Datensatz demonstrieren, indem man eine Klasse künstlich unterrepräsentiert.

---

**Aufgabe A2 – Begriffe zuordnen**

| Begriff | Zugehörige Definition |
|---|---|
| Überanpassung (Overfitting) | Das Modell lernt die Trainingsdaten auswendig und versagt bei neuen Daten. |
| Unteranpassung (Underfitting) | Das Modell ist zu simpel, um Muster zu erkennen – schlechte Ergebnisse bei Trainings- **und** Testdaten. |
| Trainings-/Testdaten-Aufteilung | Ein Teil der Daten wird nur zur Evaluation verwendet, nicht zum Training. |
| Kreuzvalidierung (Cross-Validation) | Daten werden mehrfach in verschiedene Blöcke geteilt, jeder Block dient einmal als Testmenge. |

---

## B | Vertiefung mit technischen Datensätzen

**Aufgabe B1 – Regression: Gebäude-Energieverbrauch**

*Hinweis zu den Datensätzen:*
- **ENB2012:** 768 Instanzen, 8 Features (Wandfläche, Dachfläche, Verglasungsanteil etc.), Zielgröße Y1 = Heizlast in kWh/m². Herunterladen unter https://archive.ics.uci.edu/dataset/242/energy+efficiency und als `.csv` in Orange über das File-Widget laden.
- **housing.tab** (Alternative, direkt eingebettet): Boston-Housing-Daten, Zielgröße = Mietpreis in USD. Weniger technischer Bezug, aber sofort verfügbar.

**Typische Regressionsergebnisse (ENB2012, Neural Network `100,50`, ReLU, 5-fache CV):**

| Metrik | Typischer Wert (ENB2012) | Typischer Wert (housing.tab) |
|---|---|---|
| MAE | ca. 1,5–2,5 kWh/m² | ca. 2,5–4,0 |
| RMSE | ca. 2,5–4,0 kWh/m² | ca. 3,5–6,0 |
| R² | ca. 0,97–0,99 | ca. 0,85–0,92 |

> ENB2012 ist für neuronale Netze sehr gut geeignet; die hohen R²-Werte sind realistisch und motivierend. housing.tab liefert etwas schwächere, aber immer noch gute Ergebnisse.

**Interpretation R²:**
Ein R² von z. B. 0,98 bedeutet, dass das Modell **98 % der Varianz** in den Heizlastdaten erklären kann – nur 2 % der Schwankungen bleiben unerklärt.

---

**Aufgabe B2 – Visualisierung: Vorhersage vs. Realität**

**Ideales Modell im Scatter Plot:**
Alle Punkte liegen auf einer **Winkelhalbierenden** (45°-Gerade durch den Ursprung). Das bedeutet: Vorhersage = tatsächlicher Wert. Je stärker die Punktewolke um diese Gerade streut, desto schlechter das Modell.

**Ausreißer – mögliche Ursachen:**
- Messpunkte mit ungewöhnlicher Merkmalskombination (z. B. sehr große Glasfläche + schlechte Dämmung)
- Datenfehler in der ursprünglichen Messung
- Gebäudetypen, die im Training unterrepräsentiert waren
- Nichtlineare Effekte, die das Modell nicht vollständig erfasst hat

---

**Aufgabe B3 – Über- und Unteranpassung sichtbar machen**

**Erwartete Tendenzen (ENB2012, 80/20-Split):**

| Modellgröße | R² Training (ca.) | R² Test (ca.) | Diagnose |
|---|---|---|---|
| 1 Schicht, 5 Neuronen | 0,75–0,85 | 0,70–0,82 | ☑ Underfitting – Netz zu klein für den Datensatz |
| 1 Schicht, 50 Neuronen | 0,95–0,98 | 0,94–0,97 | ☑ Gut – gute Balance |
| 2 Schichten, 200+100 | 0,98–0,99 | 0,96–0,98 | ☑ Gut bis leichtes Overfitting |
| 3 Schichten, 500+300+200 | 0,99+ | 0,90–0,96 | ☑ Overfitting – Trainings-R² deutlich besser als Test-R² |

> Hinweis: Die Werte variieren je nach Zufalls-Split. Wichtig ist das **relative Muster**, nicht absolute Zahlen. Es empfiehlt sich, den Seed im Data Sampler zu fixieren (z. B. 42), damit alle SuS vergleichbare Ergebnisse erhalten.

**Erkennung von Overftting:**
Overfitting erkennt man daran, dass R² (Trainingsdaten) **deutlich höher** ist als R² (Testdaten). Das Modell hat die Trainingsdaten „auswendig gelernt", kann aber nicht auf neue Daten generalisieren.

---

## C | Klassifikation: Ziffern- und Mustererkennung

**Aufgabe C1 – Digits-Datensatz**

1. **Anzahl Bilder:** 1.797 | **Features pro Bild:** 64 (= 8 × 8 Pixel, Grauwerte 0–16)

2. **Typische Accuracy** mit Neural Network `100, 50`, ReLU, 10-fache CV: ca. **97–98 %**

3. **Häufigste Verwechslungen** (typisch, variiert leicht je nach Split):

   - Ziffer **3** ↔ **8** (ähnliche Kurvenstruktur)
   - Ziffer **4** ↔ **9** (ähnliche obere Hälfte)
   - Ziffer **1** ↔ **7** (bei schlechter Handschrift)

   > Tipp für die Klasse: Die Verwechslungen im 8×8-Raster sind leicht nachvollziehbar, wenn man sich die Bilder im Image Viewer ansieht – eine gute Diskussionsgrundlage.

4. **Plausibilität der Verwechslungen:**
   Ziffern wie 3 und 8 teilen viele strukturelle Merkmale auf Pixel-Ebene (geschwungene Linien, ähnliche Belegung der Rasterzellen). Bei niedriger Auflösung (8×8) sind die Unterschiede minimal. Das Modell reagiert auf Pixelmuster, nicht auf semantische Bedeutung.

---

**Aufgabe C2 – Feature-Relevanz (Rank-Widget)**

Das Rank-Widget bewertet Features nach statistischen Kriterien (z. B. Information Gain, ReliefF).

**Erwartetes Ergebnis:**
Die wichtigsten Pixel liegen typischerweise **in der Mitte** des 8×8-Rasters (Zeilen 3–6, Spalten 3–6), da dort die meisten Unterschiede zwischen den Ziffern auftreten. Randpixel (z. B. `pixel_1_1`, `pixel_8_8`) sind oft weniger informativ, da die meisten Ziffern dort kaum Tinte haben.

> Tipp: Das Rank-Widget zeigt je nach gewähltem Kriterium unterschiedliche Ranglisten. ReliefF oder Information Gain sind für Klassifikationsaufgaben gut geeignet.

**Interpretation:**
Pixel in der Bildmitte sind informativer, weil dort die charakteristischen Kurven und Striche der Ziffern verlaufen. Ecken und Ränder des 8×8-Fensters sind bei handgeschriebenen Ziffern meist leer (Hintergrund).

---

## D | Qualität der Trainingsdaten – Datenreduktion

**Aufgabe D1 – Bewusste Datenreduktion (Digits-Datensatz)**

**Erwartete Ergebnisse (Neural Network `100, 50`, 10-fache CV):**

| Trainingsanteil | Tatsächliche Trainingsinstanzen (ca.) | Erwartete Accuracy |
|---|---|---|
| 10 % | ~180 Bilder | ca. 80–88 % |
| 30 % | ~540 Bilder | ca. 92–95 % |
| 70 % | ~1.260 Bilder | ca. 96–97 % |
| 90 % | ~1.620 Bilder | ca. 97–98 % |

**Schlussfolgerung:**
Ein deutlicher Qualitätsabfall tritt typischerweise **unter ca. 30 %** der Daten auf. Ab ~70 % nähert sich die Accuracy dem Maximum an – weitere Datenzugaben bringen noch geringe Verbesserungen, aber mit deutlich abnehmendem Ertrag.

> Didaktisch wertvoll: Dieses Experiment zeigt das Konzept der **Lernkurve** – ein zentrales Werkzeug zur Diagnose von Datenmengen-Problemen.

---

## E | Reflexion und Transfer

**Aufgabe E1 – Musterlösung: Eigenes Szenario**

Nachfolgend ein Beispiel-Szenario als Orientierung für die Bewertung:

**Szenario:** Vorhersage der Restlebensdauer von Schneidwerkzeugen (Tool Wear Prediction)

| Aspekt | Beispiellösung |
|---|---|
| Eingabe-Features (x) | Schnittkraft, Vibrationsamplitude, Temperatur, Bearbeitungszeit, Drehzahl |
| Zielgröße (y) | Verbleibende Nutzungsdauer in Minuten (Regression) oder Klasse „gut / verschlissen" (Klassifikation) |
| Typ | Regression oder binäre Klassifikation |
| Geeignete Metrik | Regression: RMSE, R² | Klassifikation: F1-Score (da Fehlklassifikation eines verschlissenen Werkzeugs teuer ist) |
| Fehlerquellen Trainingsdaten | Messfehler der Sensoren, unterschiedliche Materialien, Werkzeugchargen, fehlende Beschriftung des Verschleißzustands |
| Risiko Over-/Underfitting | Bei wenigen Trainingsdaten (Werkzeugwechsel selten) → Underfitting; bei sehr tiefem Netz und kleinem Datensatz → Overfitting |

> Bewertungshinweis: Lösungen müssen nicht exakt diesem Beispiel entsprechen. Zentral ist, dass Features und Zielgröße plausibel zusammenpassen und die Metrikwahl zum Problem passt.

---

**Aufgabe E2 – Kritische Fragen**

**1. Reicht 98 % Accuracy für den Produktionseinsatz?**

**Nein – nicht ohne weitere Analyse.** Entscheidend ist:
- Wie häufig treten Ausfälle überhaupt auf? Bei 1 % Ausfallrate liefert ein Modell, das stets „kein Ausfall" sagt, bereits 99 % Accuracy – ohne je einen Ausfall erkannt zu haben.
- Welche Konsequenzen hat ein **falsch negativer** Alarm (Ausfall nicht erkannt)? In der Produktion kann das sehr teuer oder gefährlich sein.
- Zuverlässigkeit, Reaktionszeit und Erklärbarkeit des Modells sind im Industrieeinsatz oft wichtiger als reine Accuracy.

**2. Warum reicht Accuracy allein nicht aus?**

Bei **unbalancierten Klassen** oder wenn die Kosten von Fehlern asymmetrisch sind, ist Accuracy irreführend. Beispiele:

- **Medizintechnik / Qualitätssicherung:** Ein Defekt-Erkennungssystem, das 99 % Accuracy hat, aber 50 % aller Defekte übersieht, ist gefährlich → **Recall** wichtiger
- **Spam-Filter:** Jede echte E-Mail als Spam zu klassifizieren, wäre sehr störend → **Precision** wichtiger
- **Allgemein:** Bei 10 Klassen mit je unterschiedlicher Häufigkeit ist der **F1-Score (makro)** aussagekräftiger
- **AUC (ROC-Kurve)** ist besonders wichtig, wenn der Entscheidungsschwellwert variabel sein soll

> Kernbotschaft: Die Wahl der Metrik muss vom **Verwendungszweck und den Fehlerkosten** abhängen, nicht nur von der Datenlage.

---

## Zusatzhinweise für die Lehrkraft

### Zum ENB2012-Datensatz
Falls der Download über das UCI-Repository Probleme bereitet: Die Datei ist auch auf Kaggle verfügbar. Als Alternative eignet sich `housing.tab` (direkt in Orange), wobei der Technikbezug geringer ist. Der Datensatz `autompg.tab` (Kraftstoffverbrauch, direkt eingebettet) ist ebenfalls eine gute Regression-Alternative mit technischem Bezug.

### Zur Reproduzierbarkeit
Neuronale Netze haben eine zufällige Initialisierung. Für vergleichbare Ergebnisse im Unterricht:
- Im Neural Network-Widget → **Random seed** auf einen festen Wert setzen (z. B. 42)
- Im Data Sampler → **Fixed seed** aktivieren

### Zeitplanung
Die Aufgaben B3 (Overfitting-Tabelle) und D1 (Datenreduktion) können je nach Klasse zeitintensiv sein. Empfehlung: B3 oder D1 als **Hausaufgabe oder Partneraufgabe** auslagern.

---

*Lösungshinweise | KIT | Technik | Jahrgangsstufe 12 | Berufliche Oberschule Bayern*
