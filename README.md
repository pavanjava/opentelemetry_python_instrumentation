# opentelemetry_python_instrumentation
this repository will explain how to instrument and work with open telemetry in python environments

there are 2 files in the project which says 
- `basic_instrumentation.py` which will demonstrate the trace capability in console
- `advanced_instrumentation.py` which will export the trace to jaeger


- NOTE: before you install the project dependencies please have jager installed in docker and check its up and running


# All in one Jaeger Docker image
docker run -d --name jaeger \
-e COLLECTOR_ZIPKIN_HTTP_PORT=9411 \
-p 5775:5775/udp \
-p 6831:6831/udp \
-p 6832:6832/udp \
-p 5778:5778 \
-p 16686:16686 \
-p 14268:14268 \
-p 9411:9411 \
jaegertracing/all-in-one:1.6

- You can then navigate to http://localhost:16686 to access the Jaeger UI.
