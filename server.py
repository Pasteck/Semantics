from flask import Flask, request
from owl_inserter.main import insert_all_owl
from queries.main import queries_builder
from jsonld.main import load_all

app = Flask(__name__)

AvailableCity = [ 'StEtienne', 'Lyon','Paris']
ontologies = [f'./ontology/{c}.owl' for c in AvailableCity]
querier = queries_builder(ontologies)


@app.route('/api/reload_all')
def reload_all():
  global querier
  load_all()
  insert_all_owl(AvailableCity)
  querier = queries_builder(ontologies)
  return {'res':True}

@app.route('/api/getinfo_by_id')
def getinfo_by_id():
  id = request.args.get('id', default = '10006', type = str)
  city = request.args.get('city', default = 'Paris', type = str)
  response = querier[city].getInfo_by_id(id, disp=False)
  response = {"body":response}
  return response



@app.route('/api/getAllFreeStation')
def getAllFreeStation():
  city = request.args.get('city', default = 'Paris', type = str)
  response = querier[city].getAllFreeStation(disp=False)
  response = {"body":response}
  return response

@app.route('/api/getStandFreeStation')
def getStandFreeStation():
  city = request.args.get('city', default = 'Paris', type = str)
  response = querier[city].getStandFreeStation(disp=False)
  response = {"body":response}
  return response

@app.route('/api/getBikeFreeStation')
def getBikeFreeStation():
  city = request.args.get('city', default = 'Paris', type = str)
  response = querier[city].getBikeFreeStation(disp=False)
  response = {"body":response}
  return response


@app.route('/api/getAllData')
def getAllData():
  city = request.args.get('city', default = 'Paris', type = str)
  if city in AvailableCity:
    response = querier[city].getAllData(disp=False)
  else:
    response = f"<h1>City unknown:{city} </h1>"
  response = {"body":response}
  return response

app.run(port=5000)