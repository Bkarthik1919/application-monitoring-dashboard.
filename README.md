# Application Monitoring Dashboard
Prometheus scrapes a sample Flask app's metrics and Grafana visualizes them.

## Run
`docker compose up --build -d`
App: http://localhost:5003 | Prometheus: http://localhost:9090 | Grafana: http://localhost:3000
Grafana demo login: admin / change-me-now. Change this password before sharing the environment.
In Grafana add Prometheus data source `http://prometheus:9090`, then query `up` or `demo_http_requests_total`.
