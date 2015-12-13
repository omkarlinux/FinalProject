__author__ = 'omkardanke'

from source.KeywordClass import KeywordClass

def main():
    keywordList = ['IBM','Oracle','Microsoft','SAP','Intel','Hadoop','SQL']                   #Keywords to be searched

    for keyword in keywordList:
        keyword = keyword.upper()
        keywordObject = KeywordClass(keyword)
        keywordObject.getResults()
        print(keywordObject.keyword)
        #keywordObject.listItems()
        keywordObject.pullSource()
        #keywordObject.debugListItemSource()


if __name__ == '__main__':
    main()