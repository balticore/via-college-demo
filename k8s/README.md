## Create Kubernetes Deployment and Service

If you have followed all the steps in the README file in the root folder you should have Minikube Kubernetes cluster running on your local machine. You can then interact with your cluster either with kubectl directly or through visual interface k9s. There are many more other tools available as well, but it is recommended to get comfortable with kubectl in the beginning.

## Create Kubernetes resources

Kubernetes uses [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) to isolate groups of resources within a cluster. 

For this example first create a namespace called `hello-world` by running:

```shell
kubectl create ns hello-world
```

Next, we can use this namespace for creating Deployment and Service, but before that you need to replace <USERNAME> in the `image` section

`deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-world-deployment
  labels:
    app: hello-world 
spec:
  replicas: 2
  selector:
    matchLabels:
      app: hello-world-label
  template:
    metadata:
      labels:
        app: hello-world-label
    spec:
      containers:
      - name: hello-world-container
        image: <USERNAME>/hello-world:latest <-- Replace with the username from your Dockerhub account
        ports:
        - containerPort: 5000
```

You can leave service.yaml file without modifications but note that `labels` field matched the ones from `deployment.yaml`. Since containers are ephemeral - created and destroyed constantly their IP addresses change each time. Instead of trying to access them directly we use Service resource which has a static name and finds containers through their labels. Note that in Kubernetes [Pod](https://kubernetes.io/docs/concepts/workloads/pods/) is a smallest unit of deployment and usually has 1 to 1 relationship between to containers. This means that 1 Kubernetes pod usually hosts 1 container, but there are exceptions which are out of scope for this example.

`service.yaml`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: hello-world-service
  labels:
    app: hello-world-label
spec: 
  ports:
  - port: 5000
    targetPort: 5000
    protocol: TCP
  selector:
    app: hello-world-label
```

If you already created namespace `hello-world` from first step you can create Deloyment and Service by running commands from the current folder:

```shell
kubectl create -f deployment.yaml -n hello-world
```

```shell
kubectl create -f service.yaml -n hello-world
```

Now you can use [port-forwarding](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/) to access your application running in the containers through the service endpoint by first running:

```shell
kubectl port-forward svc/hello-world-service -n hello-world 5000:5000
```

This allows you to access created service through `localhost:5000` in your web browser. If you see `"Hostname: hello-world-deployment-****"` then you have successfully set up your Kubernetes environment and deployed application.

If you want to update the application make changes to it and go through the steps in `python` folder to publish new image or image tag and then run:

```shell
kubectl rollout restart deployment hello-world-deployment -n hello-world
```

This will destroy running containers one by one and create new ones with your updated application container image. Advantage of this approach is that Kubernetes will make sure new container image is created before old one is destroyed, ensuring high availability of your applications.

