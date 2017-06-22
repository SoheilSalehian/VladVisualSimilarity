import cv2
import sys
import numpy as np
import glob

def extractVladDescriptor(image):
  pass

def extractSIFT(imagePath):
  descriptors = list()

  for path in glob.glob(imagePath+"/*.jpg"):
    print "Extracting from"+path
    # SIFT Feature Extraction
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    (kps, siftDescriptors) = sift.detectAndCompute(gray, None)

    descriptors.append(siftDescriptors)

  return descriptors

# TODO: Additional features for future use
def extractSURF(image):
  pass

def extractORB(image):
  pass

print extractSIFT(sys.argv[1])

