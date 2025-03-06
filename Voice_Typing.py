import speech_recognition as sr
import pyautogui

def voice_typing():
    recognizer = sr.Recognizer()
    
    while True:
        with sr.Microphone() as source:
            print("Please speak something (you can speak continuously)...")
            
            try:
                audio = recognizer.listen(source, phrase_time_limit=10)  # You can adjust the time limit by changing the '10'
                recognized_text = recognizer.recognize_google(audio)
                print("You said: " + recognized_text)
                
                # This sends the verbal input to the text box you are on
                pyautogui.typewrite(recognized_text)
                
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service.")

        print("Would you like to record more? Please say 'yes' or 'no'.")
        
        with sr.Microphone() as source:
            try:
                audio = recognizer.listen(source, timeout=3)
                response = recognizer.recognize_google(audio).lower()
                print("You said: " + response)
                
                # Multiple inputs for 'yes' and 'no', add and change to whatever you like
                yes_responses = ['yes', 'yeah', 'yep', 'sure', 'absolutely', 'definitely']
                no_responses = ['no', 'nope', 'nah', 'not really', 'never']

                if any(yes in response for yes in yes_responses):
                    print("Please continue...")
                elif any(no in response for no in no_responses):
                    print("Exiting...")
                    break
                else:
                    print("I didn't understand that. Please say 'yes' or 'no'.")
            except sr.WaitTimeoutError:
                print("No input detected within the time limit.") # You cna change it to say "within x seconds"
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service.")

if __name__ == "__main__":
    voice_typing()
