import customtkinter as ctk
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import pygame
import os
from dotenv import load_dotenv
import os
import google.generativeai as genai
from threading import Thread
from PIL import Image, ImageTk
import time
import itertools

# API Keys
load_dotenv()
NEWS_API = os.getenv("NEWS_API_KEY")
genai_api_key = os.getenv("GEMINI_API_KEY")
if not genai_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
recognizer.energy_threshold = 250
recognizer.pause_threshold = 0.6
recognizer.dynamic_energy_threshold = True

engine = pyttsx3.init()
pygame.mixer.init()


# Configure Gemini
genai.configure(api_key=genai_api_key)
gemini_model = genai.GenerativeModel("models/gemini-1.5-flash")

# Setup UI
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.title("Jarvis AI Assistant")
app.geometry("500x670")
app.resizable(False, False)

# Logo
logo_frame = ctk.CTkFrame(app, fg_color="transparent")
logo_frame.pack(pady=10)
try:
    logo_path = "assets/jarvis_logo.png"
    if os.path.exists(logo_path):
        logo_img = Image.open(logo_path).resize((80, 80))
        logo_img = ImageTk.PhotoImage(logo_img)
        logo_label = ctk.CTkLabel(logo_frame, image=logo_img, text="")
    else:
        raise FileNotFoundError
except:
    logo_label = ctk.CTkLabel(logo_frame, text="🧠", font=("Arial", 40))
logo_label.pack()

# Title
ctk.CTkLabel(app, text="Hi, I'm Jarvis", font=("Product Sans", 22, "bold")).pack(pady=5)

# Output box
output_box = ctk.CTkTextbox(app, width=460, height=340, font=("Consolas", 14), corner_radius=12)
output_box.pack(pady=10)
output_box.insert("end", "Jarvis is Ready. Say 'Jarvis' to activate.\n")

# Wave animation
wave_label = ctk.CTkLabel(app, text="", font=("Consolas", 26))
wave_label.pack()

def animate_wave():
    for wave in itertools.cycle([".", "..", "...", "....", "....."]):
        wave_label.configure(text=f"\U0001F3A4 Listening{wave}")
        time.sleep(0.4)
        if not listening_flag[0]:
            wave_label.configure(text="")
            break

def type_text(text, delay=0.012):
    output_box.insert("end", "\n")
    for char in text:
        output_box.insert("end", char)
        output_box.update()
        time.sleep(delay)
    output_box.insert("end", "\n")
    output_box.see("end")

def speak(text):
    type_text(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def local_ai(command):
    command = command.lower()
    if "your name" in command:
        return "I'm Jarvis, your AI assistant."
    elif "time" in command:
        return time.strftime("The time is %I:%M %p.")
    elif "creator" in command:
        return "I was created by Nirdesh."
    return "I'm not sure how to help with that."

def ai_process(command):
    try:
        prompt = f"Respond briefly: {command}"
        response = gemini_model.generate_content(prompt)
        return response.text.strip()
    except:
        return local_ai(command)

def process_command(cmd):
    cmd = cmd.lower()
    if "open google" in cmd:
        webbrowser.open("https://google.com")
    elif "open youtube" in cmd:
        webbrowser.open("https://youtube.com")
    elif "open facebook" in cmd:
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in cmd:
        webbrowser.open("https://linkedin.com")
    elif cmd.startswith("play"):
        song = cmd.split(" ", 1)[-1].strip()
        if song in musicLibrary.music:
            webbrowser.open(musicLibrary.music[song])
            speak(f"Playing {song}")
        else:
            speak(f"{song} not found in your music library.")
    elif "news" in cmd:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API}")
            if r.status_code == 200:
                articles = r.json().get("articles", [])[:5]
                for article in articles:
                    speak(article["title"])
            else:
                speak("Failed to fetch news.")
        except Exception as e:
            speak(f"News error: {e}")
    else:
        speak(ai_process(cmd))

def listen_for_speech(timeout=6, phrase_limit=6):
    with sr.Microphone(sample_rate=16000) as source:
        recognizer.adjust_for_ambient_noise(source, duration=1.2)
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_limit)
            return recognizer.recognize_google(audio)
        except sr.WaitTimeoutError:
            speak("No speech detected.")
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that.")
        except sr.RequestError:
            speak("Speech service is down.")
        return ""

def start_listening():
    try:
        speak("Say 'Jarvis' to activate.")
        listening_flag[0] = True
        Thread(target=animate_wave, daemon=True).start()

        wake = listen_for_speech(timeout=4, phrase_limit=3)
        if "jarvis" in wake.lower():
            speak("Yes, I'm listening.")
            command = listen_for_speech(timeout=5, phrase_limit=6)
            if command:
                process_command(command)
            else:
                speak("You didn't say anything.")
        else:
            speak("Wake word not detected.")
    except Exception as e:
        speak(f"Mic Error: {e}")
    finally:
        listening_flag[0] = False

def run_jarvis():
    Thread(target=start_listening, daemon=True).start()

listening_flag = [False]

mic_button = ctk.CTkButton(
    app,
    text="\U0001F399 Speak",
    font=("Arial", 18),
    command=run_jarvis,
    corner_radius=50,
    width=120,
    height=60,
    fg_color="#1DB954",
    hover_color="#1AA34A",
    text_color="white"
)
mic_button.pack(pady=20)

app.mainloop()
