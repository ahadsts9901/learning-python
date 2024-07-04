import pyjokes
import pyttsx3

joke = pyjokes.get_joke()

print(joke)
pyttsx3.speak(joke)