import speech_recognition as sr
import sys

# Keine Datei angegeben (verwende Mikrofon)
if len(sys.argv) == 1:
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Höre zu...")
		audio = r.listen(source)
else: # WAV-Datei ist als Kommandozeilen-Argument mitgegeben
	r = sr.Recognizer()
	with sr.AudioFile(sys.argv[1]) as source:
		audio = r.listen(source)

print(r.recognize_google(audio, language="de_DE"))
