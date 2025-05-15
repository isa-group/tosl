import os
import pytest
from rdflib import Graph
from pyshacl import validate

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SHACL_PATH = os.path.join(BASE_DIR, "..", "agreement_shape.ttl")

def run_validation(data_path):
    g = Graph()
    g.parse(data_path, format='turtle')
    conforms, _, _ = validate(
        data_graph=g,
        shacl_graph=SHACL_PATH,
        inference='rdfs',
        serialize_report_graph=True
    )
    return conforms

@pytest.mark.parametrize("ttl_file", os.listdir("validator/tests/valid"))
def test_valid_cases(ttl_file):
    path = os.path.join("validator/tests/valid", ttl_file)
    assert run_validation(path) == True, f"{ttl_file} should conform but doesn't."

@pytest.mark.parametrize("ttl_file", os.listdir("validator/tests/invalid"))
def test_invalid_cases(ttl_file):
    path = os.path.join("validator/tests/invalid", ttl_file)
    assert run_validation(path) == False, f"{ttl_file} should not conform but does."


