#!/usr/bin/python

from pyld import jsonld
import requests
from jsonld.context import apis
import pickle 
 



def load(name, url, context, root, double):
    data = requests.get(url).json()
    doc = root(data)
    for s in doc:
        s['@context'] = context
    rdf = jsonld.to_rdf(doc, {format: 'application/n-quads', 'base':"http://www.semanticweb.org/ontologies/2021/bike"})

    if double:
        with open(f'./rdf_data/Triple_{name}.obj', 'rb') as f:
            tab = pickle.load(f)
            rdf['@default'] += tab

    with open(f'./rdf_data/Triple_{name}.obj', 'wb') as f:
        pickle.dump(rdf['@default'], f)


def load_all():
    for api in apis:
        load(api['name'], api['url'], api['context'], api['root'], api['double'])
        