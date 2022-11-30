import speech_recognition as sr

#Creates a new Recognizer instance, 
# which represents a collection of speech recognition functionality.

recognizer = sr.Recognizer()

#Creates a new Microphone instance, 
# which represents a physical microphone on the computer. Subclass of AudioSource.

microphone = sr.Microphone()

#Returns a list of the names of all available microphones. For microphones where the name can't be retrieved, 
# the list entry contains None instead.

#list = sr.Microphone.list_microphone_names()

#print(list)

with microphone as source:
    #Adjusts the energy threshold dynamically using audio from source 
    # (an AudioSource instance) to account for ambient noise.
    recognizer.adjust_for_ambient_noise(source)

    print('Please say something..')

    audio = recognizer.listen(source)

    print("Recognizing Now..")


    try:
        dest= recognizer.recognize_google(audio)
        print("You have said: " + dest)
    except:
        print("Failed to recognize")

