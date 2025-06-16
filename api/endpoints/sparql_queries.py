from fastapi import APIRouter, UploadFile, File, Query
from rdflib import Graph
import os

router = APIRouter()

VALID_TERM_TYPES = [
    "arbitration",
    "change",
    "choice_of_law",
    "content_removal",
    "contract_by_use",
    "jurisdiction",
    "limitation_of_liability",
    "termination"
]

DEONTIC_STATUS_QUERIES = [
    "get_customer_duties",
    "get_customer_permissions",
    "get_customer_prohibitions",
    "get_duties",
    "get_permissions",
    "get_prohibitions",
    "get_provider_duties",
    "get_provider_permissions",
    "get_provider_prohibitions",
    "total_duties",
    "total_permissions",
    "total_prohibitions",
    "total_rules"
]


def run_query(ttl_content: str, query: str, rdf_format="ttl"):
    g = Graph()
    g.parse(data=ttl_content, format="turtle")
    qres = g.query(query)
    
    results = []
    for row in qres:
        result_row = {}
        for var, value in row.asdict().items():
            result_row[var] = str(value) if value else None
        results.append(result_row)
    
    return results

@router.post("/unfair_terms")
async def unfair_terms(
    term_type: str = Query(..., enum=VALID_TERM_TYPES),
    file: UploadFile = File(...)):

    query_file_path = f"sparql_queries/unfair_terms/{term_type}.rq"
    
    if not os.path.exists(query_file_path):
        return {"error": f"Query file not found for term_type '{term_type}'"}

    with open(query_file_path, "r", encoding="utf-8") as f:
        sparql_query = f.read()
    
    content = await file.read()
    
    return run_query(content.decode("utf-8"), sparql_query)


@router.post("/deontic_status")
async def deontic_status(
    deontic_status: str = Query(..., enum=DEONTIC_STATUS_QUERIES),
    file: UploadFile = File(...),
):
    query_file_path = f"sparql_queries/obligations_permissions_prohibition/{deontic_status}.rq"

    if not os.path.exists(query_file_path):
        return {"error": f"Query file not found for deontic_status '{deontic_status}'"}

    with open(query_file_path, "r", encoding="utf-8") as f:
        sparql_query = f.read()

    content = await file.read()

    return run_query(content.decode("utf-8"), sparql_query)
