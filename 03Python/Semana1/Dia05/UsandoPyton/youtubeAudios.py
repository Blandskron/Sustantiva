from pytube import YouTube
from moviepy.editor import *

# URL del video de YouTube que deseas descargar
url = 'https://www.youtube.com/watch?v=og9ewQAioUk'

try:
    # Crear un objeto YouTube
    yt = YouTube(url)
    
    # Seleccionar el objeto de audio
    audio = yt.streams.filter(only_audio=True).first()
    
    # Descargar el audio en el directorio actual
    audio_path = audio.download()
    
    # Convertir el archivo de audio descargado a MP3
    audio_clip = AudioFileClip(audio_path)
    audio_clip.write_audiofile(audio_path[:-4] + '.mp3')
    audio_clip.close()
    
    print("Descarga exitosa del audio en formato MP3!")
except Exception as e:
    print("Ocurrió un error durante la descarga del audio:", str(e))
