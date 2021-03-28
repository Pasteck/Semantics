import os

def insert_all_owl(AvailableCity):
  for c in AvailableCity:
    os.system(f'python ./owl_inserter/inserter.py "{c}"')


