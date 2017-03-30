import numpy as np
import cv2

img = np.zeros ((512, 512, 3), np.uint8)

# img = cv2.line (img, (0, 0), (511, 511), (250, 0, 0), 5)			 # draw line
# img = cv2.rectangle (img, (384, 0), (510, 128), (0, 255, 0), 3)	 # draw rectangle
# img = cv2.circle (img, (447, 63), 63, (0, 0, 255), -1)			 # draw circle
# img = cv2.ellipse (img, (256, 256), (100, 50), 0, 0, 180, 255, -1) # draw ellipse

cv2.imshow ('image', img)
cv2.waitKey (0)
cv2.destroyAllWindows ()