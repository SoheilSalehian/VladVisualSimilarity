# Vlad
This is POC for a vlad microservice.

## Motivation
We would like to efficiently build a content based image retrieval system with state of the art featre descriptors. This is a first stab at building the basic components of a visual similarity using VLAD descriptors.

## Workflow
A docker based workflow to avoid dependancy hell that we all hate in most computer visio projects.

### Setup
1. build the dockerfile:
`docker build -t vlad .`

2. Run the docker container + mount the development:
`docker run --rm -it -v $(pwd):/host vlad /bin/bash`

3. Once in the running container, go to host:
`cd /host`

4. And run the vlad algorithm by pointing to the data folder:
`python vlad.py data/`

5. Once done, you should have a pickle file of the index in the root('index.pickle')


## Roadmap
- [x] Basic vlad functionality
- [x] Dockerize
- [ ] Better indexing
- [ ] Wrap around API
- [ ] Optimization
- [ ] A TON OF OTHER GOODIES!


