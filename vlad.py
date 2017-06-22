import cv2
import sys
import numpy as np

def extractVladDescriptor(image):
  pass

def extractSURF(imagePath):
  # SURF Feature Extraction
  image = cv2.imread(imagePath)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  sift = cv2.xfeatures2d.SIFT_create()
  (kps, descriptors) = sift.detectAndCompute(gray, None)
  return kps, descriptors

# TODO: Additional features for future
def extractSIFT(image):
  pass

def extractORB(image):
  pass

print extractSURF(sys.argv[1])

