import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

# Ignore any warning messages
warnings.filterwarnings('ignore')

# Record audio and return as a string
def recordAudio():
  # Record the audio
  r = sr.Recognizer() # Creating a recognizer object
  # Open the microphone
  with sr.Microphone() as source:
    print('Say somethink!')
    audio = r.listen(source)
  # Use Google speech recognition
  data =''
  try:
    data = r.recognizw_google(audio)
    print('You said:'+data)
  except sr.UnknownValueError:
    print('Google Speech Recognitio could not understand the audio, unkown error')
  except sr.RequestError as e:
    print('Request result from Google Speech Recogition service error!'+e)

  return data

recordAudio()