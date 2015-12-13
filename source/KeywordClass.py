__author__ = 'omkardanke'
import apiclient
import datetime
import json
import os
from .ItemClass import ItemClass

class KeywordClass:
    def __init__(self, inputKeyword):
        self.keyword = inputKeyword
        self.items = []
        self.hasLocalResult = False

    def getResults(self):
        result = self.getLocalResult()
        if not self.hasLocalResult:
            devKey = open('../documentation/googleCustomSearchAPIKey').read()  #AIzaSyDH0_r3a8C3JJM0j1ofaeh5_3H18trySng'
            customSearchID = open('../documentation/googleSearchEngineID').read()     #010291719019110963087:n9bkswrylmi'
            service = apiclient.discovery.build('customsearch','v1',developerKey=devKey)
            result = service.cse().list(
                    q= self.keyword,
                    cx= customSearchID
                    #num= '100'
                    ).execute()
            with open('../output/result_'
                                  + self.keyword
                                  + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
                                  + '.txt','w') as outfile:
                            json.dump(result,outfile)

        for row in result["items"]:
            itemObject = ItemClass(row["link"])
            self.items.append(itemObject)       #Initialize Item Class



    def getLocalResult(self):
        """

        :rtype : json
        """
        outputFiles = os.listdir('../output')
        filesForQuery = []
        for filename in outputFiles:
            if filename.find(self.keyword ,7,len(filename)-17) > 0:
                filesForQuery.append(filename)
        filesForQuery.sort(reverse=True)
        if filesForQuery:
            foundFile = filesForQuery[0]
            results = json.loads(open('../output/' + foundFile).read())
            self.hasLocalResult = True
            return results

