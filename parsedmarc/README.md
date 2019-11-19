# DMARC Reports Dashboard
Dashboard to visualize data from [ParseDMARC](https://github.com/domainaware/parsedmarc)

Available from Grafana.com: [DMARC Reports](https://grafana.com/grafana/dashboards/11227)

![DMARC Report Overview](./grafana-dmarc-reports01.png)

![DMARC Report Status Over Time](./grafana-dmarc-reports02.png)

![DMARC Report Details](./grafana-dmarc-reports03.png)

Two data sources to be updates, one for Aggregate reports and one for Forensic reports.
![Aggregate data source setup](./grafana-dmarc-reports04.png)

![Forensic data source setup](./grafana-dmarc-reports05.png)

Requires Worldmap and Piechart plugins for all panels to display.

Aggregate data is per-day, so dashboard is only helpful when looking back 24hr+.

