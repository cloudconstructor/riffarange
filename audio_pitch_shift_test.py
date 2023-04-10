from pydub import AudioSegment
from pydub.effects import change_pitch

# Load audio file
audio_file = "../my_audio_file.wav"
audio = AudioSegment.from_file(audio_file)

# Pitch shift audio by 2 semitones
shifted_audio = change_pitch(audio, 200)

# Export pitch shifted audio file
shifted_audio.export("shifted_audio.wav", format="wav")