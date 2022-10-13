import requests
import json

client_id = "Your Client ID in double quotes"
client_secret = "Your Client Secret in double quotes"
code = "Your OAuth Authorization Code in double quotes"
redirect_uri = 'http://www.cisco.com'

API_BASE_URL = "https://webexapis.com/v1/access_token"


def getTokenFromCode(client_id,client_secret,code,redirect_uri):
    data = {'grant_type': 'authorization_code',
            'client_id' : client_id,
            'client_secret' : client_secret,
            'code' : code,
            'redirect_uri' : redirect_uri}
            
    bodyPayloadText = json.dumps(data) 
    API_HEADERS = { 'Content-Type' : 'application/json'}
    API_RESPONSE = requests.post(API_BASE_URL, headers=API_HEADERS, data = bodyPayloadText) 
    access_token = API_RESPONSE.json()
    return access_token

results = getTokenFromCode(client_id,client_secret,code,redirect_uri)
print("Access Token is: ")
print(results['access_token'])
print("\n")
print("Complete JSON Response: \n")
print(results)
