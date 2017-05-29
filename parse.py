import csv
import time
import os
import sys
import re
import json
from pprint import pprint
from selenium import webdriver


def apartment():
  apt_array = []
  with open('apartment.json') as data_file:
    data = json.load(data_file)
  for key in data:
    for apt in (data[key]['data']):
      apt_array.append(apt + " , " + key + " , apartment \n")
  f = open('apartment.csv','w')
  f.write("price , bedrooms , zipcode , city \n")
  for item in apt_array:
    f.write(item)
  return "Complete"

def house():
  apt_array = []
  with open('house.json') as data_file:
    data = json.load(data_file)
  for key in data:
    for apt in (data[key]['data']):
      apt_array.append(apt + " , " + key + " , house \n")
  f = open('house.csv','w')
  f.write("price , bedrooms , zipcode , city \n")
  for item in apt_array:
    f.write(item)
  return "Complete"

if __name__ == "__main__":
  apartment()