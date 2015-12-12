__author__ = 'omkardanke'

class KeywordClass:
    def __init__(self, inputKeyword):
        self.keyword = inputKeyword

    def getResults(self):
        devKey = open('../documentation/googleCustomSearchAPIKey').read()  #AIzaSyDH0_r3a8C3JJM0j1ofaeh5_3H18trySng'
        customSearchID = open('../documentation/googleSearchEngineID').read()     #010291719019110963087:n9bkswrylmi'
        service = apiclient.discovery.build('customsearch','v1',developerKey=devKey)
        result = service.cse().list(
                q= self.keyword,
                cx= customSearchID
                #num= '100'
                ).execute()
        with open('../output/result_'
                              + keyword
                              + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
                              + '.txt','w') as outfile:
        json.dump(result,outfile)

