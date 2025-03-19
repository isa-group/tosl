from rdflib_neo4j import Neo4jStoreConfig
from rdflib_neo4j import HANDLE_VOCAB_URI_STRATEGY
from rdflib import Namespace
from rdflib_neo4j import Neo4jStore
from rdflib import Graph

file_path = "../examples/API_Service_Agreement.ttl"

AURA_DB_URI="neo4j+s://your-id.databases.neo4j.io"
AURA_DB_USERNAME="neo4j"
AURA_DB_PWD="your-password"

auth_data = {'uri': AURA_DB_URI,
             'database': "neo4j",
             'user': AURA_DB_USERNAME,
             'pwd': AURA_DB_PWD}
             
# Define your prefixes
prefixes = {
    '': Namespace('http://example.com/'),
    'owl': Namespace('http://www.w3.org/2002/07/owl#'),
    'rdf': Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#'),
    'xml': Namespace('http://www.w3.org/XML/1998/namespace'),
    'xsd': Namespace('http://www.w3.org/2001/XMLSchema#'),
    'rdfs': Namespace('http://www.w3.org/2000/01/rdf-schema#'),
    'skos': Namespace('http://www.w3.org/2004/02/skos/core#'),
    'dcterms': Namespace('http://purl.org/dc/terms/'),
    'foaf': Namespace('http://xmlns.com/foaf/0.1/'),
    'odrl': Namespace('http://www.w3.org/ns/odrl/2/'),
    'tosl': Namespace('https://w3id.org/tosl/'),
    'dx-prof': Namespace('http://www.w3.org/ns/dx/prof/'),
    'vann': Namespace('http://purl.org/vocab/vann/')
}

# Define your custom mappings
config = Neo4jStoreConfig(
    auth_data=auth_data,
    custom_prefixes=prefixes,
    handle_vocab_uri_strategy=HANDLE_VOCAB_URI_STRATEGY.SHORTEN, 
    batching=True
)

graph_store = Graph(store=Neo4jStore(config=config))
graph_store.parse(file_path,format="ttl")
graph_store.close(True)