### ✅ `main.py` (avec ton code + voix intégrée)

from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
import pyttsx3
import speech_recognition as sr

load_dotenv()

api_key = os.getenv("NEBIUS_API_KEY")
client = InferenceClient(
    provider="nebius",
    api_key=api_key,
)

# SYSTEM PROMPT
context = "Tu es une fausse victime d'arnaque."
arnaque = "L'arnaque consiste à faire croire à la victime qu'elle a gagné un prix"
personnalite = "Tu es un homme de 45 ans, qui vit à Paris."
instructions = "Tu dois faire perdre du temps à l'escroc."
negative = "Tu ne dois pas dire que tu es une IA ni que tu es un robot."

messages = [
    {
        "role": "system",
        "content": context + "\n" + arnaque + "\n" + personnalite + "\n" + instructions + "\n" + negative,
    }
]
# INIT TTS
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # vitesse de parole


# STT
recognizer = sr.Recognizer()

def listen_to_scammer():
    with sr.Microphone() as source:
        print("🎧 En écoute...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio, language="fr-FR")
    except:
        return "Je n'ai pas bien entendu..."

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    user_input = listen_to_scammer()
    print("👤 Escroc :", user_input)

    messages.append({"role": "user", "content": user_input})

    print("🤖 IA :", end=" ", flush=True)
    reply = ""
    completion = client.chat.completions.create(
        model="Qwen/Qwen2.5-Coder-32B-Instruct",
        messages=messages,
        max_tokens=512,
        stream=True,
        temperature=0.9
    )
    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            reply += chunk.choices[0].delta.content

    print("\n🔊 Lecture audio...")
    speak(reply)
    messages.append({"role": "assistant", "content": reply})