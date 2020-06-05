# Coding-test
# @author stinsley

# 'implement a function that combines two arrays into one sorted array'

# To build: 
# 1) build the docker file
docker build . -t tinsley-coding-test

# 2) Tag the image 
docker tag coding-test tinsley-codingtest:latest

# 3) Push the image (if using a repository) 
docker push tinsley-coding-test:latest

# 4) Run the container and pass in args
docker run tinsley-coding-test:latest [4,5,2,7] [8,0,1,6]

#Resulting array
[0, 1, 2, 4, 5, 6, 7, 8]

