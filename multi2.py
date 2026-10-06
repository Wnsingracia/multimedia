import cv2
import numpy as np
import matplotlib.pyplot as plt

mono = cv2.imread("mono.png")
plt.imshow(cv2.cvtColor(mono,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()

y1, y2 = 80, 450
x1, x2 = 200, 700

cabezam =mono[y1:y2, x1:x2]
plt.imshow(cv2.cvtColor(cabezam,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()

payaso = cv2.imread("payaso.jpeg")
plt.imshow(cv2.cvtColor(payaso,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
cv2.imwrite("cabezapayaso.jpeg", cabezam)

y1, y2 = 0, 270
x1, x2 = 100, 450

cabezap =payaso[y1:y2, x1:x2]
plt.imshow(cv2.cvtColor(cabezap,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
cv2.imwrite("cabezapayaso.jpeg", cabezap)

