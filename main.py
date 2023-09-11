import speech_recognition as sr
import pywhatkit
import pyttsx3
import wikipedia
#initializations for assistant
detect = sr.Recognizer()
assistant_speak = pyttsx3.init()
voice = assistant_speak.getProperty('voices')
assistant_speak.setProperty('voice', voice[0].id)
assistant_speak.say('What can I help you with?')
assistant_speak.runAndWait()
#various error messages contingent on exception thrown
error_message = "Video url is too long, please try again"
error_message2 =  "Can't find any info, please try again"

def parse():
    #takes microphone input, converts to prompt
    try:
        with sr.Microphone() as inputS:
            print('listening for inputs')
            speech = detect.listen(inputS)
            prompt = detect.recognize_google(speech)
            print(prompt)
    except Exception as ex:
        #throws exception if try fails
        print("Error ", ex)
    return prompt
#simple function to make
def speak(text):
    assistant_speak.say(text)
    assistant_speak.runAndWait()

def run():
    prompt = parse()
    print(prompt)
    # Prompt should be in 'find a place where I can (activity)'
    # plays on youtube
    try:
        if 'find a place where I can' in prompt:
            activity = prompt.replace('find a place where I can', '')
            speak("I'll see what I can do for you....")
            pywhatkit.playonyt(activity)
    except:
        speak(error_message)
    #Prompt should be 'find a video of (activity)'
    #plays on youtube
    try:
        if 'find a video of' in prompt:
            activity1 = prompt.replace('find a video of', '')
            speak("Interesting topic, searching youtube")
            pywhatkit.playonyt(activity1)
    except:
        speak(error_message)
    #Prompt should be 'what is (item)'
    #recites from wikipedia
    try:
        if 'what is' in prompt:
            item = prompt.replace("what is", '')
            details = wikipedia.summary(item, 1)
            speak("Great question, here is what I could find.")
            speak(details)
    except:
        speak(error_message2)
    #Prompt should be 'where is (item)'
    #recites from wikipedia
    try:
        if 'where is' in prompt:
            item = prompt.replace("where is", '')
            location = wikipedia.summary(item, 1)
            speak("Great question, here is what I could find.")
            speak(location)
    except:
        speak(error_message2)
    #Prompt should be 'who is (item)'
    #recites from wikipedia
    try:
        if 'who is' in prompt:
            person = prompt.replace("who is", '')
            details1 = wikipedia.summary(person, 1)
            speak(details1)
    except:
        speak(error_message2)
    

    #Prompt should be 'tell me about (item)'
    #recites from wikipedia
    try:
        if 'tell me about' in prompt:
            trivia = prompt.replace("tell me about", "")
            fact = wikipedia.summary(trivia, 1)
            speak(fact)
    except:
        speak(error_message2)
 


run()
