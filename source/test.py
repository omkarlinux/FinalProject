__author__ = 'omkardanke'
import pprint
import json
import os
import datetime
import apiclient

def main():
    readFromGoogle = False;         #Toggle to fetch results from google or get from already stored file
    keywordList = ['IBM']                   #Keywords to be searched
    devKey = open('../documentation/googleCustomSearchAPIKey').read()  #AIzaSyDH0_r3a8C3JJM0j1ofaeh5_3H18trySng'
    customSearchID = open('../documentation/googleSearchEngineID').read()     #010291719019110963087:n9bkswrylmi'
    if readFromGoogle:
        service = apiclient.discovery.build('customsearch','v1',developerKey=devKey)
        for keyword in keywordList:
            #Get search results from google search
            result = service.cse().list(
                q= keyword,
                cx= customSearchID
                #num= '100'
                ).execute()
            with open('../output/result_'
                              + keyword
                              + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
                              + '.txt','w') as outfile:
                json.dump(result,outfile)
    else:
        outputFiles = os.listdir('../output')
        print(outputFiles)
        for keyword in keywordList:
            filesForQuery = []
            for filename in outputFiles:
                if filename.find( keyword ,7,len(filename)-17) > 0:
                    print('keyword ' + keyword + ', filename ' + filename)
                    filesForQuery.append(filename)
            filesForQuery.sort(reverse=True)
            if filesForQuery:
                foundFile = filesForQuery[0]
                print(foundFile)
                #result = json.loads(open('../output/' + foundFile).read())
                #print(result["context"])


if __name__ == '__main__':
    main()