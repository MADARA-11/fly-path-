import cartopy.crs as ccrs
import streamlit as st
import cartopy.feature as feature
import matplotlib.pyplot as plt
from io import BytesIO

cities ={
    'New York': [40.7128, -74.0059],
    'London': [51.5074, -0.1278],
    'Tokyo': [35.6895,139.6917],
    'Sydney': [-33.8688,151.2093],
    'Cape Town': [-33.9249,18.4241],
    'Rio de Janeiro': [-22.9068,-43.1729],
    'Paris': [48.8566,2.3522 ],
    'Moscow': [55.7558,37.6173],
    'Mumbai': [ 19.0760,72.8777]
}

st.title("🕊️ the  fly linepath")

city_name = cities.keys()
city_name = list(city_name)

city1 = st.selectbox("select the departure:",city_name)
city2 = st.selectbox("select the arrival city",city_name)


if st.button("Generate path"):
    if city1 == city2:
        st.warning("please enter a different city:")
    else:
        lat1,long1 = cities[city1]
        lat2,long2 = cities[city2]
        fig = plt.figure(figsize=(9,9))
        ax = fig.add_subplot(1,1,1,projection = ccrs.PlateCarree())

        ax.set_extent([-180,180,-90,90], crs = ccrs.PlateCarree())

        ax.add_feature(feature.OCEAN,facecolor = "lightblue",alpha = 0.6)
        ax.add_feature(feature.LAND,facecolor = "lightgreen",alpha = 0.6)
        ax.add_feature(feature.RIVERS)
        ax.add_feature(feature.COASTLINE)

        ax.coastlines()
        plt.title('World Map')

        for city, (lat, lon) in cities.items():
            ax.plot(lon, lat, color='red', marker='o', ms=6, transform=ccrs.PlateCarree())
            ax.text(lon + 5, lat - 2, city, color='green', transform=ccrs.PlateCarree())

        lat_ny, lon_ny = cities[city1]
        lat_r, lon_r = cities[city2]

        ax.plot([lon_ny, lon_r], [lat_ny, lat_r], color="blue", linewidth=2, marker='o', transform=ccrs.Geodetic())

        st.pyplot(fig)
        img = BytesIO()
        fig.savefig(img,format='png')
        img.seek(0)


        st.download_button(
            label="download",
            data=img,
            file_name=f"fyl path between{city1}and {city2}.png",
            mime="image/png"
        )
