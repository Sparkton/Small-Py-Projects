#!/usr/bin/env python
# coding: utf-8

# In[2]:


import folium as fo
import pandas as pn


# In[3]:


df = pn.read_excel("volcan.xlsx")
df


# In[ ]:


lat = list(df["Latitude"])
lon = list(df["Longitude"])
elev = list(df["Elev"])


# In[ ]:


map = fo.Map(location=[40, -100],zoom_start=6,tiles="Mapbox Bright")


# In[ ]:


fgv = fo.FeatureGroup("Volcanoes")


# In[ ]:


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


# In[ ]:


for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(fo.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" m",
    fill_color=color_producer(el), fill=True,  color = 'grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(fo.LayerControl())

map.save("Map1.html")


# In[ ]:




