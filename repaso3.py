import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("img/rot.jpg")
img_new="img/rot-nuevo.jpg"

gris=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
suavizado=cv2.GaussianBlur(gris, (5,5), 0)
bordes=cv2.Canny(suavizado, 80, 180)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
BordesCerrados=cv2.morphologyEx(bordes,cv2.MORPH_CLOSE, kernel)

contornos, _ = cv2.findContours(BordesCerrados, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
mascara= np.zeros(gris.shape, dtype=np.uint8)

if contornos:
    contorno_mayor = max(contornos, key=cv2.contourArea)
    cv2.drawContours(mascara, [contorno_mayor], -1,255,-1)
fondo = np.zeros_like(img)
fondo[:]=[255,0,0]

resultado = img.copy()
resultado[mascara==0]= fondo[mascara==0]

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Imagen Original")
plt.axis("off")


plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB))
plt.title("Imagen Bordes cerrados")
plt.axis("off")

plt.tight_layout()
plt.show()

