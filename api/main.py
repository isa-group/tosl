from fastapi import FastAPI
from api.endpoints import validator, sparql_queries

app = FastAPI(
    title="TOSL API",
    description="API para validar TOSL y realizar consultas SPARQL",
    version="1.0.0",
)

app.include_router(validator.router, prefix="/validator", tags=["Validator"])
app.include_router(sparql_queries.router, prefix="/sparql", tags=["SPARQL Queries"])
