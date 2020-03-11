import speech_recognition as sr


def takeCommand():
    # Input and returns String
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        return "None"
    return query


query = takeCommand()

print(query)
