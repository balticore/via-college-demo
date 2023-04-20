# via-college-demo

## Description

This repository contains useful links to set up a Kubernetes cluster on local machine as well as a hello world example of python application, Dockerfile and Kubernetes [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) and [Service](https://kubernetes.io/docs/concepts/services-networking/service/)

## Operating system

It is possible to set up the environment on Windows directly but it is also recommended to try out Windows Subsystem for Linux [WSL](https://learn.microsoft.com/en-us/windows/wsl/install). This will give access to Linux terminal which is beneficial since many examples in the Kubernetes resources will be tailored for it. Using MacOS is also beneficial if non of the previous options are available since it's terminal syntax is very similar to Linux.

## Creating Dockerhub account

Kubernetes is a [container](https://www.docker.com/resources/what-container/) orchestration system, therefore before using it you should be familiar with what it is and how it can be used. You can then use free version of [Dockerhub](https://hub.docker.com/) to push your container images which can then be used in your Kubernetes environments.

## Setting up Kubernetes

You can read about what [Kubernetes](https://kubernetes.io/) is and if you would like to set it up on your local machine you can use [Minikube](https://minikube.sigs.k8s.io/docs/start/). This will spin up a Kubernetes cluster giving you most of needed functionalities to test it's features.

## Installing Kubernetes command line interface - kubectl

To interact easily with your Kubernetes cluster it is recommended to use it's command line interface - kubectl. You can find instructions on how to install it on different operating systems in [Kubernetes tools](https://kubernetes.io/docs/tasks/tools/) page under kubectl section.

## Installing Kubernetes visual command line interface - k9s

If you would like to see your Kubernetes cluster and it's resources in a visual represenation it is recommended to use [k9s](https://k9scli.io/). 

