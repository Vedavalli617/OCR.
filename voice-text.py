import speech_recognition as sr
import pyttsx3
import json
from datetime import datetime
import mysql.connector
import pymongo

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Loop infinitely for the user to speak
while True:
    # Exception handling to handle exceptions at runtime
    try:
        # Use the microphone as the source for input
        with sr.Microphone() as source2:
            # Wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            # Listens for the user's input
            print("GIVE USER INPUT---")
            audio2 = r.listen(source2)
            print("Recognizing voice input...")
            
            # Using Google to recognize audio
            text = r.recognize_google(audio2)
            text = text.lower()

            print("Did you say:", text)
            #SpeakText(text)
            if text == "stop":
                print("Exiting the program...")
                break
            data = {"text": text}
            json_data = json.dumps(data)

            # Generate a unique timestamp for the JSON file name
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            json_file = f"extracted_voicetext_{timestamp}.json"

            with open(json_file, "w") as file:
                file.write(json_data)

            # Step 1: Read the JSON file and parse it into Python data structures
            with open('your_file_path.json', 'r') as file:
                data = json.load(file)

            print("Text extracted and saved in", json_file)
            # Check if the user wants to exit
            
            
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown error occurred")
    except:
        False
