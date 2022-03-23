# autheur : Triomphante SONWA
# Projet  : Niryo service du Cafe
# Fichier de creation des classes du projet

#importer le json pour le format de no donées
import json
#importer la bibliotheque Flask qui est notre framework
from flask import Flask, request
from flask_restful import Resource
#importer le fichier de connexion a la base de données
import DatabaseConnection
from DatabaseConnection import firebase

class Order(Resource):
  def __init__(self, CoffeeChoice, size):
    self.CoffeeChoice = CoffeeChoice
    self.size = size

  # mettre a jour la donné du choix de café
  @DatabaseConnection.app.route('/order/coffee', methods=['GET'])
  def orderCoffee(dataOrder):
    firebase.put('/order/1', {"coffeeChoice": 9, "size": 3})
    #DatabaseConnection.Database.child("order").child("1").update({"coffeeChoice": 4, "size": 2})
    #return request.method + 'for Debug\n'
