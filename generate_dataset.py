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
import time

sys.setrecursionlimit(200)
reload(sys)
sys.setdefaultencoding('utf-8')


with open('DATASET10_results.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(['V1','v1_time_fitness_minutes','v1_distance_fitness_km', 'v1_runtime', 'V2', 'v2_time_fitness_minutes', 'v2_distance_fitness_km', 'v2_runtime', 'V3', 'v3_time_fitness_minutes', 'v3_distance_fitness_km', 'v3_runtime'])
    
    i = 0;

    while (i<20):
        print "Iteration: " + str(i)

        urlV1 = 'http://localhost:5050/api/v1'
        tsV1Start = time.time()
        dataV1 = urllib2.urlopen(urlV1).read()
        tsV1Stop = time.time()
        outputV1 = json.loads(dataV1)

        timeV1 = outputV1['fitness']
        distanceV1 = outputV1['distance']
        runTimeV1 = str(tsV1Stop-tsV1Start)



        urlV2 = 'http://localhost:5050/api/v2'
        tsV2Start = time.time()
        dataV2 = urllib2.urlopen(urlV2).read()
        tsV2Stop = time.time()
        outputV2 = json.loads(dataV2)

        timeV2 = outputV2['fitness']
        distanceV2 = outputV2['distance']
        runTimeV2 = str(tsV2Stop-tsV2Start)



        urlV3 = 'http://localhost:5050/api/v3'
        tsV3Start = time.time()
        dataV3 = urllib2.urlopen(urlV3).read()
        tsV3Stop = time.time()
        outputV3 = json.loads(dataV3)

        timeV3 = outputV3['fitness']
        distanceV3 = outputV3['distance']
        runTimeV3 = str(tsV3Stop-tsV3Start)

        print str(timeV1) + ' ' + str(distanceV1) + ' ' + str(runTimeV1) + ' ' + str(timeV2) + ' ' + str(distanceV2) + ' ' + str(runTimeV2) + ' ' + str(timeV3)+ ' ' + str(distanceV3) + ' ' + str(runTimeV3)
        print ''

        wr.writerow(['', timeV1, distanceV1, runTimeV1, '', timeV2, distanceV2, runTimeV2, '', timeV3, distanceV3, runTimeV3])
        i += 1

print "final array "
