# Project 2

## Project descriptioin
This is an iteration of the first project. The key difference being that this version is running in a container. The same backend applies from the first project. 

## How to run
To get this project to run, execute this command:

`docker run -p 12345:12345 blue_whale`

If you would like to make changes and rebuild the image, then try this:

`docker build -t blue_whale .`

then, 

`docker run -p 12345:12345 blue_whale`


## Example of running

There are two methods to testing if the project is running successfully.

### Method One - curl
You can always use `curl` to quickly check if the API is setup correctly. 


### Method Two - Postman
This is the method used in Project1 to make sure everything was setup correctly. The steps as the same as project one, except the port number is different this time. 
