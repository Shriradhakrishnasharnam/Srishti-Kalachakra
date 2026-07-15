"""
Srishti Kalachakra - Solar System Explorer page
An interactive 3D view of the solar system, with real relative distances
and facts about each planet.

This file lives inside the 'pages' folder, so Streamlit automatically
adds it as another page in the sidebar, alongside app.py and Space Explorer.
"""

import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Solar System Explorer - Srishti Kalachakra", layout="centered")

st.title("Solar System Explorer")
st.caption("An interactive 3D map of our solar system")

# --- Planet data ---
# distance_au: average distance from the Sun, in astronomical units (1 AU = Earth-Sun distance)
# relative_size: for the marker size on the chart only (not to real scale - true sizes
#   would make the inner planets invisible next to Jupiter and the Sun)
# color: rough real-world color of each planet
# facts: a short, genuinely useful fact about each one
PLANETS = [
    {"name": "Mercury", "distance_au": 0.39, "relative_size": 6,  "color": "#9c9c9c",
     "facts": "Smallest planet. A year on Mercury lasts only 88 Earth days."},
    {"name": "Venus",   "distance_au": 0.72, "relative_size": 9,  "color": "#e8cda2",
     "facts": "Hottest planet in the solar system due to a thick CO2 atmosphere, even hotter than Mercury."},
    {"name": "Earth",   "distance_au": 1.00, "relative_size": 9,  "color": "#3d7dca",
     "facts": "The only known planet with life. One full orbit takes 365.25 days."},
    {"name": "Mars",    "distance_au": 1.52, "relative_size": 7,  "color": "#c1440e",
     "facts": "Home to Olympus Mons, the tallest volcano in the solar system."},
    {"name": "Jupiter", "distance_au": 5.20, "relative_size": 20, "color": "#d8ba7d",
     "facts": "Largest planet. Its Great Red Spot is a storm bigger than Earth."},
    {"name": "Saturn",  "distance_au": 9.58, "relative_size": 18, "color": "#e3ce9d",
     "facts": "Known for its ring system, made mostly of ice and rock particles."},
    {"name": "Uranus",  "distance_au": 19.20, "relative_size": 13, "color": "#a8dce0",
     "facts": "Rotates almost on its side, likely due to an ancient collision."},
    {"name": "Neptune", "distance_au": 30.05, "relative_size": 13, "color": "#4166f5",
     "facts": "Windiest planet, with storms reaching over 1,500 mph (2,400 km/h)."},
]

st.write(
    "Distances below are shown to real relative scale (in astronomical units, "
    "where 1 AU is the distance from Earth to the Sun). Planet sizes on the "
    "chart are exaggerated for visibility, not to real scale."
)

# --- Build the 3D figure ---
fig = go.Figure()

# The Sun, at the center
fig.add_trace(go.Scatter3d(
    x=[0], y=[0], z=[0],
    mode="markers",
    marker=dict(size=25, color="#FDB813"),
    name="Sun",
    hovertext=["The Sun: our star, containing 99.8% of the solar system's mass."],
    hoverinfo="text",
))

# Each planet's orbit path (a full circle) and its current position marker
for planet in PLANETS:
    r = planet["distance_au"]
    theta = np.linspace(0, 2 * np.pi, 200)
    orbit_x = r * np.cos(theta)
    orbit_y = r * np.sin(theta)
    orbit_z = np.zeros_like(theta)

    fig.add_trace(go.Scatter3d(
        x=orbit_x, y=orbit_y, z=orbit_z,
        mode="lines",
        line=dict(color="gray", width=1),
        showlegend=False,
        hoverinfo="skip",
    ))

    # place the planet marker at a fixed point on its orbit
    fig.add_trace(go.Scatter3d(
        x=[r], y=[0], z=[0],
        mode="markers",
        marker=dict(size=planet["relative_size"], color=planet["color"]),
        name=planet["name"],
        hovertext=[f"{planet['name']}: {planet['distance_au']} AU from the Sun"],
        hoverinfo="text",
    ))

fig.update_layout(
    scene=dict(
        xaxis=dict(showbackground=False, showticklabels=False, title=""),
        yaxis=dict(showbackground=False, showticklabels=False, title=""),
        zaxis=dict(showbackground=False, showticklabels=False, title=""),
        aspectmode="data",
    ),
    margin=dict(l=0, r=0, t=0, b=0),
    height=600,
    showlegend=True,
)

st.plotly_chart(fig, use_container_width=True)

st.caption("Tip: click and drag to rotate the view. Scroll to zoom.")

st.divider()

# --- Planet facts, selectable ---
st.header("Planet Facts")

planet_names = [p["name"] for p in PLANETS]
selected_name = st.selectbox("Choose a planet", planet_names)

selected_planet = next(p for p in PLANETS if p["name"] == selected_name)

col1, col2 = st.columns(2)
col1.metric("Distance from Sun", f"{selected_planet['distance_au']} AU")
col2.metric(
    "Distance in km (approx.)",
    f"{selected_planet['distance_au'] * 149_600_000:,.0f} km",
)

st.write(selected_planet["facts"])
