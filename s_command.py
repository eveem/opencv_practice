import numpy as numpy
import cv2

img = cv2.imread ('./image/cat.jpg', 0) # 0 is grayscale, 1 is original	

cv2.namedWindow ('image', cv2.WINDOW_NORMAL)	# can resize window
cv2.imshow ('image', img)
cv2.waitKey (0)
cv2.destroyAllWindows ()
