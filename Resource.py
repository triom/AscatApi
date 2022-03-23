# autheur : Triomphante SONWA
# Projet  : Niryo service du Cafe
# Fichier de creation des classes du projet

# importer le json pour le format de no donées
import json
# importer la bibliotheque Flask qui est notre framework
from flask import Flask, request
from flask_restful import Resource
# importer le fichier de connexion a la base de données
import DatabaseConnection
from DatabaseConnection import firebase


class Resource(Resource):
    def __init__(self, AmountOfWater, NumberOfCapsules):
        self.AmountOfWater= AmountOfWater
        self.NumberOfCapsules = NumberOfCapsules

    dataRessource = {"numCapsule": 1, "tailleCafé": 40}

    # mettre à jour les quantités d'eau  et de capsule de cafés après chaque commande
    @DatabaseConnection.app.route('/ressource', methods=['GET', 'POST'])
    def updateRessources(dataRessource):
      resources = firebase.get('/resources', None)  # recuperer les ressources de notre base de données
      print(resources)
      for dictionary in resources:
        numberCapsules = dictionary["capsules"]  # recuperer le nombre de capsules avant la commande
        waterAmount = dictionary["water"]  # recuperer la quantité d'eau avant la commande
      print(numberCapsules)
      print(waterAmount)
      if dataRessource["numCapsule"] <= numberCapsules and dataRessource["tailleCafé"] <= waterAmount:
        print("On peut faire le café\n")
      else:
        print("oPlus assez de ressources pour faire un café\n")

      return "recuperation des ressources"

