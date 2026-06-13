# Anleitung: FaceMesh – Gesichtserkennung im Browser

## Was macht dieses Notebook?

Das Notebook bettet eine vollständige Web-App direkt in Jupyter ein. Die App erkennt in Echtzeit
ca. 478 Punkte im Gesicht des Nutzers – mithilfe des vortrainierten Modells **MediaPipe FaceMesh**,
das über **TensorFlow.js** im Browser ausgeführt wird.

Das Modell läuft dabei **komplett lokal auf dem Gerät** (On-Device KI): Es werden keine Bilder an
einen Server geschickt. Die Berechnungen übernimmt die GPU des Browsers via WebGL.

### Was ist auf dem Bildschirm zu sehen?

- **Live-Kamerabild** mit gespiegelter Darstellung (wie ein Spiegel)
- **478 Messpunkte** als kleine Kreise über dem Gesicht (Mesh)
- **Konturlinien** entlang Gesichtsoval, Augen, Augenbrauen, Lippen und Nase
- **Iris-Erkennung** in zwei Varianten:
  - *Ungenau*: schnelle Schätzung aus dem Augenkontour (kein extra Modell nötig)
  - *Präzise*: echter Pupillenkreis aus verfeinerten Landmarks (`refineLandmarks: true`)
- **FPS-Anzeige** und Zähler für erkannte Gesichter (bis zu 2 gleichzeitig)

### Steuerung

Alle Optionen lassen sich per Toggle-Button ein- und ausschalten. Iris Ungenau und Iris Präzise
schließen sich gegenseitig aus, da sie unterschiedliche Modell-Konfigurationen erfordern.

---

## Wichtig: HTTPS ist erforderlich

### Warum?

Der Zugriff auf die **Kamera des Geräts** (`getUserMedia`-API) ist ein sicherheitskritischer
Vorgang. Browser erlauben diesen Zugriff aus Datenschutzgründen **nur unter bestimmten
Bedingungen**:

- Die Seite wird über **HTTPS** ausgeliefert, **oder**
- die Seite läuft auf **`localhost`** (lokale Entwicklung)

Wird das Notebook über eine ungesicherte HTTP-Verbindung geöffnet (z. B. `http://123.45.67.89:8888`),
verweigert der Browser den Kamerazugriff stillschweigend oder zeigt eine Fehlermeldung.
Die App startet dann nicht.

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
