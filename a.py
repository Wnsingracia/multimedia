import cv2
import numpy as np

archivo = "./img/yeti.jpg"

image = cv2.imread(archivo)

cv2.imshow("Imagen original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("Valor del pixel:", image[2, 2, 2])
print("Shape:", image.shape)
print("Alto:", len(image))
print("Ancho:", len(image[0]))
print("Canales:", len(image[0, 0]))


imagenB = image[:, :, 0]
imagenG = image[:, :, 1]
imagenR = image[:, :, 2]

cv2.imshow("Canal B", imagenB)
cv2.waitKey(0)
cv2.imshow("Canal G", imagenG)
cv2.waitKey(0)
cv2.imshow("Canal R", imagenR)
cv2.waitKey(0)
cv2.destroyAllWindows()


parte = np.zeros((71, 44), dtype=np.uint8)

l = 0

for i in range(70, 141):
    m = 0
    for j in range(109, 153):
        parte[l, m] = imagenR[i, j]
        m += 1

    l += 1


# Mostrar la parte recortada
cv2.imshow("Parte del canal R", parte)
cv2.waitKey(0)
cv2.destroyAllWindows()