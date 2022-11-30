import speech_recognition as sr
import webbrowser as web

def main():
    
    path  = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
    #print(path)
      
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)

        print("Please say something..")

        audio = recognizer.listen(source)

        print("Recognizing..")

        try:
            destination = recognizer.recognize_google(audio)
            print("You have said :" + destination)

            web.get(path)
            web.open(destination)

        except Exception as e :
            print("Error:" + str(e))

   

if __name__ == "__main__":
    main()