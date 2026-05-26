#!/usr/bin/env python3
"""
Hands-free Voice Wrapper for Aider on Kali Linux

Continuous listening with wake word ("Hey Aider").
Fast transcription + lightweight TTS.
Prints what you said clearly so you can use it with Aider.

pipx friendly setup.
"""

import speech_recognition as sr
import pyttsx3
import time
import os

WAKE_WORD = "hey aider"

# TTS setup (uses espeak-ng under the hood on Linux)
engine = pyttsx3.init()
engine.setProperty('rate', 175)
engine.setProperty('volume', 0.9)

recognizer = sr.Recognizer()

print("\ud83c\udf99\ufe0f  Calibrating microphone...")
with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=1.5)

print("\n\u2705  Hands-free Aider Voice is ready!")
print(f"Say the wake word \"{WAKE_WORD}\" then speak your command.")
print("Say 'stop' to exit.\n")

def speak(text):
    print(f"\ud83d\udde3\ufe0f  Aider: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("\ud83c\udf99\ufe0f  Listening...")
        try:
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=12)
            text = recognizer.recognize_google(audio).lower()
            return text
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            print(f"Speech error: {e}")
            return None

def main():
    try:
        while True:
            text = listen()
            if not text:
                continue

            print(f"\nYou said: {text}")

            if "stop" in text or "exit" in text or "quit" in text:
                speak("Stopping. Goodbye!")
                break

            if WAKE_WORD in text:
                # Remove wake word and process the command
                command = text.replace(WAKE_WORD, "").strip()
                if command:
                    print(f"\n\u2192 Command for Aider: {command}")
                    speak(f"Got it. Command received: {command}")
                    # TODO: Here we can add pexpect to auto-send to Aider
                    # For now it prints clearly so you can copy/paste or run in parallel
                else:
                    speak("Wake word heard. What's your command?")
            else:
                # Optional: still show transcription
                print("(No wake word detected - waiting for wake word)")

            time.sleep(0.3)

    except KeyboardInterrupt:
        print("\nExiting...")
        speak("Voice wrapper stopped.")

if __name__ == "__main__":
    main()
