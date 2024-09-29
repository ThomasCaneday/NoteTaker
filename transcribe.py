import speech_recognition as sr
from pydub import AudioSegment
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# This file will be used instead of transcribe.py for future use 9/12/24

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def split_audio(audio_path, chunk_length_ms=60000):
    """
    Splits the audio file into chunks of specified length.

    Parameters:
    audio_path (str): Path to the audio file.
    chunk_length_ms (int): Length of each chunk in milliseconds.

    Returns:
    list: List of chunk file paths.
    """
    audio = AudioSegment.from_file(audio_path)
    chunks = []
    total_length = len(audio)
    for i in range(0, total_length, chunk_length_ms):
        chunk = audio[i:i + chunk_length_ms]
        chunk_filename = f"chunk_{i // chunk_length_ms}.wav"
        chunk.export(chunk_filename, format="wav")
        chunks.append(chunk_filename)
    print("Total chunks to transcribe: " + str(len(chunks)))
    return chunks

def transcribe_chunk(recognizer, audio_file):
    """
    Transcribes a single audio chunk and calculates transcribed chunk ratio.

    Parameters:
    recognizer (sr.Recognizer): An instance of Recognizer.
    audio_file (str): Path to the audio chunk.

    Returns:
    str: Transcribed text for the chunk.
    int: Ratio of transcribed chunks.
    """
    transcribed_chunk = 0
    total_chunks = 0
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            print(f"Transcribed {audio_file}")
            transcribed_chunk += 1
            total_chunks += 1
        except sr.UnknownValueError:
            print(f"Could not understand audio in {audio_file}")
            text = ""
            transcribed_chunk -= 1
            total_chunks += 1
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            text = ""
    chunk_ratio = transcribed_chunk / total_chunks
    return text, chunk_ratio

def transcribe_audio(audio_file):
    """
    Transcribes audio chunks into a text variable.

    Parameters:
    audio_file (str): Path to the audio file.

    Returns:
    str: Text variable.
    """
    recognizer = sr.Recognizer()
    # Split audio into chunks
    chunks = split_audio(audio_file)
    full_transcription = ""

    for chunk in chunks:
        transcription, ratio = transcribe_chunk(recognizer, chunk)
        full_transcription += transcription + " "
        # Optionally, remove the chunk file after transcription
        os.remove(chunk)
    print("Transcribed chunk ratio: " + str(ratio))

    return full_transcription.strip()

def ask_for_file():
    print("Enter name of audio file to be transcribed (w/o extension, e.g., .mp3):")
    audio_file = input().strip()
    audio_file += ".mp3"
    if not os.path.isfile(audio_file):
        print(f"File '{audio_file}' does not exist. Please check the name and try again.")
        return ask_for_file()
    return audio_file

def write_variable_to_txt(variable):
    """
    Writes the contents of a variable to a text file.

    Parameters:
    variable (str): The content to be written to the file.
    """
    print("Enter name of transcription text file to write to (without .txt):")
    new_text_file = input().strip()
    text_file = new_text_file + ".txt"
    with open(text_file, 'w', encoding='utf-8') as file:
        file.write(str(variable))
    print(f"Transcription saved to {text_file}")

def main():
    audio_file = ask_for_file()
    transcribed_text = transcribe_audio(audio_file)
    write_variable_to_txt(transcribed_text)
    print("\nTranscribed Text:\n", transcribed_text)

if __name__ == "__main__":
    main()
