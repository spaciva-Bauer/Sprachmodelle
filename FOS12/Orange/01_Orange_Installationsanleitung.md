# Orange – Installationsanleitung für Lehrkräfte (Windows)

**Software:** Orange Data Mining  | **Stand:** Juni 2026

## 1. Was ist Orange?

Orange ist eine Open-Source-Software für visuelle Datenanalyse und maschinelles Lernen. Workflows werden durch Verbinden von grafischen Bausteinen (sog. *Widgets*) erstellt – ohne Programmierkenntnisse. Orange eignet sich hervorragend für den Unterricht zu neuronalen Netzen, da Modelle interaktiv konfiguriert, trainiert und visualisiert werden können.

## 2. Systemvoraussetzungen

| Anforderung | Minimum |
| - | - |
| Betriebssysteme | Windows, macOS, ... |
| RAM | 4 GB (empfohlen: 8 GB) |
| Speicherplatz | ca. 1,5 GB |
| Internetzugang | für Installation und Add-ons erforderlich |
| Administratorrechte | für die Standardinstallation erforderlich |


> **Hinweis für schulische Umgebungen:** Falls keine Administratorrechte zur Verfügung stehen, kann Orange auch ohne Admin-Rechte installiert werden (siehe Abschnitt 4).

## 3. Standardinstallation (mit Administratorrechten)

### Schritt 1: Installer herunterladen

