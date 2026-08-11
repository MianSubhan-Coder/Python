import pyttsx3
engine = pyttsx3.init()
text = input("Write that you want to listen or write exit: ")
engine.say(text)
engine.runAndWait()