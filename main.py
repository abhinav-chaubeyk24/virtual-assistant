import speech_recognition as sr
import pywhatkit
import pyttsx3
import wikipedia

detect = sr.Recognizer()
alexa_speak = pyttsx3.init()
voice = alexa_speak.getProperty('voices')
alexa_speak.setProperty('voice', voice[0].id)
alexa_speak.say('What can I help you with?')
alexa_speak.runAndWait()
error_message = "Video url is too long, please try again"
error_message2 =  "Can't find any info, please try again"

def parse():
    try:
        with sr.Microphone() as inputS:
            print('listening for inputs')
            speech = detect.listen(inputS)
            prompt = detect.recognize_google(speech)
            print(prompt)
    except Exception as ex:
        print("Error ", ex)
    return prompt

def speak(text):
    alexa_speak.say(text)
    alexa_speak.runAndWait()

def run():
    prompt = parse()
    print(prompt)
    # Prompt should be in 'find a place where I can (activity) in (location)'
    try:
        if 'find a place where I can' in prompt:
            activity = prompt.replace('find a place where I can', '')
            speak("I'll see what I can do for you....")
            pywhatkit.playonyt(activity)
    except:
        speak(error_message)
    try:
        if 'find a video of' in prompt:
            activity1 = prompt.replace('find a video of', '')
            speak("Interesting topic, searching youtube")
            pywhatkit.playonyt(activity1)
    except:
        speak(error_message)

    try:
        if 'what is' in prompt:
            item = prompt.replace("what is", '')
            details = wikipedia.summary(item, 1)
            speak("Great question, here is what I could find.")
            speak(details)
    except:
        speak(error_message2)
    
    try:
        if 'who is' in prompt:
            person = prompt.replace("who is", '')
            details1 = wikipedia.summary(person, 1)
            speak(details1)
    except:
        speak(error_message2)

 


run()
