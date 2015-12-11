__author__ = 'omkardanke'
import pprint
import json
import os
import datetime
import apiclient

def main():
    readFromGoogle = False;
    query = 'IBM'
    devKey = 'AIzaSyDH0_r3a8C3JJM0j1ofaeh5_3H18trySng'
    customSearchID = '010291719019110963087:n9bkswrylmi'
    if readFromGoogle:
        service = apiclient.discovery.build('customsearch','v1',developerKey=devKey)
        result = service.cse().list(
           q=query,
          cx= customSearchID
        ).execute()
        with open('../output/result_' + query + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.txt','w') as outfile:
          json.dump(result,outfile)
    else:
        outputFiles = os.listdir('../output')
        filesForQuery = []
        for filename in outputFiles:
            if filename.find('*' + query + '*',7,len(filename)-14):
                filesForQuery.append(filename)
        filesForQuery.sort(reversed)



if __name__ == '__main__':
    main()



