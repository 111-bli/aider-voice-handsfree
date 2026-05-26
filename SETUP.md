# Aider Voice Hands-Free Setup for Kali Linux

**Hands-free voice wrapper for Aider** — continuous listening with wake word, so you can talk to Aider without touching anything.

Tuned for your **2008 iMac (Kali Linux)** using fast cloud STT + lightweight TTS.

pipx is fully supported (it manages its own isolated environments).

## 1. Install required system packages (these must be installed separately)

```bash
sudo apt update
sudo apt install -y espeak-ng portaudio19-dev python3-pyaudio git
```

## 2. Install / verify Aider via pipx (your preferred method)

```bash
pipx install aider-chat
aider --version
```

If you already have it, you're good.

## 3. Get an OpenAI API key (recommended for speed on old hardware)

1. Go to https://platform.openai.com/api-keys
2. Create a key
3. You'll export it when running: `export OPENAI_API_KEY=sk-...`

## 4. Clone or update the repo

```bash
git clone https://github.com/111-bli/aider-voice-handsfree.git
cd aider-voice-handsfree
git pull
```

## 5. Install Python dependencies (pipx handles its own envs)

pipx creates clean isolated environments for tools. For this project:

```bash
# Core packages via pipx
pipx install openai pexpect

# Speech + other libs (pipx doesn't do -r requirements directly for libraries, so we use --user)
python3 -m pip install --user -r requirements.txt
```

**Note:** `pipx` manages its own environments automatically. The `--user` flag keeps library installs clean and out of the system Python.

## 6. Run the hands-free wrapper

```bash
export OPENAI_API_KEY=sk-your-key-here

python3 voice_aider.py
```

- It will calibrate your microphone.
- Then wait for the **wake word "Hey Aider"** (edit the script to change it).
- Speak naturally after the wake word.
- The transcription prints clearly so you can paste into Aider or extend it to auto-control.

## How it works
- Wake word detection
- Cloud speech-to-text (fast even on old hardware)
- Lightweight TTS via pyttsx3 / espeak-ng
- Ready to integrate with Aider (pexpect ready in code)

## When you upgrade your PC later
We can switch to fully local/offline models (Whisper + Piper TTS) with one change in the script.

## Troubleshooting
- Mic check: `arecord -l`
- Test speech: `espeak-ng "hello from kali"`
- If things are trippin' with pip: the pipx + --user combo above usually fixes it.

You're all set for hands-free Aider on Kali!