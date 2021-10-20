#To detect corner or chess board 

import cv2
import numpy as np 
 
img = cv2.imread("chess.jfif")
cv2.imshow("Chess",img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
#(src, blockSize, ksize, k)
dest = cv2.cornerHarris(gray, 2, 3, 0.04)

dest = cv2.dilate(dest, None)

img[dest > 0.01 * dest.max()] = (0,0,255)

cv2.imshow("Destination", img)
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()