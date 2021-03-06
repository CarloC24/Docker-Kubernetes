Why do you need docker?

- There are times when some services are not compatible with certain OS.
- Docker solves Compatability/Dependency Long Setup Times and Different Dev/Test/Prod environments

Container vs Images

Docker Image - has package template plans

Docker Container - runs images and isolates it.

Docker in DevOps - Developers make images and transfers it to hosts and if they have docker available it will be available to run.

### How to get started with docker

Docker Editions

1.  Community Edition - With free images
2.  Enterprise Edition - Comes with image security and a bunch of other features

Come back from 16:50

## Installing Docker for mac

download docker for mac

to run a simple docker file open your terminal and say

`docker run docker/whalesay cowsay Hello-Carlo!`

## Docker Commands

`docker run` - Starts/Runs a container
`docker ps` - lists all running containers
`docker ps -a` - shows all containers whether running or previously stopped.
`docker stop <name or container-ID>` - stops the docker container
`docker rm <name or container-ID>` - removes the docker container for good.
`docker images` - list all the images you pulled from the docker hub.
`docker rmi <nameofimage>` - removes a image that you pulled from docker hub.
`docker pull <imagename>` - just download and store the image on host.
`docker exec <container-name> <command>` - runs the command on the given container name.

### Appending commands

`docker run ubuntu` - runs ubuntu for as long as the process inside it is finished.
`docker run ubuntu sleep 5` - runs ubuntu to sleep for 5 seconds.
`docker exec distracter_mcclintock cat /etc/hosts` - runs the command on the given container name

## Exercise

`docker run kodekloud/simple-webapp` - runs a flash web app.

`docker run -d kodekloud/simple-webapp` - `-d` runs the app on the background. and will not display the content on the terminal

## Docker lab

https://katacoda.com/kodekloud/scenarios/docker-for-beginners-fcc-basiccommands

## Docker run

`docker run redis` - runs the latest `docker run redis:latest`docker run redis:<tag-version>` - runs the version of redis specified

- You can find tags on dockerhub.com on the image page.

`docker run -i kodekloud/simple-prompt-docker` - `-i` is the interactive mode.

`docker run -it kodekloud/simple-prompt-docker` - `-it` is the interactive terminal mode in docker.

### DOCKER PORT MAPPING

`docker run -p 80:5000 kodekloud/simple-webapp` - docker runs everything on port 80 to port 5000.

### DOCKER MYSQL

`docker run mysql` - runs a mysql container

my sql data gets stored at /var/lib/mysql

when you stop the container everything gets dropped.

if you want to persist data
`docker run -v /opt/datadir:/var/lib/mysql mysql`

### DOCKER INSPECT

`docker inspect <container-name>` - will return details in a json format

### DOCKER CONTAINER LOGS

`docker logs <container-id or container - name>` - will give the logs for everything in the container.

### OS ENVIRONMENTAL VARIABLES

color = os.environ.get("APP_COLOR")
`export APP_COLOR=Blue; python app.py`

to run containers and specify their env variables
`docker run -e APP_COLOR=blue simple-webapp-color`

### INSPECTING VARIABLES

`docker inspect blissful_hopper` - you can see your environmental variables if it is not specified.

### DOCKER IMAGES

#### How to Create your Own Image

SEE DockerFile to see how a docker file is supposed to look like.

then run `docker build Dockerfile -t <creator/imagename>` on your terminal `-t` is the tag of the image

If you want to push it to the docker hub simply run the command `docker push <creator/imagename>`

### DOCKERFILE

Dockerfile includes INSTRUCTION and arguments

1. Start with a base OS `FROM Ubuntu`
2. `RUN` installs all dependencies.
3. `COPY` will copy all the source code.
4. `ENTRYPOINT` will specify what will be run after all is complete

### Docker CMD vs Entrypoint

Unlike VM's... Containers are not supposed to hold OS. They are simply to just run and do a set of instructions and exits when it is done.

#### APPENDING COMMANDS

`docker run ubuntu sleep 5`

===

```
FROM Ubuntu
CMD sleep 5
```
CMD command param1 CMD Sleep 5
CMD ["command","param1"] CMD ["sleep","5"]
` docker build -t ubuntu-sleeper .`
` docker run ubuntu-sleeper `

#### Entrypoint Instruction
```
FROM ubuntu

ENTRYPOINT ["sleep"]
```
you can now append 10 to be sleep 10

### Docker networking
Docker has three networks `Bridge` &`none` & `host`.

`Bridge` - `docker run Ubuntu`
`none` - `docker run Ubuntu --network=none`
`host` - `docker run ubuntu --network=host`

`Bridges` default on 172.17.0.1 if you want to create another bridge you can run `docker network create \
        --driver bridge \
        --subnet 182.18.0.0/16
        <custom-isolate-networkname>`
