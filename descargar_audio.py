import yt_dlp
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener la ruta de ffmpeg desde el archivo .env
FFMPEG_PATH = os.getenv("FFMPEG_PATH")  # Si no encuentra la variable, usa "ffmpeg" por defecto


def descargar_audio(url):
    ruta=os.path.join(os.getcwd(),'audio')
    if not os.path.exists(ruta):
        os.makedirs(ruta)
    opciones = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(ruta, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp3',
        'ffmpeg_location': FFMPEG_PATH,  # Usa la variable de entorno
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': False,
    }

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
        print("✅ Descarga completada con éxito.")
    except Exception as e:
        print("❌ Error durante la descarga:", e)

url = input("Ingrese la URL del audio: ")
print("Descargando el audio...")
descargar_audio(url)