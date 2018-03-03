# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup, SoupStrainer

import httplib2
import requests
from urlparse import urlparse
from requests.exceptions import ConnectionError
import re
import sys
import csv
import requests as rq
import validators
import time
import csv
import random
import json
import itertools
import random
import psycopg2

sys.setrecursionlimit(200)
reload(sys)
sys.setdefaultencoding('utf-8')


with open('DATASET10_results.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(['V1','v1_time_fitness_minutes','v1_distance_fitness_km', 'V2', 'v2_time_fitness_minutes', 'v2_distance_fitness_km', 'V3', 'v3_time_fitness_minutes', 'v3_distance_fitness_km'])
    
    i = 0;

    while (i<20):
        print "Iteration: " + str(i)

        urlV1 = 'http://localhost:8080/api/v1'
        dataV1 = urllib2.urlopen(urlV1).read()
        outputV1 = json.loads(dataV1)

        timeV1 = outputV1['fitness']
        distanceV1 = outputV1['distance']

        urlV2 = 'http://localhost:8080/api/v2'
        dataV2 = urllib2.urlopen(urlV2).read()
        outputV2 = json.loads(dataV2)

        timeV2 = outputV2['fitness']
        distanceV2 = outputV2['distance']

        urlV3 = 'http://localhost:8080/api/v3'
        dataV3 = urllib2.urlopen(urlV3).read()
        outputV3 = json.loads(dataV3)

        timeV3 = outputV3['fitness']
        distanceV3 = outputV3['distance']

        print str(timeV1) + ' ' + str(distanceV1) + ' ' + str(timeV2) + ' ' + str(distanceV2) + ' ' + str(timeV3)+ ' ' + str(distanceV3)
        print ''

        wr.writerow(['', timeV1, distanceV1, '', timeV2, distanceV2, '', timeV3, distanceV3])
        i += 1

print "final array "
