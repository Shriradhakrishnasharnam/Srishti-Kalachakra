"""
Srishti Kalachakra - Space Explorer page
Live space data: NASA's picture of the day, current ISS location,
and near-Earth asteroids approaching today.

This file lives inside the 'pages' folder, which is a Streamlit convention:
Streamlit automatically turns every .py file in 'pages/' into an extra page,
listed in the sidebar of the app. No extra setup is needed.
"""

import streamlit as st
import requests
import pandas as pd
from datetime import date
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Space Explorer - Srishti Kalachakra", layout="centered")

st.title("Space Explorer")
st.caption("Live data from NASA and open space APIs")

env_key = os.getenv("NASA_API_KEY")

with st.sidebar:
    st.subheader("NASA API Key")

    if env_key:
        st.success("Using your personal API key (loaded securely from .env).")
    else:
        st.info("Using the shared NASA demo key (rate-limited). Add a key to your .env file for higher limits.")

    override_key = st.text_input(
        "Override key for this session (optional)",
        value="",
        type="password",
        help="Leave blank to use the key from your .env file. Anything typed here is masked and never saved.",
    )

    api_key = override_key if override_key else (env_key or "DEMO_KEY")

st.divider()

# --- Section 1: Astronomy Picture of the Day ---
st.header("Astronomy Picture of the Day")

if st.button("Load Today's Picture"):
    try:
        response = requests.get(
            "https://api.nasa.gov/planetary/apod",
            params={"api_key": api_key},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()

        st.subheader(data.get("title", "Untitled"))

        if data.get("media_type") == "image":
            st.image(data["url"], use_container_width=True)
        elif data.get("media_type") == "video":
            st.video(data["url"])

        st.write(data.get("explanation", "No description available."))
        st.caption(f"Date: {data.get('date', 'unknown')}")

    except requests.exceptions.RequestException as e:
        st.error(f"Could not fetch today's picture. Details: {e}")

st.divider()

# --- Section 2: Live ISS Location ---
st.header("Where is the ISS Right Now")

if st.button("Track ISS"):
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json", timeout=10)
        response.raise_for_status()
        data = response.json()

        lat = float(data["iss_position"]["latitude"])
        lon = float(data["iss_position"]["longitude"])

        col1, col2 = st.columns(2)
        col1.metric("Latitude", f"{lat:.2f}")
        col2.metric("Longitude", f"{lon:.2f}")

        map_data = pd.DataFrame({"lat": [lat], "lon": [lon]})
        st.map(map_data, zoom=1)

    except requests.exceptions.RequestException as e:
        st.error(f"Could not fetch ISS location. Details: {e}")

st.divider()

# --- Section 3: Near-Earth Asteroids Today ---
st.header("Near-Earth Asteroids Approaching Today")

if st.button("Check Asteroids"):
    try:
        today = date.today().isoformat()
        response = requests.get(
            "https://api.nasa.gov/neo/rest/v1/feed",
            params={"start_date": today, "end_date": today, "api_key": api_key},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()

        asteroids_today = data.get("near_earth_objects", {}).get(today, [])

        if not asteroids_today:
            st.write("No tracked close approaches for today.")
        else:
            rows = []
            for obj in asteroids_today:
                approach = obj["close_approach_data"][0]
                rows.append({
                    "Name": obj["name"],
                    "Estimated Diameter (m)": round(
                        obj["estimated_diameter"]["meters"]["estimated_diameter_max"], 1
                    ),
                    "Miss Distance (km)": f"{float(approach['miss_distance']['kilometers']):,.0f}",
                    "Velocity (km/h)": f"{float(approach['relative_velocity']['kilometers_per_hour']):,.0f}",
                    "Potentially Hazardous": "Yes" if obj["is_potentially_hazardous_asteroid"] else "No",
                })

            df = pd.DataFrame(rows)
            st.dataframe(df, use_container_width=True, hide_index=True)

    except requests.exceptions.RequestException as e:
        st.error(f"Could not fetch asteroid data. Details: {e}")

st.divider()
st.caption("Data source: NASA Open APIs (api.nasa.gov) and Open Notify (api.open-notify.org)")
