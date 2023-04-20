## Containerized hello-world python application

This folder contains a basic example of python application which runs a [Flask](https://flask.palletsprojects.com/en/2.2.x/) HTTP server and returns hostname on a localhost address.

### Build and publish container image

If you have already created a Dockerhub account you can login with your credentials from your terminal:

```shell
docker login
```

Make sure you are in the current folder where this README file is located and build your Docker container image by running:

```shell
docker build . -t hello-world
```

Tag your image by replacing <USERNAME> with username your Dockerhub account:

```shell
docker tag hello-world:latest <USERNAME>/hello-world:latest
```

Push your image to Dockerhub:

```shell
docker push <USERNAME>/hello-world:latest
```

If all steps were successful you should be able to see your image in Dockerhub page when logged in with personal account. You can then also use this image in your Kubernetes deployment which can be found in k8s folder.