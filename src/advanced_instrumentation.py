from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter

trace_provider = TracerProvider()
batch_span_processor = BatchSpanProcessor(ConsoleSpanExporter())
trace_provider.add_span_processor(batch_span_processor)
trace.set_tracer_provider(
    TracerProvider(
        resource=Resource.create({SERVICE_NAME: "health-service"})
    )
)
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(jaeger_exporter)
)

tracer = trace.get_tracer("advanced_instrumentation_module")

app = FastAPI()


@app.get("/advanced/health")
def health():
    with tracer.start_as_current_span("server_request"):
        return {"health": "OK"}