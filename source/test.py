__author__ = 'omkardanke'

import apiclient

service = apiclient.discovery.build('customsearch','v1')
customSearchObject = service.cse()




