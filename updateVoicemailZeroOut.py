import requests, pprint, json, csv

bearer_token = "Enter Your Token Here in Double Quotes"

userList = {}

with open("voicemail_users.csv", "r") as csv_file:
    dictUserList = csv.DictReader(csv_file)
    line_count = 0

    for user in dictUserList:
        if line_count == 0:
            line_count += 1
        userList[line_count] = {}
        email = (user['#email#'])
        zeroOutEnable = (user['#zeroOutEnable#'])
        destination = (user['#destination#'])
        #print(email + " : " + zeroOutEnable + " : " + destination)
        line_count += 1
        # Part 1 - Get User ID from Email
        
        API_HEADER =   {'Authorization': 'Bearer ' + bearer_token,
                    'Content-Type' : 'application/json',
                    'Accept' : '*/*'}

        API_RESPONSE = requests.get('https://webexapis.com/v1/people/?email=' + email, headers=API_HEADER, verify=True) 
        
        if API_RESPONSE.json()["items"]:
            userId = API_RESPONSE.json()["items"][0]["id"]
            print ("The user ID for the email address " + email + " is :" + userId + "\n")

            # Part 2 - Enable Voicemail Zero Out & Set Destination for User ID

            if zeroOutEnable == "TRUE":
                print("Setting Zero-Out Destination for user " + email + " to " + destination + "\n")
                data = {
                    "transferToNumber": {
                    "enabled": True,
                    "destination" : destination
                        }
                    }
            elif zeroOutEnable == "FALSE":
                print("Disabling Zero Out for user " + email + "\n")
                data = {
                        "transferToNumber": {
                        "enabled": False
                        }
                    }
            
            bodyPayloadText = json.dumps(data)
            API_RESPONSE = requests.put('https://webexapis.com/v1/people/' + userId + "/features/voicemail", headers=API_HEADER, data=bodyPayloadText) 
            print("API Response: " + API_RESPONSE.text + "\n")
        else:
            print("No User Found")