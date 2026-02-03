import streamlit as st
import leafmap.maplibregl as leafmap

st.set_page_config(page_title='My Webpage', page_icon=':tada:', layout='wide')

#  Customize the sidebar
markdown = """
Web App URL: <https://geotemplate.streamlit.app>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# Customize page title
st.title("Streamlit for Geospatial Applications")

st.markdown(
    """
    This multipage app template demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org). It is an open-source project and you are very welcome to contribute to the [GitHub repository](https://github.com/giswqs/streamlit-multipage-template).
    """
)

st.header("Instructions")

m = leafmap.Map(
    center=[-122.19861, 46.21168], zoom=13, pitch=60, bearing=150, style="3d-terrain", projection='globe')
m.add_layer_control(bg_layers=True)
# m.to_html("terrain.html", title="Awesome 3D Map", width="100%", height="100%", replace_key=False)
m.to_streamlit(height=700)
