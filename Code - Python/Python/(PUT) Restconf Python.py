#Restconf Python

# Converts json data to Python objects and vice versa
import json
#let us send REST request via URL.
import requests
#Disable SSL warnings 
requests.packages.urllib3.disable_warnings()

#URL you want to access on restconf
api_url = "https://192.168.10.1/restconf/data/ietf-interfaces:interfaces/interface=Loopback3"

#headers attached to the REST 
headers = {"Accept" : "application/yang-data+json", "Content-type" : "application/yang-data+json"}

#Authentication 
basicauth = ("cisco", "cisco123!")

#Config you want to implement
yangconfig= {
    "ietf-interfaces:interface": {
        "name": "Loopback3",
        "description": "Link to PC",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "192.168.12.1",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

#collection variables to perform the RESTconf PUT
# Verify = ssl certificates when the request is made!
resp = requests.put (api_url, data=json.dumps(yangconfig), auth=basicauth, headers=headers,verify=False)
print(resp.status_code)

#Print Convert for JSON to Python
#response_json = resp.json()

#print (response_json)
#print(json.dumps(response_json, indent=4))