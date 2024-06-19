# speech_recognition_using_vosk
In this project we are converting speech to text using vosk library and numpy.
Steps:-
1)First we import the installed vosk model.We also import KaldiRecognizer to use it as a speech recognizer.
2)We also import pyaudio and numpy which we are going to use in our project
3)model is a variable which is used to store the path where our vosk dependency is installed.
4)recognizer is a variable used to recognize audio with a frequency of 16000Hz.
5)Now we setup a mic for speech input.
6)Audio input from mic with following specifications will be catched by the recognizer.
7)Now we start the audio stream
8)silence threshold and silence duration are used to detect silence and depending on their value,system automatically stops listening when nothing is being said.
9)after entering a loop we check if audio volume level is less than the threshold in which case system stops listening,otherwise,we get text as output.

