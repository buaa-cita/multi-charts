if [ $1x != "uninstallx" ]
then
	helm install -f samples/chain_values.yaml chain chain-chart/
	helm install -f samples/node_values_0.yaml node0 node-chart/
	helm install -f samples/node_values_1.yaml node1 node-chart/
else
	helm uninstall node1
	helm uninstall node0
	helm uninstall chain
fi

