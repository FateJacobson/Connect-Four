# Connect-Four

## Authors 

Fate Jacobson - Sole Developer

## Thanks

Special thanks to Erin Keith for a great semester

## News

Upcoming presentation on Tuesday, April 26th, around 3:00pm

## Build Instructions

### Install Docker

First, install Docker Desktop. 

Installation link: https://www.docker.com/products/docker-desktop/

### Build Docker Container 

Once installed, run the following commands in the command line to create and run a container.

$ docker build -t connect_four .

$ docker run -t -i connect_four

### Open CLI in Docker Container

Navigate to the newly created container in Docker Desktop and click the cli button to open a terminal.

### Run Connect_Four Program

To play connect four, simply enter the following command.

$ Python connect_four.py

### Run Tests and View Coverage

To run the automated tests, enter the following command.

$ coverage run test.py -b

After running the automated test, test coverage can be evaluated by entering the following command.

$ coverage report -m
