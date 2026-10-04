import os
import matplotlib.pyplot as plt
import cv2


dir_frames="frames/saori"
imagenes = os.listdir(dir_frames)
imagenes.sort()

print("total de frames ", len(imagenes))
print("Primeros 5", imagenes[:5])

frames_prueba = cv2.imread(dir_frames+"/"+imagenes[201])
frames_rgb = cv2.cvtColor(frames_prueba, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(8,4))
plt.imshow(frames_rgb)
plt.axis("off")
plt.title("frame")
plt.show()

frame_ejemplo = cv2.imread(dir_frames+"/"+imagenes[10])
alto, ancho = frame_ejemplo.shape[:2]
print("alto ", alto, " ancho ", ancho)
codec= cv2.VideoWriter_fourcc(*'mp4v')
video_salida= cv2.VideoWriter("video/saori_rebirth.mp4", codec, 30, (ancho,alto))
for imagen in imagenes:
    ruta_frame = os.path.join(dir_frames, imagen)  # Usa 'imagen' directamente
    frame = cv2.imread(ruta_frame)
    if frame is None:
        continue
    frame = cv2.resize(frame, (ancho, alto))
    video_salida.write(frame)

video_salida.release()
print("video rebirth terminado con éxito")