# Charts
**This project is to facilitate operation and maintenance operations such as packaging, installation and uninstallation of chains and nodes after instantiating the crd-based cita-cloud**
### Prerequisites
- Kubernetes 1.17+
- Helm 3.6.3
- go 1.16+

### Install Helm

Helm is a tool for managing Kubernetes charts. Charts are packages of pre-configured Kubernetes resources.

To install Helm, refer to the [Helm install guide](https://github.com/helm/helm#install) and ensure that the `helm` binary is in the `PATH` of your shell.

### Using Helm

Once you have installed the Helm client, you can deploy a Helm Chart into a Kubernetes cluster.

Please refer to the [Quick Start guide](https://helm.sh/docs/intro/quickstart/) if you wish to get running in just a few commands, otherwise the [Using Helm Guide](https://helm.sh/docs/intro/using_helm/) provides detailed instructions on how to use the Helm client to manage packages on your Kubernetes cluster.

Useful Helm Client Commands:
* Install a **chain-chart**: `helm install chain chain-chart`
* List the instance of charts: `helm list`
* Uninstall a chart: `helm unintall test-chain`

### introduce charts

#### chain-chart/ - Create the chain of CITA-Cloud

```
helm install chain chain-chart
```
#### node-chart/ - Create the node of CITA-Cloud

```
helm install -f samples/(your node valus).yaml (your node name) node-chart/
```

#### samples/ - Template repository used to instantiate the chart

#### install.sh - In a single-cluster scenario, establish a chain and create new nodes in batches

#### gen_key.py - Script to generate the **network_key,  node_address, node_key** of the new node
