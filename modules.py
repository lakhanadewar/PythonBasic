import pyttsx3
import art
from textblob import TextBlob
engine = pyttsx3.init()

# print(art.text2art("Ministry of Work!"))


# engine.say("I will speak this text")
# engine.runAndWait()

def polarity(text):
    return TextBlob(text).sentiment.polarity

print("Enter how was you day: ")
ip= input("> ")
pol=polarity(ip)

while pol < 0.5:
    print("Please write only Positive: ")
    ip= input("> ")
    pol=polarity(ip)

print("Thank You")
