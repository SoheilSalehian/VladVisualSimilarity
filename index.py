import glob
import pickle
from sklearn.neighbors import BallTree
import argparse
from core import extract


def index(dataPath):
  vladDescriptors = list()
  imageIDs = list()

  for imagePath in glob.glob(dataPath+"/*.jpg"):
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

ap = argparse.ArgumentParser()
ap.add_argument("-data", required=True, help="Path to the data set to be indexed")
args = vars(ap.parse_args())
dataPath = args["data"]
index(dataPath)
