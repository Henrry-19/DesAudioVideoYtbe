import yt_dlp


import os
from dotenv import load_dotenv

load_dotenv()

# Función que descarga un video de YouTube
FFMPEG_PATH = os.getenv("FFMPEG_PATH")

"""

if FFMPEG_PATH:
    print(f"✅ Ruta de FFMPEG cargada desde .env: {FFMPEG_PATH}")
else:
    print("❌ No se pudo cargar la variable FFMPEG_PATH desde .env")

"""
#Comentarios en Python: ... // 
def descargar_youtube(url):
    # Crear la carpeta 'video' si no existe
    ruta_video = os.path.join(os.getcwd(), 'video')
    if not os.path.exists(ruta_video):
        os.makedirs(ruta_video)

    opciones = {

        'format': 'bestvideo[height<=?720]+bestaudio/best',
        'outtmpl': os.path.join(ruta_video, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'ffmpeg_location': FFMPEG_PATH,  # Usa la variable de entorno
    }


    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
        print("✅ Descarga completada con éxito.")
    except Exception as e:
        print("❌ Error durante la descarga:", e)

# Ingresar la URL del video de YouTube
url = input("Ingrese la URL del video de YouTube: ")
print("Descargando el video...")
descargar_youtube(url)

