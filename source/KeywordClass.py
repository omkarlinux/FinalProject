__author__ = 'omkardanke'
import apiclient
import datetime
import json
import os
from ItemClass import ItemClass

class KeywordClass:
    def __init__(self, inputKeyword):
        self.keyword = inputKeyword
        self.items = []
        self.hasLocalResult = False
        self.count = 0

    def getResults(self):
        result = self.getLocalResult()
        if not self.hasLocalResult:
            print("No locally stored result. Fetching result from Google...")
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
            print("Result stored locally for next time.")

        for row in result["items"]:
            itemObject = ItemClass(row["link"])
            self.items.append(itemObject)       #Initialize Item Class



    def getLocalResult(self):
        """

        :rtype : json
        """
        print("\nLooking for local search results for \"" + self.keyword + "\"...")
        outputFiles = os.listdir('../output')
        filesForQuery = []
        for filename in outputFiles:
            if filename[len(filename)-18:len(filename)-10] == datetime.datetime.now().strftime('%Y%m%d') and filename.find(self.keyword ,7,len(filename)-17) > 0:
                filesForQuery.append(filename)
        filesForQuery.sort(reverse=True)
        if filesForQuery:
            foundFile = filesForQuery[0]
            results = json.loads(open('../output/' + foundFile).read())
            print("Found locally stored result.")
            self.hasLocalResult = True
            return results

    def listItems(self):
        for item in self.items:
            item.showItem()

    def pullSource(self):
        print("Getting source code from links...")
        for item in self.items:
            item.getSource()

    def debugListItemSource(self):
        for item in self.items:
            item.debugShowSource()

    def getKeywordCount(self):
        keywordOccurances = 0
        for item in self.items:
            keywordOccurances = item.countInSource(self.keyword)
            self.count = self.count + keywordOccurances

    def showCount(self):
        print(self.keyword + " = " + self.count.__str__())