import cv2
import sys
import numpy as np
import glob
import itertools
from sklearn.cluster import KMeans
import pickle

def extractVladDescriptor():
  desc = extractSIFT(sys.argv[1])

  # FIXME: the cluster is either 64 or 256 for decent results
  est = kMeans(desc, 8)

  pickle_indexer(est)


def extractSIFT(imagePath):
  descriptors = list()

  # FIXME: handle all kinds of image types
  for path in glob.glob(imagePath+"/*.jpg"):
    print "Extracting from"+path
    # SIFT Feature Extraction
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    (kps, siftDescriptors) = sift.detectAndCompute(gray, None)

    descriptors.append(siftDescriptors)

  descriptors = list(itertools.chain.from_iterable(descriptors))
  descriptors = np.asarray(descriptors)

  return descriptors


# TODO: Additional features for future use
def extractSURF(image):
  pass

def extractORB(image):
  pass

def kMeans(trainingDescriptors, k):
  est = KMeans(n_clusters=k,init='k-means++',tol=0.01,verbose=0).fit(trainingDescriptors)
  return est

def pickle_indexer(est):
  with open("index.pickle", 'wb') as f:
	  pickle.dump(est, f)

extractVladDescriptor()
