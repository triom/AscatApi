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


class Coffee(Resource):
  def __init__(self, name, intensity, aroma, image):
    self.name = name
    self.intensity = intensity
    self.aroma = aroma
    self.image = image

    @DatabaseConnection.app.route('/order', methods=['GET', 'POST'])
    def post():
      choiceCoffee = {'image': 'gs:/ascat-cbb31.appspot.com/images/ROSSO.jpg', 'name': 'test2', 'intensity': 5,
                      'aroma': 'cer'}
      result = firebase.post('/coffee', choiceCoffee)
      print(result)

    @DatabaseConnection.app.route('/coffee', methods=['GET', 'POST'])
    def getCoffee(self):
      result = firebase.get('/coffee', None)
      return json.dumps(result, indent=4)


class Commande():
  def __init__(self, CoffeeChoice, size):
    self.CoffeeChoice = CoffeeChoice
    self.size = size

  def orderCoffee(self):
    DatabaseConnection.Database.child("order").child("1").update({"coffeeChoice": 4, "size": 2})
    return request.method + 'for Debug\n'


class User():
  def __init__(self, email, password):
    self.telephone =email
    self.password = password
