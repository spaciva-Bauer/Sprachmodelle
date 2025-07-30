import tkinter as tk
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "gemma3"

def ask_ollama_top_k(prompt, top_k=10):
    system_prompt = (
        f"Was sind die {top_k} wahrscheinlichsten nächsten Wörter "
        f"nach folgendem Text:\n\"{prompt}\"\n"
        f"Gib nur eine saubere Liste von Wörtern aus, ohne Erklärungen."
    )

    try:
        response = requests.post(OLLAMA_URL, json={
            "model": OLLAMA_MODEL,
            "prompt": system_prompt,
            "stream": False
        })

        if response.status_code == 200:
            return response.json().get("response", "").strip()
        else:
            return f"Fehler vom Server: {response.status_code}"
    except Exception as e:
        return f"Fehler bei der Anfrage: {str(e)}"

def on_submit():
    input_text = entry.get()
    result = ask_ollama_top_k(input_text)
    output_label.config(text=result)

# GUI mit tkinter
root = tk.Tk()
root.title("Ollama gemma3 – Top 10 Wort-Vorhersage")

tk.Label(root, text="Satzanfang eingeben:").pack(pady=(10, 0))
entry = tk.Entry(root, width=60)
entry.pack(pady=5)

submit_button = tk.Button(root, text="Vorhersagen", command=on_submit)
submit_button.pack(pady=10)

output_label = tk.Label(root, text="", wraplength=500, justify="left")
output_label.pack(pady=10)

root.mainloop()
