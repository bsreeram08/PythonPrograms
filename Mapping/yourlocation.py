import geocoder
import folium
g = geocoder.ip('me')
map=folium.Map(location=g.latlng,zoom_start=30)
map.save("Your_location.html")
