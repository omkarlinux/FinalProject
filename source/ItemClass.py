__author__ = 'omkardanke'

import requests
class ItemClass:

    def __init__(self, inputLink):
        self.link = inputLink
        self.pageSource = ""
        self.cantGetSource = False

    def getSource(self):
        session = requests.session()
        session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        try:
            response = session.get(self.link)
        except requests.exceptions.TooManyRedirects:
            self.cantGetSource = True
        if not self.cantGetSource:
            self.pageSource = response.text
        session.close()

    def showItem(self):
        print(self.link)

    def debugShowSource(self):
        print(self.link)
        print(self.pageSource.splitlines()[0:2])

        #Change for git test
        #Newline