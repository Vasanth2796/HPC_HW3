import cv2
from matplotlib import pyplot as plt
  
# Read the image. 
img = cv2.imread('messi5.jpg') 
  
# Apply bilateral filter with d = 85,
# sigmaColor = sigmaSpace = 75.
bilateral = cv2.bilateralFilter(img, 85, 75, 75)
# Save the output. 
cv2.imwrite('bilateral.jpg', bilateral) 

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(bilateral, cv2.COLOR_BGR2RGB))
plt.show()