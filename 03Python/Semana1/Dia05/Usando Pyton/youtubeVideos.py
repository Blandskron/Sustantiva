from pytube import YouTube

# URL del video de YouTube que deseas descargar
url = '####'

try:
    # Crear un objeto YouTube
    yt = YouTube(url)
    
    # Seleccionar la mejor calidad disponible
    video = yt.streams.get_highest_resolution()
    
    # Descargar el video en el directorio actual
    video.download()
    
    print("Descarga exitosa!")
except Exception as e:
    print("Ocurrió un error durante la descarga:", str(e))
