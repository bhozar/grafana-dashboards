**Enable Carbon Data Exports to S3**
- Navigate to the Billing and Cost Management console.
- In the left sidebar, select Data Exports.
- Click Create and choose Carbon emissions as the data table.
- Configure the Export:
- - ***Export name:*** e.g., carbon_emissions_monthly.
- - ***S3 bucket:*** Choose an existing bucket or create a new one.
- - ***Format:*** Select Parquet. (It’s much faster and cheaper to query in Athena than CSV).
- - ***Compression:*** Snappy.
- - ***Versioning:*** Select "Overwrite existing data export file" if you want a clean "latest" state, or "Create new export version" for historical tracking.

***[!IMPORTANT]*** **The 3-Month Lag:** AWS carbon data is updated monthly but typically has a 3-month delay (e.g., in June, you'll see data for March). Your Grafana dashboard will look empty if you filter for "Last 7 days."
