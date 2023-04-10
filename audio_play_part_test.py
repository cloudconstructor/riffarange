import pygame
import tkinter as tk
from tkinter import ttk

pygame.init()

root = tk.Tk()

# Load audio file
audio_file = "../my_audio_file.wav"
pygame.mixer.music.load(audio_file)

# Define start and end time in seconds
start_time = 5.0
end_time = 10.0

# Play audio from start_time to end_time
pygame.mixer.music.play(start=start_time)

# Wait for audio to finish playing
pygame.time.wait(int((end_time - start_time) * 1000))

# Stop audio playback
pygame.mixer.music.stop()

# Create a Tkinter button to play the audio
def play_audio():
    pygame.mixer.music.play()

play_button = ttk.Button(root, text="Play Audio", command=play_audio)
play_button.pack()

root.mainloop()