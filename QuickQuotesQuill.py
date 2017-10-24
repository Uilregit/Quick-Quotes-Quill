import speech_recognition as sr

r = sr.Recognizer()
#r.recognize_google (audio, key = "94f421a6c116086bdcddbdd5accdd4c072cfb164")
def listen ():
    with sr.Microphone() as source:
        print ("Say something!")
        audio = r.listen(source)

    try:
        sentence = r.recognize_google(audio)
        print ("'"+sentence+"'")
        findSubStringLocation (sentence)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def findSubStringLocation (text):
    triggerPhraseList = "I'm going to give you "
    index = text.find(triggerPhraseList)
    if index == -1:
        print("Could not find prescription")
    else:
        findPrescription (text, index+len(triggerPhraseList))

def findPrescription (text, index):
    print( text[index:])
