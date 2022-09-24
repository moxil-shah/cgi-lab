#!/usr/bin/env python3

import os
import json
# print("Content-Type: text/plain")
# print()
# print(os.environ)

print("Content-Type: application/json")
print()
d = dict(os.environ)
print(json.dumps(d, indent=2))
print(d['INFOPATH'])
