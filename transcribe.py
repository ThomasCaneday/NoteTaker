import speech_recognition as sr
from pydub import AudioSegment
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_file(audio_file)

    # Convert audio to the desired format if necessary
    audio.export("temp.wav", format="wav")

    with sr.AudioFile("temp.wav") as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    
    return text

def ask_for_file():
    print("Enter name of audio file to be transcribed (without .mp3):")
    new_audio_file = input()
    audio_file = new_audio_file + ".mp3"
    return audio_file

# audio_file = "recording.mp3"
audio_file = ask_for_file()
transcribed_text = transcribe_audio(audio_file)

def write_variable_to_txt(variable, file_name):
    """
    Writes the contents of a variable to a text file.
    
    Parameters:
    variable (str): The content to be written to the file.
    file_name (str): The name of the file to write to (with .txt extension).
    """
    with open(file_name, 'w') as file:
        file.write(str(variable))

write_variable_to_txt(transcribed_text, 'transcription.txt')
print("Transcribed Text:\n", transcribed_text)
