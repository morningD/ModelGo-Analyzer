from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, XSD

# Define namespaces
EX = Namespace("http://example.org/")

# Create a new RDF graph
g = Graph()

# Parse the N3 data
g.parse("example.ttl", format='n3')

# Serialize and print the graph in N3 format
print("Serialized N3 Data:")
print(g.serialize(format='n3').decode('utf-8'))

# Query the graph to check inferred triples
query = """
SELECT ?s ?p ?o
WHERE {
    ?s ?p ?o .
}
"""

print("\nQuery Results:")
for row in g.query(query):
    print(f"{row.s} {row.p} {row.o}")
