import requests

email_address = "jseinfeld@crpslab.com"
bearer_token = "Enter Your Token Here in Double Quotes"

API_HEADER =   {'Authorization': 'Bearer ' + bearer_token,
                'Content-Type' : 'application/json',
                'Accept' : '*/*'}

API_RESPONSE = requests.get('https://webexapis.com/v1/people/?email=' + email_address, headers=API_HEADER, verify=True) 
    
if API_RESPONSE.json()["items"]:
    userId = API_RESPONSE.json()["items"][0]["id"]
    print(userId)
else:
    print("No User Found")
