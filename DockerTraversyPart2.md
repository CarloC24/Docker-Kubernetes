### Docker Compose with NodeJS and MongoDB

CHECK THE DOCKERFILE IN THE MONGOAPP

```
#Pick the version of node!
FROM node:10
#Specify the workdir in our docker image
WORKDIR /usr/src/app
# Copy the package.json and packagelock.json into the workdir
COPY package*.json ./
# Run npm install
RUN npm install
#Copy all the files into the working directory
COPY . .
#We need to expose the port 3000 because it is the port it runs on
EXPOSE 3000
# Command to start the app.
CMD ["npm","start"]
```

### DOCKER COMPOSE

docker-compose.yml

```
version: '2'

# same as
# docker run -p 80:4000 -v $(pwd):/site bretfisher/jekyll-serve

services:
  jekyll:
    image: bretfisher/jekyll-serve
    volumes:
      - .:/site
    ports:
      - '80:4000'
```

you can also add `.dockerignore` and it works just like a .gitignore
