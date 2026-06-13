# Anleitung: Obsterkennung – Bildklassifikation im Browser

## Was macht dieses Notebook?

Das Notebook bettet eine Kamera-App direkt in Jupyter ein und demonstriert **Bildklassifikation**
mit dem vortrainierten Modell **MobileNetV2**, das über **TensorFlow.js** im Browser läuft.

Das Modell wurde auf **ImageNet** trainiert – einem Datensatz mit über 14 Millionen Bildern in
1000 Kategorien. Die App filtert aus diesen 1000 Klassen die bekannten Obstsorten heraus und
zeigt das wahrscheinlichste Ergebnis mit Emoji, deutschem Namen und einem Konfidenzbalken an.

### Ablauf

1. Die Kamera startet automatisch, sobald das Modell geladen ist.
2. Ein Klick auf den **Auslöser-Button** friert das Bild ein und startet die Analyse.
3. Das Modell gibt für alle 1000 ImageNet-Klassen eine Wahrscheinlichkeit aus.
   Die App zeigt das Obst mit dem höchsten Wert an – oder eine Fehlermeldung, falls kein
   bekanntes Obst erkannt wurde.
4. Mit **"↩ Nochmal"** kehrt die App zur Live-Ansicht zurück.

### Optionaler Python-Teil (Zelle 3)

Über den Button **"📤 An Python senden"** wird das aufgenommene Foto als Base64-kodierter Text
über die Jupyter Contents API auf dem Server gespeichert (`captured_fruit.txt`).
Zelle 3 liest diese Datei serverseitig ein, führt die Klassifikation erneut mit **Keras/TensorFlow
(Python)** durch und zeigt die Top-5-Ergebnisse mit Textbalken an. So wird der Unterschied
zwischen clientseitiger (JavaScript im Browser) und serverseitiger KI (Python auf dem Server)
direkt erlebbar.

Ist kein Kamerabild vorhanden, verwendet Zelle 3 automatisch ein Beispielbild (roter Apfel
von Wikimedia Commons).

---

## Wichtig: HTTPS ist erforderlich

### Warum?

Die App greift über die **`getUserMedia`-API** auf die Kamera des Geräts zu.
Browser erlauben diesen Zugriff aus Datenschutzgründen **nur in sicheren Kontexten**:

- Die Seite wird über **HTTPS** ausgeliefert, **oder**
- die Seite läuft auf **`localhost`** (lokale Entwicklung)

Wird das Notebook über eine ungesicherte HTTP-Verbindung geöffnet (z. B. `http://123.45.67.89:8888`),
blockiert der Browser den Kamerazugriff. Die App zeigt dann dauerhaft „FEHLER" an und der
Auslöser-Button bleibt deaktiviert.

### Was bedeutet das in der Praxis?

| Situation | Kamerazugriff möglich? |
|---|---|
| JupyterLab auf `localhost` (lokal am eigenen Rechner) | ✅ Ja |
| JupyterLab über HTTPS (z. B. JupyterHub mit Zertifikat) | ✅ Ja |
| JupyterLab über HTTP auf einem Schulserver | ❌ Nein |
| JupyterLab über HTTP mit IP-Adresse | ❌ Nein |

### Lösung für den Unterricht

Wird das Notebook auf einem Schulserver betrieben, muss dieser mit einem gültigen
TLS/SSL-Zertifikat gesichert sein und über `https://...` erreichbar sein.
Alternativ kann jede Schülerin und jeder Schüler JupyterLab lokal auf dem eigenen Gerät
starten – dann ist kein Zertifikat nötig.

> **Hinweis zur "An Python senden"-Funktion:** Diese nutzt intern die Jupyter Contents API
> und setzt ebenfalls einen sicheren Kontext voraus. Bei lokalem Betrieb auf `localhost`
> funktioniert sie ohne weitere Konfiguration.
