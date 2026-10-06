import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("img/rot.jpg")
img_new="img/rot-nuevo.jpg"

gris=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
suavizado=cv2.GaussianBlur(gris, (5,5), 0)
bordes=cv2.Canny(suavizado, 80, 180)

kernel = np.ones((2,2), np.uint8)
BordesGruesos=cv2.dilate(bordes, kernel, iterations=1)

resplandor=cv2.GaussianBlur(BordesGruesos,(25,25),0)

intensidad=(resplandor/225.0)[:,:,np.newaxis]

color_resplandor=np.array([20,75,160],dtype=np.float32)
capa_luz=intensidad*color_resplandor

resultador_f=img.astype(np.float32)+(capa_luz+1.2)
resultado=np.clip(resultador_f,0,255).astype(np.uint8)
resultado[BordesGruesos>0]=[255,0,0]

cv2.imwrite(img_new, resultado)
print("Imagen Guardada")
print(img_new)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Imagen Original")
plt.axis("off")


plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB))
plt.title("Imagen Bordes elaborados")
plt.axis("off")

plt.tight_layout()
plt.show()
