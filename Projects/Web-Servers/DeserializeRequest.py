import json, ssl
import urllib.request
from RandomBlood import RandomBlood

ssl._create_default_https_context = ssl._create_unverified_context

bloodURL = "https://random-data-api.com/api/blood/random_blood"

addresses:RandomBlood = [] 

req = urllib.request.Request(bloodURL)
requestData = json.loads(urllib.request.urlopen(req).read())

for r in requestData:  
    blood:RandomBlood = RandomBlood(**r)
    addresses.append(blood) 
    print(blood.id)