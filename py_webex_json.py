import requests
import json
import time
choice = input("Do you wish to use the hard coded token? (y/n)")

if choice == "N" or choice == "n":
	accessToken = input("Enter your access token: ")
	accessToken = "Bearer " + accessToken
else: 
	accessToken = "Bearer YTg1NmRmYzEtZWIyNS00OTRhLTg0YWQtMmU4MzU2Mjg1NDgzZjlhMTg1MDItZDc0_P0A1_49d1e4bd-2a1c-4119-b74e-be561ec00408"
	# Using the requests library, create a new HTTP GET Request against the 
# Webex Teams API Endpoint for Webex Teams Rooms:
# The local object "r" will hold the returned data:
r = requests.get(   "https://api.ciscospark.com/v1/rooms",
                    headers={'Authorization':accessToken}
                )
# Check if the response from the API call was OK (resp. code 200)
if(r.status_code != 200):
    print("Something wrong has happened:")
    print("ERROR CODE: {} \nRESPONSE: {}".format(r.status_code, r.text))
    assert()
def setHeaders():         
	spark_header = {'Authorization': accessToken, 
                    'Content-Type': 'application/json; charset=utf-8'}
	return spark_header

def getRooms(theHeader):    
	uri = 'https://api.ciscospark.com/v1/rooms'  
	resp = requests.get(uri, headers=theHeader)
	return resp.json()

header = setHeaders()
value = getRooms(header)
# See what is in the JSON data:

jsonData = r.json()

print(
    json.dumps(
        jsonData,
        indent=4
    )
)
rooms = jsonData['items']
for room in rooms:
    print ("Room name: '" + room['title'] + "' ID: " + room['id'])
# Define a variable that will hold the roomId 
roomIdToMessage = None

while True:
    roomNameToSearch = input('Enter full or partial name of the room to find: ')
    rooms = jsonData['items']
    for room in rooms:
        if(room['title'].find(roomNameToSearch) != -1):
            print ("Found rooms with the word " + roomNameToSearch)
            print ("Room name: '" + room['title'] + "' ID: " + room['id'])
            roomIdToMessage = room['id']
            roomTitleToMessage = room['title']
            break

    if(roomIdToMessage == None):
        print("Did not find a room with " + roomNameToSearch + " in it.")
        print("\nPlease try again...")
    else:
        break
