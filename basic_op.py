import cv2
import numpy as np

img = cv2.imread ('image/cat.jpg')

img [100, 100] = [255, 255, 255]	
# position x = 100, y = 100 change value to 255 255 255

print img.shape		# rows, columns, channels
print img.size 		# pixels
print img.dtype		# datatype

cv2.imshow ('image', img)
cv2.waitKey (0)
cv2.destroyAllWindows ()