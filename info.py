
import gmaps
from geopy.geocoders import Nominatim
class Empty:
    pass

#
cidade=Empty();
cidade.data= geolocator.geocode("campina grande, Paraiba")
cidade.coordinates=(cidade.data.latitude,cidade.data.longitude)
#
bombeiros1=Empty();
bombeiros1.data=geolocator.geocode("2º Batalhão de Bombeiro Militar, Av. Prof. Almeida Barreto,<campina grande>")
bombeiros1.coordinates=(bombeiros1.data.latitude,bombeiros1.data.longitude)
#
bombeiros2=Empty();
bombeiros2.data=geolocator.geocode("Aeroporto, Campina Grande")
bombeiros2.coordinates=(bombeiros2.data.latitude,bombeiros2.data.longitude)
#
print(bombeiros1.coordinates,bombeiros2.coordinates,cidade.coordinates)
#
gmaps.configure(api_key="AIzaSyB1MhfDz7x85UyTWQEqtAnKy_4aUwt2HDI")
fig = gmaps.figure(cidade.coordinates,map_type='ROADMAP')
rota1=gmaps.directions_layer(bombeiros2.coordinates, bombeiros1.coordinates,waypoints=[cidade.coordinates])
fig.add_layer(rota1)
fig.add_layer(gmaps.transit_layer())
fig