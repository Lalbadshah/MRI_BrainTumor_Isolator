import cv2
import numpy as np

cap = cv2.imread('MRI-Brain.jpg')

boundaries = [
	([150, 150, 150], [180, 180, 180])
	
	]


while(True):
	image = cap

	for (lower,upper) in boundaries:
		
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")

		mask = cv2.inRange(image,lower,upper)
		output = cv2.bitwise_and(image, image, mask = mask)
		
		
		cv2.imshow("Keypoints", output)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()	
