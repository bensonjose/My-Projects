'''Importing the gtts module.
What is gTTS module in Python?
gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API. '''

from gtts import gTTS

# Specifying the language of the Speech.

language="en"

# Specifying the text /Sentence you want to convert to Speech.

text="Hello, This's how I work.I can speak Slow or Fast as per your requirement.I can speak in the language you wish also i can imitate a particuar accent if you wish me to do so. Have a Nice Day!!"

# Here, You Specify the speed of the speech, also you can mention any particular accent if you want.

speech=gTTS(text=text,lang=language,slow=False,tld="com.au")


# Finally we Save this into an Audio File(MP3 File) 
# First we've to run the Program and the play the MP3 File that we just created!


speech.save("textToSpeech.mp3")