# Aider Voice Hands-Free Setup for Kali Linux

This repo gives you a **continuous hands-free voice interface** for Aider on Kali Linux.

It listens for a wake word ("Hey Aider"), transcribes your speech using fast cloud STT, automatically feeds commands into Aider, and speaks the results back using lightweight `espeak-ng`.

Perfect for your 2008 iMac running Kali.

## Prerequisites

### 1. Install system packages (required separately)
```bash
sudo apt update
sudo apt install -y espeak-ng portaudio19-dev python3-pyaudio python3-venv git
```

### 2. Install Aider first (make sure it works normally)
```bash
aider --version
```
If not installed:
```bash
pipx install aider-chat
```

### 3. Get an OpenAI API key (recommended for speed on old hardware)
- Go to https://platform.openai.com/api-keys
- Create a key and copy it.

## Setup

```bash
# Clone or update the repo
git clone https://github.com/111-bli/aider-voice-handsfree.git
cd aider-voice-handsfree

git pull

# Install Python dependencies with pipx
pipx install -r requirements.txt

# Or if you prefer a venv:
# python3 -m venv .venv
# source .venv/bin/activate
# pip install -r requirements.txt
```

## Run it

```bash
export OPENAI_API_KEY=sk-your-key-here

python voice_aider.py
```

It will calibrate your microphone, then wait for the wake word **"Hey Aider"**.

Just talk naturally after the wake word.

## How to use
- Say **"Hey Aider, create a new Python file called test.py"**
- The script will transcribe it and send it to Aider automatically (using pexpect).
- Responses are spoken out loud.

## Switching to fully local later
When you upgrade your PC, edit the script and change to local Whisper + Piper TTS for completely offline use.

## Troubleshooting
- Mic not working? Check with `arecord -l`
- espeak-ng not speaking? `espeak-ng "test"`
- Slow? Use the cloud STT option (already default).

Enjoy hands-free coding!