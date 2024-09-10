from collections import defaultdict
import logging
from copy import deepcopy
from rdflib import Graph, Namespace, Literal, BNode
from rdflib.namespace import RDF, RDFS
from typing import Iterable

""" <actions.py>
This file contains the functions that can use to create a Turtule file that describe the ML workflow based on users' input,
i.e., combine(m1, m2 ,finetune(model, data)) -> workflow.ttl (RDF graph representation of this workflow),
after then we can visuablize this RDF graph and analysis the conflict by reasoner EYE.
"""

# Set the Namespaces
MG = Namespace("http://www.modelgo.li/rdf/terms#")
EX = Namespace("http://example.org/ns#")

# Set the prefix binding list
prefixs = [
    ("mg", MG),     # mg:xxx
    ("", EX)        # :xxx
]

# The function that create a empty RDF Graph with predefined namespace
def create_base_graph(prefixs=prefixs):
    g = Graph()
    for (prefix, ns) in prefixs:
        g.bind(prefix, ns)
    return g

class Work(object):
    def __init__(self, name: str, type: str, form: str):
        self.name = name
        self.type = type # software/data/model or mixed-type (mix of works with different type)
        self.form = form # code/linguistics/vision/exe/saas or raw-form/binary-form/service-form
        #self.license_name = license_name # MIT, Apache-2.0, Unlicense
        
class Workflow(object):
    def __init__(self, prefixs=None):
        if prefixs: self.graph = create_base_graph(prefixs)
        else: self.graph = create_base_graph()
        self.latest_action_id = ""

    # Merge multiple RDF graphs w/o changing the latest action id
    def merge(self, flows): 
        if isinstance(flows, Workflow):
            self.graph += flows.graph
        if isinstance(flows, Iterable):
            for f in flows:
                self.graph += f.graph
        return

    def update_action_id(self, action_id :str):
        if action_id:
            self.latest_action_id = action_id
            return True
        return False
    

# We maintain a function that generate a incremental number for each action
def gen_action_num():
    current: int = 0
    def next_num() -> int:
        nonlocal current
        current += 1
        return current
    return next_num
anum = gen_action_num()

def register_license(target_work: Work, target_license: str='Unlicense', action_label: str='reg') -> Workflow:
    flow = Workflow() # Create a new workflow contains this register action
    g = flow.graph
    wiri = EX[target_work.name]
    
    # Add the Work subject in a new RDF graph
    g.add((wiri, RDF.type, MG.work))
    g.add((wiri, MG.workName, Literal(target_work.name)))
    g.add((wiri, MG.hasWorkType, Literal(target_work.type)))
    g.add((wiri, MG.hasWorkForm, Literal(target_work.form)))
    
    # Add the Register action in this graph
    action_id = action_label + str(anum())
    airi = EX[action_id]
    g.add((airi, RDF.type, MG.RegisterLicense))
    g.add((airi, MG.actionId, Literal(action_id)))
    bn = BNode() # Blank node of mg:hasInput
    g.add((airi, MG.hasInput, bn))
    g.add((bn, MG.targetWork, wiri))
    g.add((bn, MG.targetLicense, MG[target_license]))

    # Maintain the latest action ID
    flow.update_action_id(action_id)

    return flow

def combine(target_flows: Iterable[Workflow], action_label='combine') -> Workflow:
    flow = Workflow() # Create a new empty workflow
    flow.merge(target_flows) # Add the graphs from targetflows to new workflow
    g = flow.graph

    # Add the Combine Action in the new graph
    action_id = action_label + str(anum())
    airi = EX[action_id]
    g.add((airi, RDF.type, MG.Combine))
    g.add((airi, MG.actionId, Literal(action_id)))
    bn = BNode()
    g.add((airi, MG.hasInput, bn)) # Add a blank node as input, which will be populated later by N3 rules
    # Create the yieldOutputWork links from latest actions in target_flows to this Combine action
    for f in target_flows: 
        g.add((EX[f.latest_action_id], MG.yieldOutputWork, airi))
    flow.update_action_id(airi)

    return flow

# def train() -> Workflow:

#     return flow