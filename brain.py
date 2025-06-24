# === brain.py ===

import requests

def ask_ollama(prompt):
    # No assistant identity, no fluff — just short human-like answers
    full_prompt = (
        f"Answer briefly and naturally. No introductions. No 'I'm an assistant'. "
        f"No 'thank you'. Just answer in 1-2 sentences.\n\nQ: {prompt.strip()}\nA:"
    )

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": full_prompt,
                "stream": False
            }
        )
        data = response.json()
        return data.get("response", "I don't know.").strip()
    except Exception as e:
        return f"Error: {e}"