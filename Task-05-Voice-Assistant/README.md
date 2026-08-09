# 🎙️ Voice Assistant

## Overview

A Python-based voice assistant that uses speech recognition and text-to-speech technologies to interact with users through voice commands.

The assistant listens to spoken commands, interprets them, performs predefined actions, and responds using synthesized speech.

## Objective

To develop an interactive voice-based assistant capable of recognizing natural voice commands and performing useful tasks through speech interaction.

## Features

- 🎤 Voice command recognition
- 🔊 Text-to-speech responses
- 🕐 Current time detection
- 📅 Current date detection
- 🌐 Open Google
- ▶️ Open YouTube
- 💻 Open GitHub
- 🔎 Perform Google searches
- 🛑 Voice-controlled exit

## Technologies Used

**Python • SpeechRecognition • PyAudio • pyttsx3 • Web Browser Automation**

## How It Works

```text
Voice Input
     ↓
Speech Recognition
     ↓
Command Processing
     ↓
Action Execution
     ↓
Text-to-Speech Response
```

## Project Structure

```text
Task-05-Voice-Assistant/
│
├── voice_assistant.py
├── requirements.txt
├── README.md
└── screenshots/
    └── voice_assistant_start.png
```

## Installation

Install the required dependencies:

```bash
py -m pip install -r requirements.txt
```

## Running the Assistant

Run:

```bash
py voice_assistant.py
```

Then speak a supported command when the assistant begins listening.

## Example Commands

```text
"Hello"
"What is the time?"
"What's the date?"
"Open Google"
"Open YouTube"
"Open GitHub"
"Search for Python tutorials"
"Exit"
```

## Screenshots

Screenshots demonstrating the voice assistant are available in the `screenshots` directory.

## Disclaimer

This project is intended as an educational demonstration of speech recognition, text-to-speech, and voice-based command processing.