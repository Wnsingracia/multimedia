import cv2
import matplotlib.pyplot as plt

img = cv2.imread("img/rot.jpg")

gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bordes = cv2.Canny(gris, 100, 200)
resultado = img.copy()

resultado[bordes>0]=[0,0,225]

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Imagen original")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB))
plt.title("Imagen bordes resaltados")
plt.axis("off")

plt.tight_layout()
plt.show()