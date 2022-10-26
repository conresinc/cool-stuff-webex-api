import requests, json, pprint

roomList= []

API_URL_PATH = 'https://webexapis.com/v1/'
bearer_token = "Enter Your Token Here in Double Quotes"

def deleteRoom(bearer_token, roomTitle):
    API_URL_ROUTE = 'rooms/'
    API_URL_PARAMETERS = room
    data = {}
    bodyPayloadText = json.dumps(data) 
    FULL_URL = API_URL_PATH + API_URL_ROUTE + API_URL_PARAMETERS
    API_HEADER = {'Authorization': 'Bearer ' + bearer_token, 'Content-Type' : 'application/json', 'Accept' : '*/*'}
    API_RESPONSE = requests.delete(FULL_URL, headers=API_HEADER, data = bodyPayloadText) 
    return API_RESPONSE

with open("rooms.csv", "r") as roomFile:
    roomList = roomFile.readlines()

for room in roomList:
    print("Deleting Room " +  room)

    response = deleteRoom(bearer_token, room)
    pprint.pprint(response)



print("Processing Complete.")