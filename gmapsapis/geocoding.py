import googlemaps

gmaps = googlemaps.Client(key='AIzaSyCTdgJ-2dS-fitZL31eZcVxKA0DwximKyw')

# addressComponents: dict = {}
def get_location(formattedAddress: str):
  getlocation = gmaps.geocode(formattedAddress)
  location = {
    "lat": getlocation[0]['geometry']['location']['lat'],
    "lng": getlocation[0]['geometry']['location']['lng']
  }
  return location