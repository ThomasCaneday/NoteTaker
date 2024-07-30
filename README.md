# NoteTaker

This project provides tools to record audio from the microphone, save it as an MP3 file, and transcribe the recorded audio to text.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Recording Audio](#recording-audio)
  - [Transcribing Audio](#transcribing-audio)
- [Contributing](#contributing)

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/thomascaneday/notetaker.git
    cd notetaker
    ```

2. Install the required libraries using `requirements.txt`:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Recording Audio

1. Run the `record.py` script to start recording audio:

    ```sh
    python record.py
    ```

2. Press `Enter` to stop the recording. The audio will be saved as `recording.wav` and `recording.mp3`.

### Transcribing Audio

1. Run the `transcribe.py` script to transcribe the recorded audio:

    ```sh
    python transcribe.py
    ```

2. The transcription will be saved in `transcription.txt` and printed in the console.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.
