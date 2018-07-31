import pandas
import folium
map=folium.Map(location=[12.861318, 80.211384],zoom_start=6)
def popcolor(pop):
    if(pop<10000000):
        return "yellow"
    elif(pop<20000000):
        return "green"
    elif(pop<30000000):
        return "blue"
    else:
        return "pink"
def color_producer(no):
    if no < 2000.00:
        c="red"
    elif no<3000.00:
        c="green"
    elif no>=3000.00:
        c="blue"
    return c
data = pandas.read_csv("Volcanoes_USA.txt")
lat=list(data.LAT)
lon=list(data.LON)
name=list(data.ELEV)
fgv=folium.FeatureGroup(name="Volcanoes")
fgp=folium.FeatureGroup(name="Population")
for l,ln,n in zip(lat,lon,name):
        fgv.add_child(folium.CircleMarker(location=[l,ln],radius=6,popup=folium.Popup(str(n)+" m",parse_html=True),
        fill_color=color_producer(n),color='grey',fill=True,fill_opacity=0.7))
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),style_function=lambda x:{'fillColor':'yellow' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] <20000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Mapc_v.html")
