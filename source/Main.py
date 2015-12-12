__author__ = 'omkardanke'
import json
import os
import datetime
import apiclient
#from .ItemClass import ItemClass
#from .KeywordClass import KeywordClass

def main():
    readFromGoogle = False;         #Toggle to fetch results from google or get from already stored file
    keywordList = ['IBM']                   #Keywords to be searched

    if readFromGoogle:
        service = apiclient.discovery.build('customsearch','v1',developerKey=devKey)
        for keyword in keywordList:
            keywordObject = KeywordClass()

    else:
        outputFiles = os.listdir('../output')
        for keyword in keywordList:
            filesForQuery = []
            for filename in outputFiles:
                if filename.find( keyword ,7,len(filename)-17) > 0:
                    filesForQuery.append(filename)
            filesForQuery.sort(reverse=True)
            if filesForQuery:
                foundFile = filesForQuery[0]
                #print(foundFile)
                results = json.loads(open('../output/' + foundFile).read())
                for item in results["items"]:
                    print(item["link"])





if __name__ == '__main__':
    main()