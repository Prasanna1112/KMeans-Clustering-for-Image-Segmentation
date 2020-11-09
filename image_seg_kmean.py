import numpy as np
import cv2
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans

#Reading the original picture
picture = cv2.imread('picture.jpg')
(h1, w1) = picture.shape[:2]

#Reshaping the picture
picture = cv2.cvtColor(picture, cv2.COLOR_BGR2LAB)

picture = picture.reshape((picture.shape[0] * picture.shape[1], 3))

#Initialising the number of clusters
kmean_clust = KMeans(n_clusters = 3)

#Fitting the clusters onto the model
labels = kmean_clust.fit_predict(picture)
quantified_image = kmean_clust.cluster_centers_.astype("uint8")[labels]

#Feature Scaling
#Reshape the feature vectors to pictures
quantified_image = quantified_image.reshape((h1, w1, 3))
picture = picture.reshape((h1, w1, 3))

#Converting the image back to RGB
quantified_image = cv2.cvtColor(quantified_image, cv2.COLOR_LAB2BGR)
picture = cv2.cvtColor(picture, cv2.COLOR_LAB2BGR)

#Writing the segmented image as a new one
cv2.imwrite('generated.jpg', quantified_image)
cv2.waitKey(0)
cv2.destroyAllWindows()