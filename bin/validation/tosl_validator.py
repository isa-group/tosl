from rdflib import Graph, Namespace
from rdflib.namespace import RDF
from pyshacl import validate
import time
from collections import defaultdict

SH = Namespace("http://www.w3.org/ns/shacl#")
DATA_PATH = "../../examples/openai/Europe_terms_of_use_2024.ttl"

def validate_syntax(ttl_path):
    g = Graph()
    try:
        g.parse(ttl_path, format='turtle')
        print("✅ Syntax is valid Turtle.")
        return g
    except Exception as e:
        print("❌ Syntax error:", e)
        return None


def parse_validation_results(results_graph_data):
    graph = Graph()
    graph.parse(data=results_graph_data, format="turtle")

    edges = []
    nodes = set()

    for result in graph.subjects(RDF.type, SH.ValidationResult):
        subject = graph.value(result, SH.focusNode)
        predicate = graph.value(result, SH.resultPath)
        obj = graph.value(result, SH.value)

        if subject and predicate is not None:
            subj_str = str(subject)
            pred_str = str(predicate)
            obj_str = str(obj) if obj is not None else "None"
            edges.append((subj_str, pred_str, obj_str))
            nodes.update([subj_str, obj_str])

    return edges, nodes


def build_tree(edges):
    tree = defaultdict(list)
    for subj, pred, obj in edges:
        tree[subj].append((pred, obj))
    return tree


def collect_paths(node, tree, all_paths, path=None):
    if path is None:
        path = []
    extended = False
    for pred, child in tree.get(node, []):
        extended = True
        collect_paths(child, tree, all_paths, path + [node, pred])
    if not extended:
        full_path = tuple(path + [node])
        all_paths.add(full_path)


def filter_unique_paths(all_paths):
    filtered_paths = set()
    for path in all_paths:
        if not any(other != path and path == other[:len(path)] for other in all_paths):
            filtered_paths.add(path)
    return filtered_paths


def extract_messages_results(results_graph_data):
    edges, nodes = parse_validation_results(results_graph_data)
    tree = build_tree(edges)

    child_nodes = {obj for _, _, obj in edges}
    roots = [n for n in nodes if n not in child_nodes]

    all_paths = set()
    for root in roots:
        collect_paths(root, tree, all_paths)

    filtered_paths = filter_unique_paths(all_paths)

    for path in sorted(filtered_paths):
        print(" → ".join(path))

    print(f"\n Total unique violation paths: {len(filtered_paths)}")


def validate_conformance(graph, shacl_path):
    start = time.time()
    conforms, results_graph, _ = validate(
        data_graph=graph,
        shacl_graph=shacl_path,
        inference='rdfs',
        serialize_report_graph=True,
        advanced=True,
        max_recursion_depth=6
    )
    duration = time.time() - start

    if conforms:
        print("✅ Conforms to TOSL/ODRL SHACL.")
    else:
        print("❌ Conformance error:")
        extract_messages_results(results_graph)

    print(f"\n Validation time: {duration:.2f} seconds")


if __name__ == "__main__":
    g = validate_syntax(DATA_PATH)
    if g:
        validate_conformance(g, "../../validator/agreement_shape.ttl")
