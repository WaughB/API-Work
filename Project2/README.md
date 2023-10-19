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

Here is what a successful build and run may look like:
[](images/Successful-build-and-run.png)

## Example of running

This is the same method used in Project1 to make sure everything was setup correctly. The steps as the same as Project1, except the port number is different this time. 

After this you will be able to access the API. For this example I used [Postman](https://www.postman.com/) and sent this information: 

[
    {"Age": 85, "Sex": "male", "Embarked": "S"},
    {"Age": 24, "Sex": "female", "Embarked": "C"}
]

This is what it returned to me: [](/images/Postman-working.png)
