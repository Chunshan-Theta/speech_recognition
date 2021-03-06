#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

print("recognizing,wait...")
# recognize speech using Sphinx
try:
    print("Sphinx thinks you said(offline) : " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))


# recognize speech using Houndify
HOUNDIFY_CLIENT_ID = "97SVPMnz1w7T0wzKB8L79w==" # Houndify client IDs are Base64-encoded strings
HOUNDIFY_CLIENT_KEY = "cFtuYqMdyK5yRz17kQQi5iqeQ9wTc9MUwXLei5abPTbLMrl2ZLkcBCFFi9hOc-6Fwtx6dR2tc4BhkT5AYBh_mw==" # Houndify client keys are Base64-encoded strings
try:
    print("Houndify thinks you said : " + r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))
except sr.UnknownValueError:
    print("Houndify could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Houndify service; {0}".format(e))

# recognize speech using api.ai
API_AI_CLIENT_ACCESS_TOKEN = "851d755279ef40fcb7394fd5e058fe9b" # api.ai keys are 32-character lowercase hexadecimal strings
try:
    print("api.ai thinks you said : " + r.recognize_api(audio, client_access_token=API_AI_CLIENT_ACCESS_TOKEN))
except sr.UnknownValueError:
    print("api.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from api.ai service; {0}".format(e))


# recognize speech using Wit.ai
WIT_AI_KEY = "G4R357JHVZI2B62KG7VFVZAKJPMHVBWW" # Wit.ai keys are 32-character uppercase alphanumeric strings
try:
    print("Wit.ai thinks you said(Free): " + r.recognize_wit(audio, key=WIT_AI_KEY))
except sr.UnknownValueError:
    print("Wit.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Wit.ai service; {0}".format(e))



