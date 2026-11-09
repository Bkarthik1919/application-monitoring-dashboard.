from flask import Flask,Response
from prometheus_client import Counter,generate_latest,CONTENT_TYPE_LATEST
app=Flask(__name__); REQS=Counter("demo_http_requests_total","HTTP requests",["path"])
@app.get("/")
def home(): REQS.labels("/").inc(); return "<h1>Monitoring demo</h1><a href='/metrics'>Metrics</a>"
@app.get("/health")
def health(): REQS.labels("/health").inc(); return {"status":"healthy"}
@app.get("/metrics")
def metrics(): return Response(generate_latest(),mimetype=CONTENT_TYPE_LATEST)
