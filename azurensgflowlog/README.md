# Azure NSG Flow Log Dashboard
Dashboard to visualize Azure NSG Flow Logs data from [Logstash Event Hubs plugin](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-azure_event_hubs.html)

Deploy Microsofts [Azure Network Watcher NSG Flow Logs Connector](https://github.com/microsoft/AzureNetworkWatcherNSGFlowLogsConnector) Function App to gather the data.

Setup Azure NSG FLow Logs to stream data in an Azure EventHub so the ES plugin can pickup the data.

The Logstash filter files have been provided.

![Azure NSG Flow Log Dashboard](./grafana-azure-nsgflow-log01.png)
