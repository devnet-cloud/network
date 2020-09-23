#! /usr/bin/env python
"""Sample of Get Interface information
"""

# Import libraries
import requests
import sys
import json

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
response=requests.request("POST",url, auth=(USER, PASS),headers=headers, data=payload,  verify=False)
cookies=response.cookies
           
# Run GET interface Eth1/1 information and printing interesting data
url= "https://10.10.20.58/api/mo/sys/intf/phys-[eth1/1].json"
r = requests.request("GET", url, headers = headers, cookies=cookies, verify=False)
r_json = r.json()

print("Interface:"+ r_json["imdata"][0]["l1PhysIf"]["attributes"]["id"])
print("Mode:"+ r_json["imdata"][0]["l1PhysIf"]["attributes"]["mode"])
print("Vlans configuradas:" + r_json["imdata"][0]["l1PhysIf"]["attributes"]["trunkVlans"])
