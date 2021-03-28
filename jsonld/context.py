#!/usr/bin/python

# Data properties : [Name, AvailableBikeStands, AvailableBikes, Lastupdate, Lat, Long]

contextLyon = {
  "@vocab": "http://schema.org/",
	"@base": "http://www.semanticweb.org/ontologies/2021/bike/",
  "type":None,
  "properties":"@nest",
    "number": "@id",
    "name": {"@id":"Name", "@type":"xsd:string"},
    "address": None,
    "address2": None,
    "commune": None,
    "nmarrond": None,
    "bonus": None,
    "pole": None,
    "lat": {"@id":"Lat", "@type":"xsd:decimal"},
    "lng": {"@id":"Long", "@type":"xsd:decimal"},
    "bike_stands": None,
    "status": None,
    "available_bike_stands": {"@id":"AvailableBikeStands", "@type":"xsd:integer"},
    "available_bikes": {"@id":"AvailableBikes", "@type":"xsd:integer"},
    "availabilitycode": None,
    "availability": None,
    "banking": None,
    "gid": None,
    "last_update": {"@id":"Lastupdate", "@type":"xsd:dateTime"},
    "last_update_fme": None,
    "code_insee": None,
    "langue": None,
    "etat": None,
    "nature": None,
    "titre": None,
    "description": None,
    "startdate": None,
    "enddate": None,
  "geometry":None
}


contextStEtienne1 = {
  "@vocab": "http://schema.org/",
	"@base": "http://www.semanticweb.org/ontologies/2021/bike/",
  "station_id": "@id",
  "num_bikes_available": {"@id":"AvailableBikes", "@type":"xsd:integer"},
  "num_bikes_disabled": None,
  "num_docks_available": {"@id":"AvailableBikeStands", "@type":"xsd:integer"},
  "is_installed": None,
  "is_renting": None,
  "is_returning": None,
  "last_reported": {"@id":"Lastupdate", "@type":"xsd:dateTime"}
}


contextStEtienne2 = {
  "@vocab": "http://schema.org/",
	"@base": "http://www.semanticweb.org/ontologies/2021/bike/",
  "station_id": "@id",
  "name": {"@id":"Name", "@type":"xsd:string"},
  "lat": {"@id":"Lat", "@type":"xsd:decimal"},
  "lon": {"@id":"Long", "@type":"xsd:decimal"},
  "capacity": None
}


contextParis1 = {
  "@vocab": "http://schema.org/",
	"@base": "http://www.semanticweb.org/ontologies/2021/bike/",
  "stationCode": "@id",
  "station_id": None,
  "num_bikes_available": None,
  "numBikesAvailable": {"@id":"AvailableBikes", "@type":"xsd:integer"},
  "num_bikes_available_types":None,
  "num_docks_available": None,
  "numDocksAvailable": {"@id":"AvailableBikeStands", "@type":"xsd:integer"},
  "is_installed": None,
  "is_returning": None,
  "is_renting": None,
  "last_reported": {"@id":"Lastupdate", "@type":"xsd:dateTime"},
  "rental_methods":None
}

contextParis2 = {
  "@vocab": "http://schema.org/",
	"@base": "http://www.semanticweb.org/ontologies/2021/bike/",
  "station_id": None,
  "name": {"@id":"Name", "@type":"xsd:string"},
  "lat": {"@id":"Lat", "@type":"xsd:decimal"},
  "lon": {"@id":"Long", "@type":"xsd:decimal"},
  "capacity": None,
  "stationCode": "@id",
  "rental_methods":None
}

apis = [
  {
    'name':"BikeLyon",
    'url':"https://download.data.grandlyon.com/wfs/rdata?SERVICE=WFS&VERSION=1.1.0&outputformat=GEOJSON&request=GetFeature&typename=jcd_jcdecaux.jcdvelov&SRSNAME=urn%3Aogc%3Adef%3Acrs%3AEPSG%3A%3A4171",
    'context':contextLyon,
    'root':lambda x:x['features'],
    'double':False
  },
  {
    'name':"BikeStEtienne",
    'url':'https://saint-etienne-gbfs.klervi.net/gbfs/en/station_status.json',
    'context':contextStEtienne1,
    'root': lambda x:x['data']['stations'],
    'double':False
  },
  {
    'name':"BikeStEtienne",
    'url':'https://saint-etienne-gbfs.klervi.net/gbfs/en/station_information.json',
    'context':contextStEtienne2,
    'root':lambda x:x['data']['stations'],
    'double':True
  },
  {
    'name':"BikeParis",
    'url':"https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json",
    'context':contextParis1,
    'root':lambda x:x['data']['stations'],
    'double':False
   },
   {
    'name':"BikeParis",
    'url':"https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json",
    'context':contextParis2,
    'root':lambda x:x['data']['stations'],
    'double':True
   }
]




