import streamlit as st
import requests

# Define the Flask API endpoint
API_ENDPOINT = "http://127.0.0.1:5000/download_and_transcribe"

# Streamlit app
st.title("YouTube Audio Transcription")

# Get YouTube URL from user input
yt_url = st.text_input("Enter YouTube URL:")

# Handle user input and trigger API call
if st.button("Transcribe Audio"):
    if yt_url:
        # Prepare data for the API request
        data = {"url": yt_url}

        # Send a POST request to the Flask API
        response = requests.post(API_ENDPOINT, json=data)

        # Display results
        if response.status_code == 200:
            result = response.json()
            st.write("Title:", result["title"])
            st.write("Transcription Result:")
            st.write(result["transcription_result"])
        else:
            st.write("Error:", response.status_code)
            st.write("Failed to transcribe the audio.")

