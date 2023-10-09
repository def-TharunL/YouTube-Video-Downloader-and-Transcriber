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


To run the provided Python script and start the Flask web application, follow these steps:

1. **Install Dependencies:**

   Make sure you have the required Python libraries installed. You can install them using pip:

   ```bash
   pip install flask pytube3 whisper
   ```

   This will install Flask, pytube, and whisper libraries.

2. **Run the Script:**

   Run the Python script by executing the following command in your terminal:

   ```bash
   python your_script_file.py
   ```

   Replace `your_script_file.py` with the actual name of your Python script.

3. **Access the API:**

   Once the script is running, you can access the API endpoints using an HTTP client like `curl`, Postman, or by sending a request from your code.

   Example using `curl` to send a POST request to the `/download_and_transcribe` endpoint:

   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"url": "https://www.youtube.com/watch?v=your_youtube_video_id"}' http://127.0.0.1:5000/download_and_transcribe
   ```

   Replace `"https://www.youtube.com/watch?v=your_youtube_video_id"` with the actual YouTube video URL.

   The Flask app will process the request, download the audio from the specified YouTube video, transcribe it, and provide the transcription result in the response.

4. **Access the Application:**

   Open a web browser and navigate to `http://127.0.0.1:5000` to access the web application and use it through a user interface if one is implemented in the script.

Keep in mind that the script is set to run in debug mode (`app.run(debug=True)`), which is suitable for development. For production deployment, consider configuring the app accordingly for security and performance.
