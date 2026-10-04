import os
import subprocess
try:
    import imageio_ffmpeg
    ffmpeg_bin = imageio_ffmpeg.get_ffmpeg_exe()
except ImportError:
    ffmpeg_bin = shutil.which("ffmpeg")

ruta_vid = "video/Melman.mp4"
ruta_aud = "audio/b.mp3"

ruta_f = "video/videoaudio.mp4"

if os.path.exists(ruta_vid) and os.path.exists(ruta_aud):
    size_video = os.path.getsize(ruta_vid)
    size_audio = os.path.getsize(ruta_aud)
    print("Tamanio video: ", size_video, " bytes")
    print("Tamanio audio: ", size_audio, " bytes")
    if size_video == 0 or size_audio == 0:
        print("Error, tamanio 0")
    else:
        print("valido, uniendo")
        cmd=[
            ffmpeg_bin, "-y",
            "-i", ruta_vid,
            "-i", ruta_aud,
            "-map", "0:v:0",
            "-map", "1:a:0",
            "-c:v", "copy",
            "-c:a", "aac",
            "-shortest",
            ruta_f
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode==0:
            print("Completado, guardado en: ", ruta_f)
        else:
            print("Error")
else:
    print("Archivos no encontrados")
