#Restconf Python

# Converts json data to Python objects and vice versa
import json
#let us send REST request via URL.
import requests
#Disable SSL warnings 
requests.packages.urllib3.disable_warnings()

#URL you want to access on restconf
api_url = "https://192.168.12.2/restconf/data/ietf-interfaces:interfaces"

#headers attached to the REST 
headers = {"Accept" : "application/yang-data+json", "Content-type" : "application/yang-data+json"}

#Authentication 
basicauth = ("cisco", "cisco123!")

#collection variables to perform the RESTconf GET
# Verify = ssl certificates when the request is made!
resp = requests.get (api_url, auth=basicauth, headers=headers,verify=False)
print(resp)

#Print Convert for JSON to Python
response_json = resp.json()

#print (response_json)

print(json.dumps(response_json, indent=4))