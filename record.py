import pyaudio
import wave
import threading
from pydub import AudioSegment

# Audio recording parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1  # Change to 1 for mono if the microphone does not support stereo
RATE = 44100
CHUNK = 1024
WAVE_OUTPUT_FILENAME = "recording.wav"
MP3_OUTPUT_FILENAME = "recording.mp3"

frames = []
recording = True

def record_audio():
    global frames, recording

    audio = pyaudio.PyAudio()

    # Start recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("Recording... Press Enter to stop.")

    while recording:
        data = stream.read(CHUNK)
        frames.append(data)

    # Stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded data as a WAV file
    wave_file = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(audio.get_sample_size(FORMAT))
    wave_file.setframerate(RATE)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()

def convert_wav_to_mp3():
    audio = AudioSegment.from_wav(WAVE_OUTPUT_FILENAME)
    audio.export(MP3_OUTPUT_FILENAME, format="mp3")
    print(f"Saved as {MP3_OUTPUT_FILENAME}")

def stop_recording():
    global recording
    recording = False

def listen_for_key_press():
    input("Press Enter to stop recording...\n")
    stop_recording()

if __name__ == "__main__":
    # Start recording in a separate thread
    recording_thread = threading.Thread(target=record_audio)
    recording_thread.start()

    # Start listening for key press in the main thread
    listen_for_key_press()

    # Wait for the recording thread to finish
    recording_thread.join()

    # Convert to MP3
    convert_wav_to_mp3()
