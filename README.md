# Workshop-1
# Python Automation Toolkit

## Table of Contents
- [Text to Speech (TTS) using Python](#text-to-speech-tts-using-python)
- [Speech to Text (STT) Conversion using Python](#speech-to-text-stt-conversion-using-python)
- [Send WhatsApp Messages using Python](#send-whatsapp-messages-using-python)
- [Additional Notes](#additional-notes)

## Text to Speech (TTS) using Python
### Description
Introduce the TTS script and its purpose here.

### Installation
Provide instructions on how to install the required library, `pyttsx3`, for TTS.

### Usage
Explain how to use the TTS script. Mention any customization options, such as changing the greeting message or voice settings.

### Example
Include an example code snippet demonstrating the usage of the TTS script.

```python
import pyttsx3
engine = pyttsx3.init()
engine.say("Hello, how can I assist you?")
engine.runAndWait()

import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Adjusting for noise...")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Listening...")
    recorded_audio = recognizer.listen(source, timeout=5)
    print("Done recording")

try:
    print("Recognized Text: " + recognizer.recognize_google(recorded_audio, language="en-US"))
except Exception as ex:
    print(ex)


import pywhatkit as py

# Replace with recipient's phone number and message content
recipient_number = "+91 1234565489"
message_content = "Hello, how are you?"

py.sendwhatmsg_instantly(recipient_number, message_content)
