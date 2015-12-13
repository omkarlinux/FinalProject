#!/usr/local/bin/python3
__author__ = 'omkardanke'

from KeywordClass import KeywordClass
from tabulate import tabulate
import sys

def main():
    keywordList = sys.argv[1:]
    keywordObjectList = []

    for keyword in keywordList:
        keyword = keyword.upper()
        keywordObject = KeywordClass(keyword)
        keywordObject.getResults()
        keywordObject.pullSource()
        keywordObject.getKeywordCount()
        keywordObjectList.append(keywordObject)
    printRank(keywordObjectList)

def printRank(keywordObjectList):
    print("\n\nCalculating ranks for keywords...")
    keywordObjectList.sort(key=lambda keywordItem : keywordItem.count, reverse=True)
    printList = []
    for rank, keywordItem in enumerate(keywordObjectList):
        printList.append([rank + 1, keywordItem.keyword, keywordItem.count])
    print("\n\n" + tabulate(printList,headers=["Rank","Keyword", "Count"]))


if __name__ == '__main__':
    main()