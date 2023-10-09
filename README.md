## YouTube Video Downloader and Transcriber

This Python application, built with Flask, allows users to download YouTube videos as audio and transcribe them into text using the "whisper" library.

### Features:

1. **Video Download as Audio:**
   Users can input a YouTube video URL, and the application will download the video as audio (in MP3 format).

2. **Transcription:**
   The downloaded audio is transcribed into text using the "whisper" library.

### Code Structure:

- **`app.py`**: The main script implementing the Flask application. It defines a Flask route (`/download_and_transcribe`) for video downloading and transcription.

- **`generate_random_filename`**: A utility function to generate a random single-digit filename that hasn't been used before.

- **`download_and_transcribe`**: Flask route handler for the `/download_and_transcribe` endpoint. It processes the YouTube URL provided, downloads the video as audio, generates a random filename, transcribes the audio, and returns the results.

- **`requirements.txt`**: A file listing the required Python packages and their versions for this application.

### Usage:

1. Clone the repository and navigate to the project directory.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask application using `python app.py`.
4. Send a POST request to `http://localhost:5000/download_and_transcribe` with a JSON payload containing the YouTube URL to download and transcribe a video.
