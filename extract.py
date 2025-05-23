import speech_recognition as sr
from pydub import AudioSegment

# Path to the audio file
audio_path = "reflect-audio.wav"  # Change this to the correct path

# Convert to a format compatible with speech recognition (optional)
audio = AudioSegment.from_wav(audio_path)
audio.export("converted_audio.wav", format="wav")

# Initialize recognizer
recognizer = sr.Recognizer()

# Load the audio file
with sr.AudioFile("converted_audio.wav") as source:
    audio_data = recognizer.record(source)

# Transcribe the audio
try:
    transcription = recognizer.recognize_google(audio_data)
    print("Transcribed Text:\n", transcription)
except sr.UnknownValueError:
    print("Could not understand the audio.")
except sr.RequestError:
    print("Speech recognition service error.")
