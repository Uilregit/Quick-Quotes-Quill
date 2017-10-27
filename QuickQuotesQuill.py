import speech_recognition as sr
import wave

r = sr.Recognizer()
#r.recognize_google (audio, key = "94f421a6c116086bdcddbdd5accdd4c072cfb164")

#call Transcribe() instead of Listen() in console
#logs transcriptions in the Transcribe.txt file and tries to process the prescription
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

#if speech is recognized, then Listen() passes the recognized text to processing
def Listen ():
    sentence = SpeechRecognizer()
    if type(sentence) == str:
        FindSubStringLocation(sentence)
        return sentence
    else:
        return "Error: Google Speech Recognition could not understand audio"

#tries to recognize the recorded audio
#returns a string of transcribed text if successful
def SpeechRecognizer():
    with sr.Microphone() as source:
        print ("Recording...")
        audio = r.listen(source)
    try:
        sentence = r.recognize_google(audio)
        print ("'"+sentence+"'")
        d = wave.open (sentence+".wav","w")
        d.setparams ((2,2,16000,len(audio.get_wav_data()),"NONE","not compressed"))
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
