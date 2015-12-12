__author__ = 'omkardanke'

import requests
class ItemClass:

    def __init__(self, inputLink):
        self.link = inputLink
        self.pageSource = ""

    def getSource(self):
        response = requests.get(self.link)
        self.pageSource = response.text