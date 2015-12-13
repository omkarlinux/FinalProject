__author__ = 'omkardanke'

from .KeywordClass import KeywordClass

def main():
    readFromGoogle = False;         #Toggle to fetch results from google or get from already stored file
    keywordList = ['IBM']                   #Keywords to be searched

    if readFromGoogle:
        for keyword in keywordList:
            keyword = keyword.capitalize()
            keywordObject = KeywordClass()
            keywordObject.getResults()

if __name__ == '__main__':
    main()