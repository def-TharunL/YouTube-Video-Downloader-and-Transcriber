import os
import random
from flask import Flask, request, jsonify
from pytube import YouTube
import whisper

app = Flask(__name__)

# Function to generate a random single-digit filename that hasn't been used before
def generate_random_filename(used_numbers):
    while True:
        random_number = str(random.randint(0, 1000))
        if random_number not in used_numbers:
            used_numbers.add(random_number)
            return random_number

# Endpoint to download a video as audio and transcribe it
@app.route('/download_and_transcribe', methods=['POST'])
def download_and_transcribe():
    data = request.get_json()
    yt_url = data.get('url')

    # Download the video as audio
    yt = YouTube(yt_url)
    video = yt.streams.filter(only_audio=True).first()
    destination = data.get('destination', os.getcwd())
    out_file = video.download(output_path=destination)

    # Generate a random single-digit filename that hasn't been used before
    used_numbers = set()
    random_filename = generate_random_filename(used_numbers)
    new_file = os.path.join(destination, f'{random_filename}.mp3')
    os.rename(out_file, new_file)

    # Transcribe the audio
    model = whisper.load_model("base")
    result = model.transcribe(new_file)

    response = {
        'title': yt.title,
        'downloaded_file_path': new_file,
        'transcription_result': result['text']
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
