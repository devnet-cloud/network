#! /usr/bin/env python
"""Sample of Logging Request
"""

# Import libraries
import requests
import sys
import json
from pprint import pprint

# Use self signed certs
requests.packages.urllib3.disable_warnings()

# Credentials
USER = 'admin'
PASS = 'cisco123'

# URL for GET request
url= "https://10.10.20.58/api/mo/aaaLogin.json"

payload = "{\r\n    \"aaaUser\":{\r\n        \"attributes:{\r\n            \"name\":\"admin\",\r\n            \"pwd\":\"Cisco123\"\r\n        }\r\n    }\r\n}"

# Set yang+jsonas the data formats
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}
           
# Run POST
response = requests.request("POST",url, auth=(USER, PASS),headers=headers, data=payload,  verify=False)
response_json = response.json()
token=(response_json["imdata"][0]["aaaLogin"]["attributes"]["token"])

# Print results
print(token)
