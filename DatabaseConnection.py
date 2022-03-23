######
# autheur : Triomphante SONWA
# Projet  : Niryo service du Cafe
# Fonction pour la creation de nos classes et connection a la base de données Nosql

#importation des packages neccessaires
import json

import listener as listener
import pyrebase
import firebase_admin
from flask import Flask, request
from firebase_admin import credentials, firestore
from firebase import firebase


#crée l'objet application flask
app = Flask(__name__)

# Authentification et Initialisation de la base de données Firestore
firebase = firebase.FirebaseApplication('https://ascat-cbb31-default-rtdb.europe-west1.firebasedatabase.app/', None)
cred = credentials.Certificate('APIAccountKey.json')
firebase_admin.initialize_app(cred)

#extraction de la cle d'API
firebaseConfig = {"apiKey": "AIzaSyBSMoPq9LbUPrUXw8GsFf4e35YH63IrcAI",
                  "authDomain": "ascat-cbb31.firebaseapp.com",
                  "databaseURL": "https://ascat-cbb31-default-rtdb.europe-west1.firebasedatabase.app",
                  "projectId": "ascat-cbb31",
                  "storageBucket": "ascat-cbb31.appspot.com",
                  "messagingSenderId": "369545117327",
                  "appId": "1:369545117327:web:0d1ab1417adbf30bef7afa",
                  "measurementId": "G-SEHWJ8YRB1"}

fbase = pyrebase.initialize_app(firebaseConfig)
Database = fbase.database()

#useless just a test works for post

@app.route('/orders', methods=['GET', 'POST'])
def post():
  choiceCoffee = {'image': 'gs:/ascat-cbb31.appspot.com/images/ROSSO.jpg', 'name': 'test', 'intensity': 5,
                  'aroma': 'cer'}
  result = firebase.post('/coffee', choiceCoffee)
  print(result)

#mettre a jour la donné du choix de café
@app.route('/order/coffee1', methods=['GET'])
def orderCoffee():
    #recuper toutes les  commande
    results = firebase.get('/orderBuffer', None)
    print(results)
    #recuper la clé de la commande la plud ancienne
    idToRemove = list(results.keys())[-1]
    print(idToRemove)
    #recuper la valeur la plus ancienne
    result = results.pop(list(results.keys())[-1]) #la commande la plus ancienne
    print(results)
    print(result)
    #mettre a jour la donnée pour le robot
    Database.child("order").child("1").update({"coffeeChoice": result["coffeeChoice"], "size": result["quantity"]})
    #supprimer de la bd l'ancienne valeur
    return json.dumps(result, indent=4)


#enregistrer la commande  d'un café
@app.route('/order', methods=['GET', 'POST'])
def fillOrderBUffer():
    choiceCoffee = {'coffeeChoice': 2, 'quantity': 0}
    result = firebase.post('/orderBuffer', choiceCoffee)
    return json.dumps(choiceCoffee, indent=4)


#afficher la liste des cafés

@app.route('/coffee', methods=['GET', 'POST'])
def getCoffee():
    result = firebase.get('/coffee', None)
    return json.dumps(result, indent=4)

@app.route('/ressource', methods=['GET'])
def manageResources():
    coffee = {"coffeeChoice": 1, "quantity": 1}
    resources = firebase.get('/resources', None)  # recuperer les ressources de notre base de données
    # debug
    print(resources)

    for dictionary in resources:
        numberCapsules = dictionary["capsules"]  # recuperer le nombre de capsules avant la commande
        waterAmount = dictionary["water"]  # recuperer la quantité d'eau avant la commande

    # debug
    print(numberCapsules)
    print(waterAmount)
    # reduire le niveau d"='eau et le nombre de capsules
    if (coffee["quantity"] == 0):
        dataRessource = {"numCapsule": 1, "tailleCafé": 40}
    if (coffee["quantity"] == 1):
        dataRessource = {"numCapsule": 1, "tailleCafé": 80}

    if dataRessource["numCapsule"] <= numberCapsules and dataRessource["tailleCafé"] <= waterAmount:
        print("On peut faire du café\n")
        numberCapsules -= dataRessource["numCapsule"]
        waterAmount -= dataRessource["tailleCafé"]

        # mettre à jour les valeurs finales
        firebase.put('/resources/0', 'capsules', numberCapsules)
        firebase.put('/resources/0', 'water', waterAmount)
        return "coffe done"
    else:
        return "coffee not done"


def ActionListener(event):
    print(event.event_type)
    print(event.path)
    print(event.data)
    firebase_admin.db.reference('/listen').listen(listener)
    return "data has changed"

