import cv2
import sys
import numpy as np
import glob
import itertools
from sklearn.cluster import KMeans
from sklearn.neighbors import BallTree
import pickle



def extract(imagePath):
  print "Extracting VLAD from: ", imagePath
  # SIFT Feature Extraction
  image = cv2.imread(imagePath)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  sift = cv2.xfeatures2d.SIFT_create()
  (kps, siftDescriptors) = sift.detectAndCompute(gray, None)

  # As per the "All about VLAD" paper, 64 clusters seemed to be a good parameter to start
  est = kMeans(siftDescriptors, 64)

  # get the basics for residulas to generate the vlad features
  predictedLables = est.predict(siftDescriptors)
  centers = est.cluster_centers_
  lables = est.labels_
  k = est.n_clusters

  # The vlad feature vector shape is number of clusteres X sift feature second dimension
  vlad = np.zeros([k, siftDescriptors.shape[1]])
  # Iterate through each cluster
  for i in range(k):
     # if ther is a match in the cluster
    if np.sum(predictedLables==i) > 0:
      # add the residual (the difference from match to the center of the cluster)
      residual = siftDescriptors[predictedLables==i,:]-centers[i]
      vlad[i] = np.sum(residual, axis=0)

  # Before normalization check to assert proper shape
  if not (vlad.shape == (k, 128)):
    raise AssertionError()

  # Do a L2 normalization on the feature vector
  vlad = vlad.flatten()
  vlad = vlad/np.sqrt(np.dot(vlad,vlad))

  return vlad

def kMeans(trainingDescriptors, k):
  est = KMeans(n_clusters=k,init='k-means++',tol=0.0001,verbose=0).fit(trainingDescriptors)
  return est
