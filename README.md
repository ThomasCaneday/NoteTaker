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

### Summarizing a Text File into Lecture Notes

1. Run the `summarize.py` script to summarize the content of a `.txt` file into lecture notes using OpenAI's GPT-4:

    ```sh
    python summarize.py
    ```

2. Ensure you provide the correct file path and OpenAI API key in the script. The summarized lecture notes will be printed in the console.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Trouble With Packages?
Creating a virtual environment (venv) can help manage dependencies and avoid conflicts between packages. Using a virtual environment is generally recommended for Python projects to ensure a clean, isolated environment. Here's how you can create and use a virtual environment:

1. **Create a Virtual Environment:**
   Navigate to your project directory and create a virtual environment by running:
   ```bash
   python -m venv venv
   ```
   This creates a `venv` directory in your project folder that contains a clean Python environment.

2. **Activate the Virtual Environment:**
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

   After activation, your terminal should show the name of the virtual environment (e.g., `(venv)`) at the beginning of the command line prompt.

3. **Upgrade `pip` and `setuptools` in the Virtual Environment:**
   ```bash
   pip install --upgrade pip setuptools
   ```

4. **Install the Required Packages:**
   Now, try installing the packages from your `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

5. **Deactivate the Virtual Environment:**
   When you're done working in the virtual environment, you can deactivate it by running:
   ```bash
   deactivate
   ```

Using a virtual environment can help avoid issues caused by conflicting dependencies and ensure that your project's dependencies are managed independently from other projects or the system Python installation.
