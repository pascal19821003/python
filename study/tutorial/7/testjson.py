#!/usr/bin/env python3
#import json

#dumps = json.dumps([1, 'simple', 'list'])
#print(dumps)

import json

print(json.__file__)

with open("test.json") as json_file:
    json_data = json.load(json_file)
    print(json_data)