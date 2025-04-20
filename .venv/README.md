## On doit faire une IA capable de faire perdre du temps à des arnaqueurs téléphonique. Le but est d'être le plus convainquant possible pour garder l'escroc au téléphone.

## Pour cela on utilisere de la reconnaissance vocale ainsi qu'un LLM (Large Language Model) puis un TTS (Text To Speech).

# 🎭 Arnaquer les Arnaqueurs

## 🎯 Objectif

Créer une **IA vocale interactive** capable de **faire perdre du temps à des arnaqueurs** par téléphone ou chat, en les gardant dans la conversation le plus longtemps possible.  
Le but est de piéger les escrocs en leur faisant croire qu'on est une victime crédible.

---

## 🧠 Fonctionnalités

- 🧠 LLM (Hugging Face via Nebius) avec persona et stratégie
- 🎙️ Reconnaissance vocale (Speech-to-Text)
- 🔊 Synthèse vocale (Text-to-Speech)
- 🧩 Streaming de réponse pour fluidité
- 🎭 Simulation d’une personnalité crédible
- 🛑 Empêche de deviner qu’il s’agit d’une IA

---

## 🧪 Technologies

- Python 🐍
- Hugging Face + Nebius API
- `speech_recognition` pour la voix 🎙️
- `pyttsx3` ou TTS via API 🔊
- Streaming avec `InferenceClient`

---

## 🚀 Installation

```bash
git clone https://github.com/votre_user/arnaquer-les-arnaqueurs.git
cd arnaquer-les-arnaqueurs
pip install -r requirements.txt
