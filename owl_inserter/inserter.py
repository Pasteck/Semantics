from owlready2 import sync_reasoner_pellet, destroy_entity
from owlready2 import get_ontology
import pickle
import sys

def inserter(file, onto, save_path, reasoner=False):
  with open(file, 'rb') as f:
    triples = pickle.load(f)

  for t in triples:
    subject = t['subject']['value'].split('/')[-1]
    predicate = t['predicate']['value'].split('/')[-1]
    object = convertisor(t['object']) 


    if object != None: 
      s = onto.BikeStation(subject) 
      map_list = {'Name':s.Name, 
                  'Lat':s.Lat, 
                  'Long':s.Long, 
                  'Lastupdate':s.Lastupdate,
                  'AvailableBikes': s.AvailableBikes,
                  'AvailableBikeStands': s.AvailableBikeStands}
      map_list[predicate].append(object)

  pre_reasoner(onto)
  if reasoner:
    with onto:
      sync_reasoner_pellet()
  onto.save(save_path)



def pre_reasoner(onto):
  for i in onto.individuals():
    if i.AvailableBikes == i.AvailableBikeStands == [0]:
      destroy_entity(i)

def convertisor(data):
  _type, o = data['datatype'], data['value']

  if _type == 'xsd:integer':
    try:
      res = int(o)
    except: 
      res = None
  elif _type == 'xsd:decimal':
    try:
      res = float(o)
    except:
      res = None
  elif _type == 'xsd:dateTime':
    res = o
  else: 
    res = o
  return res

def owl_inserter(city):
  onto = get_ontology("./ontology/bike.owl").load()
  inserter(f'./rdf_data/Triple_Bike{city}.obj', onto, f'./ontology/{city}.owl', reasoner=True)

owl_inserter(sys.argv[1])