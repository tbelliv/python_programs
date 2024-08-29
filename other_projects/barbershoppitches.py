import os  # for interacting with the operating system (creating directories)
import subprocess  # for executing external commands (downloading, converting audio)
import numpy as np  # for numerical computations (not used in this code, but typically for array handling)
import pandas as pd  # for data manipulation (used for organizing pitch and role data)
import matplotlib.pyplot as plt  # for plotting data (visualizing pitch classification)
import librosa  # for audio processing (loading and analyzing audio files)
import librosa.display  # for visualizing audio data (not used directly here)
import mplcursors  # for interactive plotting (adding hover annotations to the plot)

def download_audio(youtube_url, output_path='path.mp3'):
    """
    download audio from youtube using yt-dlp
    arguments:
    - youtube_url: url of the youtube video to download audio from
    - output_path: path where the downloaded audio will be saved (default: 'path.mp3')
    """
    # execute yt-dlp command to extract audio in mp3 format
    subprocess.run(['yt-dlp', '--extract-audio', '--audio-format', 'mp3', '-o', output_path, youtube_url])

def convert_audio_to_wav(input_path='path.mp3', output_path='path.wav'):
    """
    convert mp3 audio file to wav format using ffmpeg
    arguments:
    - input_path: path to the input mp3 file (default: 'path.mp3')
    - output_path: path to save the converted wav file (default: 'path.wav')
    """
    # create the output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    # execute ffmpeg command to convert mp3 to wav
    subprocess.run(['ffmpeg', '-i', input_path, output_path])

def analyze_audio(file_path='path.wav'):
    """
    analyze audio to extract pitch data using librosa
    arguments:
    - file_path: path to the wav file to analyze (default: 'path.wav')
    returns:
    - notes: a list of detected pitches from the audio file
    """
    # load the audio file and extract audio time series (y) and sample rate (sr)
    y, sr = librosa.load(file_path)
    
    # extract pitches and magnitudes from the audio using librosa's piptrack method
    pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)
    
    notes = []  # list to store detected pitches
    
    # iterate through each time step (t) in the audio
    for t in range(pitches.shape[1]):
        # find the index of the pitch with the highest magnitude at time t
        index = magnitudes[:, t].argmax()
        
        # get the pitch value at the found index
        pitch = pitches[index, t]
        
        # add pitch to the notes list if it's greater than 0 (valid pitch)
        if pitch > 0:
            notes.append(pitch)
    
    return notes  # return the list of detected pitches

def classify_role(pitch):
    """
    classify the role (e.g., tenor, lead, baritone, bass) based on the pitch
    arguments:
    - pitch: the pitch value in Hz
    returns:
    - the classified role as a string
    """
    # categorize pitch into voice parts (barbershop roles) based on thresholds
    if pitch > 1000:  # tenor has the highest pitch range
        return 'tenor'
    elif pitch > 600:  # lead has a high but lower range than tenor
        return 'lead'
    elif pitch > 400:  # baritone has a middle range
        return 'baritone'
    else:  # bass has the lowest pitch range
        return 'bass'

def main(youtube_url, song_name):
    """
    main function to download audio, convert it, analyze pitches, classify them by role, and visualize the results
    arguments:
    - youtube_url: url of the youtube video to analyze
    - song_name: name of the song for display in the plot title
    """
    # step 1: download audio from youtube
    download_audio(youtube_url)
    
    # step 2: convert the downloaded audio to wav format
    convert_audio_to_wav()
    
    # step 3: analyze the wav file to extract pitches
    notes = analyze_audio()
    
    # step 4: classify each pitch into a barbershop role
    roles = [classify_role(pitch) for pitch in notes]
    
    # step 5: create a pandas dataframe to hold the pitch and role data for plotting
    df = pd.DataFrame({'Pitch': notes, 'Role': roles})
    
    # step 6: plot the classified pitches
    plt.figure(figsize=(10, 6))  # create a figure with a specified size
    
    # scatter plot with pitch on y-axis and time (index) on x-axis
    scatter = plt.scatter(df.index, df['Pitch'], c=pd.factorize(df['Role'])[0], cmap='viridis', s=10)
    
    # add a legend to indicate roles based on color mapping
    handles, labels = scatter.legend_elements()
    labels = df['Role'].unique()  # get unique role labels
    plt.legend(handles, labels, title="Roles")
    
    # label the axes
    plt.xlabel('Time')
    plt.ylabel('Pitch (Hz)')
    
    # set the title of the plot to include the song name
    plt.title(f'Pitch Classification by Barbershop Roles - {song_name}')
    
    # step 7: add hover functionality to display pitch and role details
    cursor = mplcursors.cursor(scatter, hover=True)  # enable hover on the scatter plot
    
    @cursor.connect("add")
    def on_add(sel):
        """
        event handler for hover functionality; displays annotations with song name, role, and pitch
        arguments:
        - sel: the selected point in the plot
        """
        idx = sel.index  # get the index of the selected point
        role = df.iloc[idx]['Role']  # get the role at that index
        pitch = df.iloc[idx]['Pitch']  # get the pitch at that index
        
        # set the annotation text to display song name, role, and pitch (rounded to 2 decimal places)
        sel.annotation.set(text=f'Song: {song_name}\nRole: {role}\nPitch: {pitch:.2f} Hz')
    
    # step 8: display the plot
    plt.show()

# example of using the main function with a youtube url and song name
youtube_url = 'https://www.youtube.com/watch?v=AKWSlX4dVeQ'
song_name = ' The Newfangled Four • Zazz (from The Prom) • 2024 International Quartet Quarterfinals '
main(youtube_url, song_name)