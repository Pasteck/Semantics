from queries.queries import SparqlQueries

def queries_builder(ontologies):
  querier = {}
  for onto in ontologies:
    querier[onto[11:-4]] = SparqlQueries(onto, reasoner=False)
  return querier