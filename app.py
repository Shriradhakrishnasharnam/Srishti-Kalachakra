"""
Srishti Kalachakra - Interactive Cosmology Toolkit
Entry point application file.

Run this file with:
    streamlit run app.py
"""

import streamlit as st
from astropy.cosmology import Planck18
import astropy.units as u

# --- Page setup ---
st.set_page_config(page_title="Srishti Kalachakra", layout="centered")

st.title("Srishti Kalachakra")
st.caption("An interactive cosmology toolkit")

st.divider()

# --- Calculator: Redshift to Distance ---
st.header("Redshift to Distance Calculator")

st.write(
    "Enter a redshift value (z) to calculate how far away that object is, "
    "and how old the universe was at that time."
)

redshift = st.number_input(
    "Redshift (z)",
    min_value=0.0,
    max_value=20.0,
    value=1.0,
    step=0.1,
)

if st.button("Calculate"):
    # astropy's Planck18 model already knows the standard cosmological
    # parameters (H0, matter density, dark energy density, etc.)
    comoving_distance = Planck18.comoving_distance(redshift)
    luminosity_distance = Planck18.luminosity_distance(redshift)
    angular_diameter_distance = Planck18.angular_diameter_distance(redshift)
    age_at_z = Planck18.age(redshift)
    age_today = Planck18.age(0)
    lookback_time = age_today - age_at_z

    st.subheader("Results")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Comoving Distance", f"{comoving_distance.to(u.Mpc).value:.1f} Mpc")
        st.metric("Luminosity Distance", f"{luminosity_distance.to(u.Mpc).value:.1f} Mpc")

    with col2:
        st.metric("Angular Diameter Distance", f"{angular_diameter_distance.to(u.Mpc).value:.1f} Mpc")
        st.metric("Age of Universe at z", f"{age_at_z.to(u.Gyr).value:.2f} Gyr")

    st.write(f"Lookback time: **{lookback_time.to(u.Gyr).value:.2f} billion years**")

st.divider()
st.caption("Cosmological model used: Planck 2018 (H0 = 67.66 km/s/Mpc)")
