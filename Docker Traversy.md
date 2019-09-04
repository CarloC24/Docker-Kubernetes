### Docker with NodeJS and MongoDB

Docker only has one server and one OS not like VM's

`docker version` - docker version
`docker info` - will give info about the docker server

### Docker Nginx

`docker container run -it -p 5000:80` to run it in localhost:5000

### Docker MySQL (Environment Variables)

`docker run -it -p 3306:3306 --name mysql_test --env MYSQL_ROOT_PASSWORD=123456 mysql`
you can use `--env` or `-e`

### Other Docker Tips

`docker rm <containerID> -f` `-f` is for force

### How to Bash inside your Nginx container??

Step 1:`docker run -d --name mynginx -p 5000:80 nginx`

Step 2:`docker exec -it mynginx bash`

### How to volume map?

`docker run -d -p 8080:80 --name nginx -v $(pwd):/usr/share/nginx/html`

### Shorthand to remove all containers

`docker rm $(docker ps -aq)` - remove all containers.. dodnt forget to add the -f flag if some of the containers are not stopped.

### Creating dockerfile

#### Check the dockerfile that we made in the test dir for comments!!

```
FROM nginx:latest

WORKDIR /usr/share/nginx/html

COPY . .
```

then run the command `docker image build -t <username>/<container-name> .`

EXAMPLE
`docker image build -t carloc24/nginx-website .`

the `.` stands for the dockerfile in the container we are in..

then check `docker image` you can see the nginx website that you pushed.

then we can get the container from our local machine simply just saying

`docker run -d -p 8080:80 carloc24/nginx-website` then we should see our hello world in localhost:8080!!

to push it to your docker account simply say `docker push carloc24/nginx-website`.
