import cv2

ruta_video = "video/si.mp4"
video = cv2.VideoCapture(ruta_video)

if not video.isOpened():
    print("Error")
else:
    print("Mucho video")

contador=1
while True:
    retorno, frame = video.read()
    if not retorno:
        break
    ruta_frame = "frames/si/imagen"+str(contador)+".png"
    cv2.imwrite(ruta_frame, frame)
    contador+=1
video.release()
print("frames extraidos", contador-1)

