import folium
map=folium.Map(location=[12.861318, 80.211384],zoom_start=30)
fg=folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[12.861318, 80.211384],popup="Sreeram is Here!",icon=folium.Icon(color='blue')))
fg.add_child(folium.Marker(location=[12.899242, 80.228082],popup="Sathvik is Here!",icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("Your_location.html")
