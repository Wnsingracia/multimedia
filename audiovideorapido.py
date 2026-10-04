import os
import edge_tts
from IPython.display import Audio, display
import asyncio

ruta_aud = "audio/b.mp3"
voz = "es-AR-ElenaNeural"

texto = "Casi todos sabemos quereeeer, Pero pocos sabemos amaaaaaar, Es que amar y querer no es igual, Amar es sufrir... querer es gozar"
comunicador = edge_tts.Communicate(
    text=texto,
    voice=voz,
    rate="-30%",
    pitch="+10Hz"
)

asyncio.run(comunicador.save(ruta_aud))

print("Audio generado")
display(Audio(ruta_aud))
