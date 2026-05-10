import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import os
import pyautogui
import psutil
import pyjokes
from datetime import datetime

# =========================
# INITIAL SETUP
# =========================

listener = sr.Recognizer()
engine = pyttsx3.init()

# =========================
# SPEAK FUNCTION
# =========================

def talk(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# =========================
# TAKE VOICE COMMAND
# =========================

def take_command():
    command = ""

    try:
        with sr.Microphone() as source:

            print("Listening...")

            # Reduce background noise
            listener.adjust_for_ambient_noise(source, duration=1)

            # Listen from mic
            voice = listener.listen(source)

            print("Recognizing...")

            # Convert speech to text
            command = listener.recognize_google(voice)

            # Lowercase
            command = command.lower()

            print("You said:", command)

    except Exception as e:
        print("Error:", e)

    return command

# =========================
# MAIN JARVIS FUNCTION
# =========================

def run_jarvis():

    command = take_command()

    # -------------------------
    # OPEN CHROME
    # -------------------------
    if 'open chrome' in command:
        talk('Opening Chrome')
        os.system('start chrome')

    # -------------------------
    # OPEN YOUTUBE
    # -------------------------
    elif 'open youtube' in command:
        talk('Opening YouTube')
        os.system('start https://youtube.com')

    # -------------------------
    # OPEN WHATSAPP
    # -------------------------
    elif 'open whatsapp' in command:
        talk('Opening WhatsApp')
        os.system('start https://web.whatsapp.com')

    # -------------------------
    # PLAY SONG
    # -------------------------
    elif 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)

    # -------------------------
    # GOOGLE SEARCH
    # -------------------------
    elif 'search' in command:
        search = command.replace('search', '')
        talk('Searching ' + search)
        pywhatkit.search(search)

    # -------------------------
    # WIKIPEDIA
    # -------------------------
    elif 'who is' in command:
        person = command.replace('who is', '')

        try:
            info = wikipedia.summary(person, 1)
            talk(info)

        except:
            talk("I couldn't find information")

    # -------------------------
    # TIME
    # -------------------------
    elif 'time' in command:
        current_time = datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + current_time)

    # -------------------------
    # JOKES
    # -------------------------
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)

    # -------------------------
    # BATTERY
    # -------------------------
    elif 'battery' in command:
        battery = psutil.sensors_battery()
        percent = battery.percent
        talk(f'Battery is at {percent} percent')

    # -------------------------
    # VOLUME UP
    # -------------------------
    elif 'volume up' in command:
        pyautogui.press('volumeup')
        talk('Volume increased')

    # -------------------------
    # VOLUME DOWN
    # -------------------------
    elif 'volume down' in command:
        pyautogui.press('volumedown')
        talk('Volume decreased')

    # -------------------------
    # MUTE
    # -------------------------
    elif 'mute' in command:
        pyautogui.press('volumemute')
        talk('Volume muted')

    # -------------------------
    # OPEN NOTEPAD
    # -------------------------
    elif 'open notepad' in command:
        talk('Opening Notepad')
        os.system('notepad')

    # -------------------------
    # OPEN CALCULATOR
    # -------------------------
    elif 'open calculator' in command:
        talk('Opening Calculator')
        os.system('calc')

    # -------------------------
    # SCREENSHOT
    # -------------------------
    elif 'take screenshot' in command:

        screenshot = pyautogui.screenshot()

        screenshot.save("screenshot.png")

        talk('Screenshot saved')

    # -------------------------
    # SHUTDOWN PC
    # -------------------------
    elif 'shutdown' in command:
        talk('Shutting down computer')
        os.system("shutdown /s /t 1")

    # -------------------------
    # RESTART PC
    # -------------------------
    elif 'restart' in command:
        talk('Restarting computer')
        os.system("shutdown /r /t 1")

    # -------------------------
    # SEND WHATSAPP MESSAGE
    # -------------------------
    elif 'send whatsapp message' in command:

        talk('Sending WhatsApp message')

        # CHANGE NUMBER
        phone_number = "+919919761121"

        # CHANGE MESSAGE
        message = "Hello from Jarvis"

        # CURRENT TIME + 2 MINUTES
        now = datetime.now()

        hour = now.hour
        minute = now.minute + 2

        pywhatkit.sendwhatmsg(
            phone_number,
            message,
            hour,
            minute
        )

    # -------------------------
    # EXIT
    # -------------------------
    elif 'exit' in command:
        talk('Goodbye')
        exit()

    # -------------------------
    # UNKNOWN COMMAND
    # -------------------------
    else:
        talk("I didn't understand")

# =========================
# START JARVIS
# =========================

talk("Jarvis activated")

while True:
    run_jarvis()