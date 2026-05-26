# Full Setup Guide for Hands-Free Aider Voice Chat

This guide will get you talking to Aider completely hands-free.

## Step 1: Install Aider

```bash
pip install aider-chat
```

Test it:
```bash
aider --help
```

## Step 2: Enable Voice in Aider (Built-in)

Aider has official voice support:

```bash
aider --voice
```

This lets you speak to Aider directly in the terminal.

However, it still requires you to press Enter or use a hotkey in some setups. For **true hands-free**, use the Python wrapper.

## Step 3: Set Up the Voice Wrapper

```bash
# Clone the repo (if you haven't)
git clone https://github.com/111-bli/aider-voice-handsfree.git
cd aider-voice-handsfree

# Install voice dependencies
pip install -r requirements.txt
```

> **Note:** On some systems you may need `portaudio` installed for PyAudio.
> - macOS: `brew install portaudio`
> - Ubuntu/Debian: `sudo apt install portaudio19-dev`

## Step 4: Run the Hands-Free Wrapper

```bash
python voice_aider.py
```

The script will:
1. Calibrate your microphone
2. Listen continuously
3. Transcribe everything you say
4. Speak responses using your system's TTS

You can then copy the transcribed text and paste it into your Aider terminal, or combine both.

## How to Use It Day-to-Day

**Recommended workflow:**

1. Open two terminals side by side:
   - Terminal 1: Run `aider` (or `aider --voice`)
   - Terminal 2: Run `python voice_aider.py`

2. Talk naturally into your microphone
3. The voice wrapper transcribes what you said
4. Paste (or have it auto-send in future versions) into Aider
5. Aider edits your code
6. Read Aider's reply or have the wrapper speak summaries

## Making It More Automatic (Future)

The current `voice_aider.py` is a solid foundation. Future versions will include:
- Automatic sending of transcribed text into a running Aider session (using pexpect)
- Wake word detection ("Hey Aider...")
- Better local STT (faster-whisper)

## Tips

- Use a decent USB microphone or headset for best accuracy
- Speak clearly and at a normal pace
- You can say things like:
  - "Add a new route to the FastAPI app"
  - "Refactor this function to be async"
  - "Write tests for the user model"
  - "Commit the current changes with message 'add login'"

## Troubleshooting

**Microphone not working?**
- Make sure PyAudio is installed correctly
- Try adjusting `recognizer.energy_threshold`

**TTS not speaking?**
- On Linux you may need `espeak` or `festival` installed

## Next Level

Want me to improve the automation further (full pexpect integration so it drives Aider automatically)? Just say the word and I'll update the repo.

Enjoy coding by voice! 🚀