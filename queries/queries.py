from owlready2 import *
from rdflib import *

class SparqlQueries:
  def __init__(self, onto_path, reasoner=False):
      my_world = World()
      my_world.get_ontology(onto_path).load() 
      if reasoner:
        sync_reasoner_pellet(my_world)
      self.graph = my_world.as_rdflib_graph()
    
  def extract_res(self, qres, params, disp):
    res = []
    for row in qres:
      l = {}
      for par in params:
        l[par] = row[par].toPython()
      res.append(l)
      if disp:
        print(l)
    return res
  
  # Some queries

  def getStandFreeStation(self, disp=True):
    query = """PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
               PREFIX  ns:<http://www.semanticweb.org/ontologies/2021/bike#>
               SELECT ?s ?abs ?ab ?lu ?name ?lat ?long  WHERE { 
                  ?s rdf:type ns:StandFreeStation . 
                  ?s ns:Name ?name .
                  ?s ns:Lat ?lat .
                  ?s ns:Long ?long .
                  ?s ns:Name ?name .
                  ?s ns:AvailableBikeStands ?abs .
                  ?s ns:AvailableBikes ?ab .
                  ?s ns:Lastupdate ?lu .
               }"""
    qres = self.graph.query(query)
    return self.extract_res(qres, ['s', 'abs', 'ab', 'lu', 'name', 'lat', 'long'], disp)

  def getAllFreeStation(self, disp=True):
      query = """PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX  ns:<http://www.semanticweb.org/ontologies/2021/bike#>
                SELECT ?s ?abs ?ab ?lu ?name ?lat ?long  WHERE { 
                    ?s rdf:type ns:StandFreeStation . 
                    ?s rdf:type ns:BikeAvailableStation .
                    ?s ns:Name ?name .
                    ?s ns:Lat ?lat .
                    ?s ns:Long ?long .
                    ?s ns:Name ?name .
                    ?s ns:AvailableBikeStands ?abs .
                    ?s ns:AvailableBikes ?ab .
                    ?s ns:Lastupdate ?lu .
                }"""
      qres = self.graph.query(query)
      return self.extract_res(qres, ['s', 'abs', 'ab', 'lu', 'name', 'lat', 'long'], disp)

  def getBikeFreeStation(self, disp=True):
    query = """PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
               PREFIX  ns:<http://www.semanticweb.org/ontologies/2021/bike#>
               SELECT ?s ?abs ?ab ?lu ?name ?lat ?long  WHERE { 
                  ?s rdf:type ns:BikeAvailableStation . 
                  ?s ns:Name ?name .
                  ?s ns:Lat ?lat .
                  ?s ns:Long ?long .
                  ?s ns:Name ?name .
                  ?s ns:AvailableBikeStands ?abs .
                  ?s ns:AvailableBikes ?ab .
                  ?s ns:Lastupdate ?lu .
               }"""
    qres = self.graph.query(query)
    return self.extract_res(qres, ['s', 'abs', 'ab', 'lu', 'name', 'lat', 'long'], disp)


  def getAllData(self, disp=True):
    query = '''PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
               PREFIX  ns:<http://www.semanticweb.org/ontologies/2021/bike#>
              SELECT ?s ?abs ?ab ?lu ?name ?lat ?long WHERE { 
                  ?s ns:Lat ?lat .
                  ?s ns:Long ?long .
                  ?s ns:Name ?name .
                  ?s ns:AvailableBikeStands ?abs .
                  ?s ns:AvailableBikes ?ab .
                  ?s ns:Lastupdate ?lu .
               }'''
    qres = self.graph.query(query)
    return self.extract_res(qres, ['s', 'abs', 'ab', 'lu', 'name', 'lat', 'long'], disp)

  def getInfo_by_id(self, id, disp=True):
    query = '''PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
               PREFIX  ns:<http://www.semanticweb.org/ontologies/2021/bike#>
               SELECT ?abs ?ab ?lu ?name ?lat ?long WHERE { 
                  ns:'''+str(id)+''' ns:Lat ?lat .
                  ns:'''+str(id)+''' ns:Long ?long .
                  ns:'''+str(id)+''' ns:Name ?name .
                  ns:'''+str(id)+''' ns:AvailableBikeStands ?abs .
                  ns:'''+str(id)+''' ns:AvailableBikes ?ab .
                  ns:'''+str(id)+''' ns:Lastupdate ?lu .
               }'''
    
    qres = self.graph.query(query)
    return self.extract_res(qres, ['abs', 'ab', 'lu', 'name', 'lat', 'long'], disp)
