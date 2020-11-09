# KMeans-Clustering-for-Image-Segmentation
Image segmentation using one of the most used clustering techniques KMeans

# About K-Means clustering:

K-Means is  one of  the simplest unsupervised  learning  algorithms  that  solve  the well  known clustering problem. The procedure follows a simple and  easy  way  to classify a given data set  through a certain number of  clusters (assume k clusters) fixed apriori. 
The  main  idea  is to define k centers, one for each cluster. These centers  should  be placed in a cunning  way  because of  different  location  causes different  result. So, the better  choice  is  to place them  as  much as possible  far away from each other. 
The  next  step is to take each point belonging  to a  given data set and associate it to the nearest center. When no point  is  pending,  the first step is completed and an early group age  is done. 
At this point we need to re-calculate k new centroids as barycenter of  theclusters resulting from the previous step. After we have these k new centroids, a new binding has to be done  between  the same data set points  and  the nearest new center. A loop has been generated. 
As a result of  this loop we  may  notice that the k centers change their location step by step until no more changes  are done or  in  other words centers do not move any more.

# Algorithmic steps for k-means clustering

Let  X = {x1,x2,x3,……..,xn} be the set of data points and V = {v1,v2,…….,vc} be the set of centers.

1) Randomly select ‘c’ cluster centers.

2) Calculate the distance between each data point and cluster centers.

3) Assign the data point to the cluster center whose distance from the cluster center is minimum of all the cluster centers.

4) Recalculate the new cluster center using the new centers.

5) Recalculate the distance between each data point and new obtained cluster centers.

6) If no data point was reassigned then stop, otherwise repeat from step.

# Brief:

This code takes in an image, reshapes it, uses KMeans clustering to cluster the datepoints for segmentation, and then reshapes back to an output image.
Make sure to have the input image in the same folder as the code.

# Usage:

In your terminal: python image_seg_kmean.py or simply build the code from your editor of choice

