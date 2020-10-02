
import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

LAT = list(data["LAT"])
LON = list(data["LON"])
ELEV = list(data["ELEV"])

def colors(metres):
    if metres < 1000:
        return "green"
    elif 1000 <= metres < 2000:
        return "blue"
    elif 2000 <= metres < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location = [42.894841, 23.908586], min_zoom = 4, zoom_start = 15, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name = "Volcanoes")

for a, b, el in zip(LAT, LON, ELEV):
    fgv.add_child(folium.CircleMarker(location = [a, b], popup = str(el) + "m", radius = 7,
    fill_color = colors(el), color = "black", fill_opacity = 0.9))

fgp = folium.FeatureGroup(name = "Population")

fgp.add_child(folium.GeoJson(data=(open("world.json", "r", encoding="utf-8-sig").read()),
style_function=lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000 
else "orange" if 10000000 <= x["properties"]["POP2005"] < 30000000 else "red"}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")

