import pickle
import itertools
import argparse
from core import extract


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

ap = argparse.ArgumentParser()
ap.add_argument("-query", required=True, help="Path to the query image")
args = vars(ap.parse_args())
imagePath = args["query"]
query(imagePath)

