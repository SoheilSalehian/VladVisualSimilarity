# Vlad
This is POC for a vlad microservice.

## Motivation
We would like to efficiently build a content based image retrieval system with state of the art feature descriptors. This is a first stab at building the basic components of a visual similarity engine using VLAD descriptors.

## Workflow
A docker based workflow to avoid dependancy hell that we all hate in most computer visio projects.

### Setup
1. build the dockerfile:
`docker build -t vlad .`

2. Run the docker container + mount the development:
`docker run --rm -it -v $(pwd):/host vlad /bin/bash`

3. Once in the running container, go to host:
`cd /host`

4. To index a data set, call:
`python index.py -data {path to your data directory}`

5. To make a query with an image, call:
`python query.py -query {path to your query image}`

6. You should see a result of similar images and a list of similarity distance measures:
`[[ 1.27814922  1.28080905  1.30426036  1.32187242]] [[2 4 3 0]]
Similar Image:  data/example copy 4.jpg
Similar Image:  data/example.jpg
Similar Image:  data/example copy.jpg
Similar Image:  data/example copy 2.jpg`


## Roadmap
- [x] Basic vlad functionality
- [x] Dockerize
- [ ] Better indexing
- [ ] Wrap around API
- [ ] Optimization
- [ ] A TON OF OTHER GOODIES!


