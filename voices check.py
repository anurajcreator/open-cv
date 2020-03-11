# Print all available voices
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[4].id)

rate = engine.getProperty('rate')
print(rate)

engine.say('Hello MR. Anuraj, How can I help you')
engine.setProperty('rate', 150)
engine.say('Hello MR. Anuraj, How can I help you')

# for voice in voices:
#     print("Voice:")
#     print(" - ID: %s" % voice.id)
#     print(" - Name: %s" % voic
#     e.name)
#     print(" - Languages: %s" % voice.languages)
#     print(" - Gender: %s" % voice.gender)
#     print(" - Age: %s" % voice.age)
