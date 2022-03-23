# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask  #importer la bibliotheque Flask qui est notre framework

#importer le fichier de connexion a la base de données
import DatabaseConnection



if __name__ == '__main__':
    DatabaseConnection.app.run(debug=True)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
