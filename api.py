"""import urllib.request, json
#Google MapsDdirections API endpoint
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyB1MhfDz7x85UyTWQEqtAnKy_4aUwt2HDI'
#Asks the user to input Where they are and where they want to go.
origin = input("say algo:").replace(' ','+').replace(' ','+').replace(' ','+')
destination = input('Where do you want to go?: ').replace(' ','+').replace(' ','+').replace(' ','+')
#Building the URL for the request
print(origin+" "+ destination)
nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
request = endpoint + nav_request
#Sends the request and reads the response.
response = urllib.request.urlopen(request).read()
#Loads response as JSON
directions = json.loads(response)
print(directions)"""
"""
dsddsd
import cgi, cgitb

data = cgi.FieldStorage()

output = data["var1"] # É assim que você captura os parâmetros passados.

array=data['var1'].value.replace("(",'').replace(')','').split(',')

for x in range(0,len(array)):
    array[x]=float(array[x])
print(array)"""