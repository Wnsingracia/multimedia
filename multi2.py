import cv2
import numpy as np
import matplotlib.pyplot as plt

mono = cv2.imread("mono.png")
plt.imshow(cv2.cvtColor(mono,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()

y1, y2 = 80, 450
x1, x2 = 200, 700

cabeza =mono[y1:y2, x1:x2]
plt.imshow(cv2.cvtColor(cabeza,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
