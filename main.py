from voice import say, take_command
from brain import ask_ollama
import webbrowser

say("Hello, I am Echolish AI, your free voice assistant.")

# Shortcut websites
sites = {
    "youtube": "https://www.youtube.com",
    "wikipedia": "https://www.wikipedia.org",
    "google": "https://www.google.com",
    "facebook": "https://www.facebook.com"
}

chat_history = []

while True:
    query = take_command()
    if not query:
        continue

    query = query.lower().strip()
    print(f"User said: {query}")
    chat_history.append(f"User: {query}")

    # === Open website commands ===
    matched = False
    for name, url in sites.items():
        if f"open {name}" in query:
            say(f"Opening {name}")
            webbrowser.open(url)
            matched = True
            break

    if matched:
        continue

    # === Special commands ===
    if "open music" in query:
        say("Opening music...")
        webbrowser.open("https://music.apple.com/us/album/killin-it-girl/1816986745?i=1816986747")

    elif any(x in query for x in ["exit", "quit", "stop"]):
        say("Goodbye!")
        break

    elif "reset chat" in query:
        chat_history = []
        say("Chat history has been reset.")

    elif "what did i just ask" in query or "what did i just say" in query:
        recent = [line for line in chat_history if line.startswith("User:")]
        if recent:
            say(f"You just said: {recent[-1][6:].strip()}")
        else:
            say("I don't remember anything before that.")

    elif "give me history" in query or "what's the chat history" in query:
        if chat_history:
            say("Here's what I remember:")
            for line in chat_history[-6:]:
                if line.startswith("User:") or line.startswith("Assistant:"):
                    say(line[6:].strip())
        else:
            say("There's no chat history yet.")

    else:
        say("Let me think about that.")
        # Keep recent chat short for better model output
        recent_prompt = "\n".join(chat_history[-10:])
        response = ask_ollama(recent_prompt)
        response = response.strip().replace("...", "")  # Remove filler if any
        say(response)
        chat_history.append(f"Assistant: {response}")