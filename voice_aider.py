#!/usr/bin/env python3
"""
Hands-free Voice Wrapper for Aider

This script provides continuous listening + text-to-speech
so you can talk to Aider without touching the keyboard.

Usage:
    python voice_aider.py

Then speak naturally. It will transcribe what you say.
You can copy the transcribed text into your Aider session,
or use it to drive Aider in more advanced setups.
"""

import speech_recognition as sr
import pyttsx3
import sys
import time

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 175)  # Speed of speech
engine.setProperty('volume', 0.9)

recognizer = sr.Recognizer()

# Adjust for ambient noise
with sr.Microphone() as source:
    print("\ud83c\udf99\ufe0f Calibrating microphone for ambient noise...")
    recognizer.adjust_for_ambient_noise(source, duration=1)

print("\n\u2705 Hands-free Aider Voice Wrapper is ready!")
print("Speak naturally. Say 'stop' or press Ctrl+C to exit.\n")

 def speak(text):
    """Speak the given text out loud."""
    print(f"\ud83d\udde3\ufe0f  Aider: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen for a single utterance and return transcribed text."""
    with sr.Microphone() as source:
        print("\ud83c\udf99\ufe0f  Listening... (speak now)")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("\u2699\ufe0f  Transcribing...")
            text = recognizer.recognize_google(audio)  # or recognize_whisper for local
            return text
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            print("\u26a0\ufe0f  Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"\u274c  Speech recognition error: {e}")
            return None


def main():
    try:
        while True:
            text = listen()
            if text:
                print(f"\n\ud83d\udcac You said: {text}")

                if text.lower() in ["stop", "exit", "quit"]:
                    speak("Stopping voice assistant. Goodbye!")
                    break

                # Here you would normally send `text` to Aider
                # For now, it prints clearly so you can paste it into Aider
                print("\n\u2192 Copy the above into your Aider chat, or run Aider with --voice\n")

                # Example: speak a placeholder response
                # In a full version this would come from Aider
                speak("Message received. I'm ready for your next instruction.")

            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\n\ud83d\udd04 Exiting...")
        speak("Voice wrapper stopped.")


if __name__ == "__main__":
    main()
