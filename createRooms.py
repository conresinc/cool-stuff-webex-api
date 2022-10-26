import requests, json, pprint

createdList = []
newroomlist = []

API_URL_PATH = 'https://webexapis.com/v1/'
bearer_token = "Enter Your Token Here in Double Quotes"

def createRoom(bearer_token, roomTitle):
    API_URL_ROUTE = 'rooms'
    API_URL_PARAMETERS = ""
    data = { 
    "title": roomTitle,
        
    }
    bodyPayloadText = json.dumps(data) 
    FULL_URL = API_URL_PATH + API_URL_ROUTE + API_URL_PARAMETERS
    API_HEADER = {'Authorization': 'Bearer ' + bearer_token, 'Content-Type' : 'application/json', 'Accept' : '*/*'}
    API_RESPONSE = requests.post(FULL_URL, headers=API_HEADER, data = bodyPayloadText) 
    return API_RESPONSE


def createMessage(bearer_token, room, message):
    API_URL_ROUTE = 'messages'
    API_URL_PARAMETERS = ""
    data = { 
    "roomId": room, 
    "text" : message

    }

    bodyPayloadText = json.dumps(data) 
    FULL_URL = API_URL_PATH + API_URL_ROUTE + API_URL_PARAMETERS
    API_HEADER = {'Authorization': 'Bearer ' + bearer_token, 'Content-Type' : 'application/json', 'Accept' : '*/*'}
    API_RESPONSE = requests.post(FULL_URL, headers=API_HEADER, data = bodyPayloadText) 
    return API_RESPONSE


with open("rooms_to_create.txt", "r") as rooms_to_create:
    new_rooms = rooms_to_create.readlines()

for room in new_rooms:
    print("Adding Room " +  room)
    response = createRoom(bearer_token, room)
    if response.json()["id"]:
        print("Room Created")
        id = response.json()["id"]
        title = response.json()["title"]
        createdList.append(id)
    else:
        print("No id Found")

pprint.pprint(createdList)

print("Open File for Writing")
f = open("rooms.csv", "w")
        
for row in createdList:
    message = "Hello World!"
    createMessage(bearer_token, row, message)
    f.write(row)
    f.write("\n")

print("Processing Complete.")