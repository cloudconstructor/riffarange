import pygame
import numpy as np

pygame.init()

# Load audio file
audio_file = "../my_audio_file.wav"
audio_data, frame_rate = pygame.sndarray.array(pygame.mixer.Sound(audio_file))

# Create time vector
num_frames = len(audio_data)
time = np.arange(0, num_frames) / frame_rate

# Create plot
plot_size = (640, 480)
screen = pygame.display.set_mode(plot_size)
pygame.display.set_caption("Audio Waveform")
plot_color = (255, 255, 255)
line_width = 2
x_scale = plot_size[0] / num_frames
y_scale = plot_size[1] / (2 * np.max(np.abs(audio_data)))

for i in range(1, num_frames):
    pygame.draw.line(screen, plot_color, ((i-1)*x_scale, plot_size[1]/2 - audio_data[i-1]*y_scale),
                     (i*x_scale, plot_size[1]/2 - audio_data[i]*y_scale), line_width)

# Display plot and wait for user to close window
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
