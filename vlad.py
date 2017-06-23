import cv2
import sys
import numpy as np
import glob
import itertools
from sklearn.cluster import KMeans
from sklearn.neighbors import BallTree
import pickle

def index():
  vladDescriptors = list()
  imageIDs = list()

  for imagePath in glob.glob(sys.argv[1]+"/*.jpg"):
    vlad = extract(imagePath)

    vladDescriptors.append(vlad)
    imageIDs.append(imagePath)

    # Save the vlad descriptors
    with open("kvd.pickle", "wb") as f:
      pickle.dump([imageIDs, vladDescriptors], f)

    # Ball tree algorithm in order to organize the vlad descriptors for query purposes
    # TODO: play with different leaf_size 
    tree = BallTree(vladDescriptors, leaf_size=10)
    # Save the index
    with open("index.pickle", "wb") as f:
      pickle.dump([imageIDs, tree], f)


def query(imagePath):
  print "Querying image: ", imagePath
  #load the index
  with open("index.pickle", 'rb') as f:
    index = pickle.load(f)

  #load the visual dictionary
  with open("kvd.pickle", 'rb') as f:
    visualDictionary = pickle.load(f) 

  imageIDs = index[0]
  tree = index[1]

  vlad = extract(imagePath) 

  # Find the distance and corresponding neaighbouring indices already in the index
  distance, indices = tree.query(vlad, 4)
  print distance, indices
  indices = list(itertools.chain.from_iterable(indices))

  # Report the similar images to the query image in the index
  for i in indices:
    print "Similar Image: ", imageIDs[i]


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

index()
query("data/example.jpg")
