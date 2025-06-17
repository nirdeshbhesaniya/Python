import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import pygame
import os
import google.generativeai as genai

# CONFIGURATION
newsapi = "e35eff5fdd8848ed8280a242b412862a"
gemini_api_key = "AIzaSyAtDyldSoilNiJZu0o475i3-Ri_zReGGdk"

# Initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()
pygame.mixer.init()

# Set up Gemini
genai.configure(api_key=gemini_api_key)
gemini_model = genai.GenerativeModel("models/gemini-1.5-flash")

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    try:
        prompt = f"Respond briefly: {command}"
        response = gemini_model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Gemini error: {e}"

def processCommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif c.startswith("play"):
        song = c.split(" ", 1)[-1].strip()
        if song in musicLibrary.music:
            webbrowser.open(musicLibrary.music[song])
            speak(f"Playing {song}")
        else:
            speak(f"{song} not found in your music library.")
    elif "news" in c:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
            if r.status_code == 200:
                articles = r.json().get("articles", [])[:5]
                for article in articles:
                    speak(article["title"])
            else:
                speak("Failed to fetch news.")
        except Exception as e:
            speak(f"News error: {e}")
    else:
        output = aiProcess(c)
        speak(output)

def listen_for_speech(timeout=5, phrase_limit=5):
    with sr.Microphone(sample_rate=16000) as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_limit)
        return recognizer.recognize_google(audio)

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        try:
            print("Say 'Jarvis' to activate...")
            wake = listen_for_speech(timeout=5, phrase_limit=3)
            if "jarvis" in wake.lower():
                speak("Yes?")
                try:
                    command = listen_for_speech()
                    processCommand(command)
                except sr.UnknownValueError:
                    speak("Sorry, I didn't catch that.")
                except Exception as e:
                    speak(f"Command error: {e}")
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except OSError as e:
            speak("Microphone error. Check your audio input.")
            print("OS Error:", e)
        except Exception as e:
            print("Error:", e)
