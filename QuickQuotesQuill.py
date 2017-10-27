import speech_recognition as sr
import wave

r = sr.Recognizer()
#r.recognize_google (audio, key = "94f421a6c116086bdcddbdd5accdd4c072cfb164")

#call Transcribe() instead of Listen() in console
#logs transcriptions in the Transcribe.txt file and tries to process the prescription
def Transcribe():
    rf = open ("Transcriptions.txt", "r")
    readTexts = rf.read()
    idNumber = FindLastIDInFile(readTexts) + 1
    idText = GenerateID (idNumber)
    d = open ("Transcriptions.txt", "w")
    d.write(readTexts)
    d.write (Listen(idNumber)+"\n")
    d.write("ID: "+idText+"\n")
    d.write ("----------\n")
    d.close()
    rf.close()

#if speech is recognized, then Listen() passes the recognized text to processing
def Listen (newID):
    sentence = SpeechRecognizer(newID)
    if type(sentence) == str:
        FindSubStringLocation(sentence)
        return sentence
    else:
        return "Error: Google Speech Recognition could not understand audio"

#tries to recognize the recorded audio
#returns a string of transcribed text if successful
def SpeechRecognizer(newID):
    with sr.Microphone() as source:
        print ("Recording...")
        audio = r.listen(source)
    try:
        sentence = r.recognize_google(audio)
        #sentence = "test"
        print ("'"+sentence+"'")
        d = wave.open (GenerateID(newID)+".wav","w")
        d.setparams ((2,2,22050,len(audio.get_wav_data()),"NONE","not compressed"))
        d.writeframes(audio.get_wav_data())
        d.close()
        return sentence
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

#input is the uneditted recognized string
#tries to find triggerphrases in the text
#if there triggerphrase is in the text, passes prescription information to FindPrescription()
#with the full text transcript and the index of where the prescription starts
def FindSubStringLocation (text):
    triggerPhraseList = "I'm going to give you "
    index = text.find(triggerPhraseList)
    if index == -1:
        print("Could not find prescription")
    else:
        FindPrescription (text, index+len(triggerPhraseList))

#input is the full transcribed text and the index of where the prescription starts
#prints the text of the prescription informations
def FindPrescription (text, index):
    print(text[index:])

#returns a 7 length string of the ID by appending 0 to the front
def GenerateID (newNumber):
    idText = str(newNumber)
    while len(idText) <7:
        idText = "0" + idText
    return idText

#Returns the int of the last ID in Trascriptions.txt
def FindLastIDInFile (newString):
    if len(newString) >= 19:
        return int(newString [-19:-12])
    else:
        return 0

#for debugging, returns the string in Transcriptions.txt
def PrintTranscript ():
    rf = open ("Transcriptions.txt", "r")
    sentences = rf.read()
    rf.close()
    return sentences