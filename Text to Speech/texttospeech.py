import pyttsx3
tts=pyttsx3.init()
tts.say("Hai my name is Jarvis.")
tts.runAndWait()
tts.say("My voice is Generated by python!")
tts.runAndWait()
tts.say("Whats Your Name???")
tts.runAndWait()
name=input()
tts.say("Glad to meet you " + name + ". Do you want to play with Me!" )
tts.runAndWait()
tts.say("Type yes or no or just y or n")
tts.runAndWait()
rep=input()
if rep == "yes" or rep=="y":
    tts.say("Just Kidding, I dont play with people named"+name)
    tts.runAndWait()
elif rep=="no" or rep=="n":
    tts.say("As if i wanted to play with you!")
    tts.runAndWait()
else:
    tts.say("Reply properly dumbass")
    tts.runAndWait()
