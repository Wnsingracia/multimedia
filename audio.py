import edge_tts
import asyncio

texto = "No soy gay pero soy peruano y tengo una fantasía donde Perú invade Chile y Chile tiene que exportar esclavos femboys para satisfacer oficiales peruanos de alto rango. Me imagino que soy un comandante poderoso, alto, con mandíbula cuadrada y músculos masivos. Mi femboy es un pequeño chileno tímido con piel pálida que viene a mi habitación. Lo agarro con mis poderosos brazos y lo beso a la fuerza, presionando su pecho contra el mío."
voz = "es-GQ-JavierNeural"
ruta = "audio/a.mp3"

async def generar_audio():
    comunicado = edge_tts.Communicate(texto, voz)
    await comunicado.save(ruta)

asyncio.run(generar_audio())
print("audio generado en ", ruta)