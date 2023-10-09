from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter

trace_provider = TracerProvider()
batch_processor = BatchSpanProcessor(ConsoleSpanExporter())
trace_provider.add_span_processor(batch_processor)
trace.set_tracer_provider(tracer_provider=trace_provider)
tracer = trace.get_tracer(instrumenting_module_name="main_module")

app = FastAPI()


@app.get("/basic/health")
def health():
    with tracer.start_as_current_span("server_request"):
        return {"health": "OK"}