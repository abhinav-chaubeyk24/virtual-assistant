import speech_recognition as sr
listener = sr.Recognizer()


try:
    with sr.Microphone() as inputS:
        print('listneing for inputs')
        speech = listener.listen(inputS)
        prompt = listener.recognize_google(speech)
        print(prompt)
except Exception as ex:
    print("Error ", ex)