1. Öffnen Sie die offizielle Website: \*\*[https://orangedatamining.com/download/\*\*](https://orangedatamining.com/download/)

2. Klicken Sie auf **„Download Orange"** (Windows-Version, .exe-Installer).

3. Speichern Sie die Datei in einem lokalen Ordner (z. B. `Downloads`).

### Schritt 2: Installation durchführen

1. Doppelklicken Sie auf die heruntergeladene `.exe`-Datei.

2. Bestätigen Sie die UAC-Nachfrage (Administratorrechte) mit **„Ja"**.

3. Wählen Sie im Installer:

   - **Installationspfad** (Standard: `C:\Users\<Benutzername\>\AppData\Local\Orange3` oder `C:\Program Files\Orange3`)

   - **„Install for all users"** (empfohlen an Schulrechnern, falls Admin-Rechte vorhanden)

4. Klicken Sie auf **„Install"** und warten Sie ca. 3–5 Minuten.

5. Nach Abschluss: **„Finish"** klicken. Orange startet automatisch.

### Schritt 3: Erste Programmöffnung

- Orange öffnet sich mit einem leeren Canvas (Arbeitsfläche).

- Links befindet sich die **Widget-Leiste**, rechts das **Workflow-Canvas**.

- Beim ersten Start erscheint ggf. ein Willkommensdialog – dieser kann geschlossen werden.

## 4. Installation ohne Administratorrechte (Portable-Variante)

Falls auf Schulrechnern keine Admin-Rechte vorhanden sind:

1. Laden Sie den **Miniconda-Installer** herunter: [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)

2. Installieren Sie Miniconda **„Just for me"** (kein Admin erforderlich).

3. Öffnen Sie die **Anaconda Prompt** (wird mit Miniconda installiert).

4. Geben Sie folgenden Befehl ein und bestätigen Sie mit Enter:

```
conda create -n orange3 python=3.10      
conda activate orange3      
pip install orange3      
python -m Orange.canvas
```

1. Orange startet nun im Browser-ähnlichen Modus.

> **Alternative:** Fragen Sie Ihre IT-Administration, ob Orange zentral über ein Software-Deployment-System (z. B. Microsoft Intune, OPSI) ausgerollt werden kann.

## 5. Empfohlene Add-ons installieren

Für den Unterricht zu neuronalen Netzen ist das Add-on **„Explain"** sowie **„Educational"** besonders wichtig.

### Installation über die Benutzeroberfläche:

1. Orange öffnen.

2. Menü: **Options → Add-ons…**

3. Im Dialog erscheint eine Liste verfügbarer Erweiterungen.

4. Folgende Add-ons auswählen (Häkchen setzen):

   - ☑ **Educational** – interaktive Lernwidgets (Perzeptron-Visualisierung!)

   - ☑ **Explain** – Erklärbarkeit von Modellen (optional, aber empfehlenswert)

5. Klicken Sie auf **„OK"** und warten Sie, bis die Installation abgeschlossen ist.

6. Orange neu starten.

> **Wichtig:** Die Add-on-Installation benötigt einen aktiven Internetzugang.

## 6. Mitgelieferte Datensätze finden

Orange enthält bereits eine Reihe eingebetteter Datensätze, die ohne eigene Dateien genutzt werden können.

**Zugang über das Widget „File":**

1. Widget **„File"** auf das Canvas ziehen.

2. Doppelklicken → im Dateidialog auf das **Ordner-Symbol** klicken.

3. Oben in der Liste erscheint **„Browse documentation datasets"** – hier sind alle mitgelieferten Datensätze aufgelistet.

**Relevante eingebettete Datensätze für den Unterricht:**

| Datensatz | Typ | Einsatz |
| - | - | - |
| `iris.tab` | Klassifikation | Einstieg, linear separierbar |
| `housing.tab` | Regression | Regression mit neuronalem Netz |
| `zoo.tab` | Klassifikation | Mehrklassen-Problem |
| `titanic.tab` | Klassifikation | Feature-Relevanz, Überanpassung |


## 7. Nützliche Einstellungen für den Unterrichtseinsatz

- **Sprache:** Orange ist auf Englisch – Fachbegriffe können mit dem Lernmaterial verknüpft werden.

- **Canvas-Zoom:** `Strg + Mausrad` zum Zoomen; `Strg + Shift + H` für „Fit to screen".

- **Workflow speichern:** `Strg + S` → `.ows`-Datei (Orange Workflow). Diese Datei kann an Schülerinnen und Schüler verteilt werden.

- **Workflow als Vorlage:** Erstellen Sie Workflows mit fehlenden Verbindungen – die SuS vervollständigen diese im Unterricht.

## 8. Fehlerbehebung

| Problem | Lösung |
| - | - |
| Orange startet nicht | Antivirenprogramm prüfen; Orange ggf. als Ausnahme hinzufügen;  **Smart App Control unter Windows 11 ggf. deaktivieren** |
| Add-ons lassen sich nicht installieren | Proxy-Einstellungen der Schule prüfen; ggf. IT fragen |
| Workflow öffnet sich leer | Überprüfen, ob das passende Add-on installiert ist |
| Langsame Performance | RAM schließen; keine anderen Programme parallel öffnen |


## 8b. Datensatz `digits_8x8.tab` vorbereiten (für Unterrichtseinheit 2)

Für das Arbeitsblatt zur Vertiefung (Unterrichtseinheit 2, Abschnitte C und D) wird ein Datensatz mit handgeschriebenen Ziffern benötigt. Dieser liegt nicht direkt in Orange vor und muss einmalig erzeugt und bereitgestellt werden.

### Voraussetzung

Python mit scikit-learn muss auf dem Rechner verfügbar sein. Bei einer bestehenden Orange-Installation ist Python bereits vorhanden. scikit-learn ist ebenfalls Teil der Orange-Umgebung.

### Skript ausführen

1. Öffnen Sie die **Eingabeaufforderung** (cmd) oder **PowerShell** und navigieren Sie in einen geeigneten Ordner, z. B.:

```
cd C:\Users\<IhrName\>\Desktop
```

2. Speichern Sie folgendes Skript als `digits.py` und führen Sie es unter Python aus:


Inhalt von `digits.py`:

```
from sklearn.datasets import load_digits
import pandas as pd

digits = load_digits()

col_names = [f"pixel_{i}" for i in range(64)] + ["digit"]
types     = ["continuous"] * 64 + ["discrete"]
roles     = ["feature"]    * 64 + ["class"]

df = pd.DataFrame(digits.data, columns=col_names[:64])
df["digit"] = digits.target.astype(str)

# Orange .tab-Format: drei Kopfzeilen (Name / Typ / Rolle)
with open("digits_8x8.tab", "w", encoding="utf-8") as f:
    f.write("\t".join(col_names) + "\n")
    f.write("\t".join(types)     + "\n")
    f.write("\t".join(roles)     + "\n")
    df.to_csv(f, sep="\t", index=False, header=False)

print(f"Fertig: {len(df)} Instanzen, Ziel: digit")
```

3. Die Datei `digits_8x8.tab` befindet sich nun im aktuellen Ordner.

### Datei bereitstellen

Verteilen Sie `digits_8x8.tab` an die SuS, z. B. über:

- Freigegebenen Netzwerkordner

- Moodle-Kurs (als Dateidownload)

- USB-Stick

Die SuS laden die Datei in Orange über das **File-Widget** → Ordner-Symbol → Datei auswählen. Orange erkennt das `.tab`-Format direkt; die Zielspalte `digit` wird automatisch als kategorische Variable erkannt.

- **Offizielle Dokumentation:** [https://orangedatamining.com/docs/](https://orangedatamining.com/docs/)

- **YouTube-Kanal (Orange Data Mining):** https://www.youtube.com/@OrangeDataMining

- **Tutorials:** [https://orangedatamining.com/blog/](https://orangedatamining.com/blog/) (viele bebilderte Schritt-für-Schritt-Anleitungen)

- **Educational Add-on:** [https://github.com/biolab/orange3-educational](https://github.com/biolab/orange3-educational)

*Erstellt für den Einsatz an Beruflichen Oberschulen in Bayern | Fach KIT, Jahrgangsstufe 12*

