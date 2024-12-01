#!/usr/bin/env python
import argparse

# do not show pandas import warnings
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
from tabulate import tabulate
from rdflib import Graph


def tabulate_result(results):
    rows = [row.asdict() for row in results]
    df = pd.DataFrame(rows)
    print(tabulate(df, headers=df.columns))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a SPARQL query on a Turtle file.")
    parser.add_argument("file", help="The file with the ontology to query.")
    parser.add_argument("query", help="The SPARQL query to run.")
    parser.add_argument("--format", help="The format of the file.", default="ttl", choices=["ttl", "xml", "n3", "nt", "rdf", "trig", "json-ld"])
    args = parser.parse_args()
    
    g = Graph()
    result = g.parse(args.file, format=args.format)
    results = g.query(args.query)
    tabulate_result(results)
