# Nginx Deployment

This repository contains a Kubernetes deployment configuration for deploying Nginx web server.

## Deployment Configuration

The deployment configuration is defined in the `nginx-deployment.yaml` file.

### Deployment Object

- **apiVersion**: Specifies the version of the Kubernetes API that this object should use.
- **kind**: Specifies the type of Kubernetes object, in this case, a Deployment.
- **metadata**: Contains metadata about the deployment, including its name.

### Spec

- **replicas**: Indicates the number of desired replicas (instances) of the application to run.
- **selector**: Defines how the Deployment selects which Pods to manage.
- **strategy**: Defines the deployment strategy, including parameters for rolling updates.
- **template**: Specifies the Pod template that the Deployment will use to create new Pods.

### Pod Template

- **metadata**: Contains metadata about the Pod template, including its labels.
- **labels**: Specifies the labels for the Pods created by this template.
- **spec**: Specifies the desired state of the Pods.

#### Containers

- **name**: Specifies the name of the container.
- **image**: Specifies the Docker image to use for the container.
- **ports**: Specifies the ports that the container exposes.
- **resources**: Specifies the CPU and memory resource requests and limits for the container.

### Affinity

Specifies affinity and anti-affinity rules for the Pod.

## How to Use

1. Ensure you have a Kubernetes cluster set up.
2. Apply the deployment configuration using `kubectl apply -f nginx-deployment.yaml`.
3. Monitor the deployment using `kubectl get deployment nginx-deployment`.

## Notes

- This configuration deploys three replicas of the Nginx web server.
- Resource requests and limits are specified to ensure proper resource allocation.
- Anti-affinity rules are defined to prevent Pods from being co-located on the same node.

