# Text to speech using python code
import pyttsx3
engine=pyttsx3.init()
engine.say("Hii Chandan, How can I help you?")
engine.runAndWait()


# Speech to text convertion using python
import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Adjusting noise ")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    engine=pyttsx3.init()
    engine.say("Hii Chandan, How can I help you?")
    engine.runAndWait()
    print("listening....")
    recorded_audio = recognizer.listen(source, timeout=5)
    print("Done recording")
    
try:
    print("Recognizing the text")
    text = recognizer.recognize_google(
            recorded_audio, 
            language="en-US"
        )
    print("Decoded Text : {}".format(text))
    #pint(text)
except Exception as ex:
    print(ex)



# Send WhatsApp message using python
import pywhatkit as py
py.sendwhatmsg_instantly("+91 1234565489", "Hii, how are you")