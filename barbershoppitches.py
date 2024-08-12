import os
import subprocess
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import librosa
import librosa.display
import mplcursors

def download_audio(youtube_url, output_path='/home/timothy/Documents/python_programs/mp3/output.mp3'):
    # Download audio using yt-dlp
    subprocess.run(['yt-dlp', '--extract-audio', '--audio-format', 'mp3', '-o', output_path, youtube_url])

def convert_audio_to_wav(input_path='/home/timothy/Documents/python_programs/mp3/output.mp3', output_path='/home/timothy/Documents/python_programs/mp3/output.wav'):
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    # Convert mp3 to wav using ffmpeg
    subprocess.run(['ffmpeg', '-i', input_path, output_path])

def analyze_audio(file_path='/home/timothy/Documents/python_programs/mp3/output.wav'):
    y, sr = librosa.load(file_path)
    pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)
    notes = []
    for t in range(pitches.shape[1]):
        index = magnitudes[:, t].argmax()
        pitch = pitches[index, t]
        if pitch > 0:
            notes.append(pitch)
    return notes

def classify_role(pitch):
    if pitch > 1000:  # Example threshold, adjust based on actual pitch ranges
        return 'tenor'
    elif pitch > 600:
        return 'lead'
    elif pitch > 400:
        return 'baritone'
    else:
        return 'bass'

def main(youtube_url, song_name):
    # Download and convert audio
    download_audio(youtube_url)
    convert_audio_to_wav()
    
    # Analyze audio
    notes = analyze_audio()
    
    # Classify roles
    roles = [classify_role(pitch) for pitch in notes]
    
    # Create a DataFrame for analysis
    df = pd.DataFrame({'Pitch': notes, 'Role': roles})
    
    # Display the results
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(df.index, df['Pitch'], c=pd.factorize(df['Role'])[0], cmap='viridis', s=10)
    
    # Add legend
    handles, labels = scatter.legend_elements()
    labels = df['Role'].unique()
    plt.legend(handles, labels, title="Roles")
    
    plt.xlabel('Time')
    plt.ylabel('Pitch (Hz)')
    plt.title(f'Pitch Classification by Barbershop Roles - {song_name}')
    
    # Add interactive hover
    cursor = mplcursors.cursor(scatter, hover=True)
    
    @cursor.connect("add")
    def on_add(sel):
        idx = sel.index
        role = df.iloc[idx]['Role']
        pitch = df.iloc[idx]['Pitch']
        sel.annotation.set(text=f'Song: {song_name}\nRole: {role}\nPitch: {pitch:.2f} Hz')
    
    plt.show()

# Example usage
youtube_url = 'https://www.youtube.com/watch?v=fJ9rUzIMcZQ'
song_name = 'Queen – Bohemian Rhapsody (Official Video Remastered)'
main(youtube_url, song_name)
