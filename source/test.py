__author__ = 'omkardanke'

import apiclient

def main():
    service = apiclient.discovery.build('customsearch','v1',developerKey='AIzaSyDH0_r3a8C3JJM0j1ofaeh5_3H18trySng')
    result = service.cse().list(
        q='IBM',
        cx='010291719019110963087:n9bkswrylmi'
    ).execute()
    print(result)


if __name__ == '__main__':
    main()



