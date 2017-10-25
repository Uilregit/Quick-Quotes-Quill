import speech_recognition as sr

r = sr.Recognizer()
#r.recognize_google (audio, key = "94f421a6c116086bdcddbdd5accdd4c072cfb164")

def Transcribe():
    r = open ("Transcriptions.txt", "r")
    readTexts = r.read()
    d = open ("Transcriptions.txt", "w")
    d.write(readTexts)
    d.write (Listen()+"\n")
    #d.write ("stuff"+"\n")
    d.write ("----------\n")
    d.close()
    r.close()

def Listen ():
    sentence = SpeechRecognizer()
    if type(sentence) == str:
        FindSubStringLocation(sentence)
        return sentence
    else:
        return "Error: Google Speech Recognition could not understand audio"
    
    
def SpeechRecognizer():
    with sr.Microphone() as source:
        print ("Recording...")
        audio = r.listen(source)
    try:
        sentence = r.recognize_google(audio)
        print ("'"+sentence+"'")
        return sentence
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def FindSubStringLocation (text):
    triggerPhraseList = "I'm going to give you "
    index = text.find(triggerPhraseList)
    if index == -1:
        print("Could not find prescription")
    else:
        FindPrescription (text, index+len(triggerPhraseList))

def FindPrescription (text, index):
    print(text[index:])
