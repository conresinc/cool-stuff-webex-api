import requests
import json

client_id = "C1934caa8bcc778899e006424f280aeb193c0d8991b454e2c4c5aa2054144d6ac"
client_secret = "bfb3eec4240416d72ab8771ff9b78c35dc772b3fa3c759d64b621729c6c16b94"
code = "YTMxODVlYjYtOGZiYS00ODUzLWE3M2MtMTY0ZjMwZjk1YjYxMmEyZWQ2YTAtNjJi_PF84_a9d796ed-c8d6-4f56-b040-d295bdf738cf"
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
