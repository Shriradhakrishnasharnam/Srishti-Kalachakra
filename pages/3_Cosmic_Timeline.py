"""
Srishti Kalachakra - Cosmic Timeline page
A visual walk through the history of the universe, from the Big Bang
to today, marking the key epochs of cosmic evolution.

This file lives inside the 'pages' folder, so Streamlit automatically
adds it as another page in the sidebar.
"""

import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Cosmic Timeline - Srishti Kalachakra", layout="centered")

st.title("Cosmic Timeline")
st.caption("From the Big Bang to today: the major epochs of the universe")

# Each epoch: name, time since the Big Bang in years (converted from seconds
# where needed), and a short, accurate description.
# A logarithmic scale is used for the chart because the time range covered
# is enormous - from a tiny fraction of a second to 13.8 billion years.
EPOCHS = [
    {
        "name": "Planck Epoch",
        "time_years": 1e-43 / 3.15e7,
        "description": (
            "The earliest moment physics can currently describe, lasting until "
            "about 10^-43 seconds after the Big Bang. Before this point, known "
            "physics (which does not yet unify gravity with quantum mechanics) "
            "breaks down."
        ),
    },
    {
        "name": "Cosmic Inflation",
        "time_years": 1e-33 / 3.15e7,
        "description": (
            "A period of extremely rapid exponential expansion, thought to have "
            "lasted from roughly 10^-36 to 10^-32 seconds after the Big Bang. "
            "This stretched the universe from subatomic scale to macroscopic "
            "scale in a fraction of a second."
        ),
    },
    {
        "name": "Quark Epoch",
        "time_years": 1e-8 / 3.15e7,
        "description": (
            "The universe was a hot, dense soup of quarks, leptons, and photons, "
            "too hot for quarks to bind into protons and neutrons yet."
        ),
    },
    {
        "name": "Big Bang Nucleosynthesis",
        "time_years": 200 / 3.15e7,
        "description": (
            "Between roughly 1 second and 3 minutes after the Big Bang, "
            "protons and neutrons fused to form the first light nuclei: mostly "
            "hydrogen and helium, plus trace lithium."
        ),
    },
    {
        "name": "Recombination (CMB Released)",
        "time_years": 380_000,
        "description": (
            "About 380,000 years after the Big Bang, the universe cooled enough "
            "for electrons to combine with nuclei, forming neutral atoms. Light "
            "could finally travel freely, and this light is what we observe "
            "today as the Cosmic Microwave Background."
        ),
    },
    {
        "name": "Dark Ages",
        "time_years": 100_000_000,
        "description": (
            "A period with no stars or galaxies yet, when the universe was "
            "filled with neutral hydrogen gas and had not yet produced its "
            "first sources of light."
        ),
    },
    {
        "name": "First Stars and Galaxies",
        "time_years": 400_000_000,
        "description": (
            "Around 200 to 400 million years after the Big Bang, gravity pulled "
            "gas together to ignite the first stars, which then grouped into "
            "the first galaxies."
        ),
    },
    {
        "name": "Reionization",
        "time_years": 550_000_000,
        "description": (
            "Radiation from the first stars and galaxies re-ionized the neutral "
            "hydrogen gas filling the universe, making it transparent to "
            "ultraviolet light for the first time since recombination."
        ),
    },
    {
        "name": "Sun and Solar System Form",
        "time_years": 9_200_000_000,
        "description": (
            "About 9.2 billion years after the Big Bang (roughly 4.6 billion "
            "years ago), the Sun and the solar system, including Earth, "
            "formed from a collapsing cloud of gas and dust."
        ),
    },
    {
        "name": "Today",
        "time_years": 13_800_000_000,
        "description": (
            "The universe is approximately 13.8 billion years old, and its "
            "expansion continues to accelerate, driven by dark energy."
        ),
    },
]

# --- Build the timeline chart ---
x_values = [epoch["time_years"] for epoch in EPOCHS]
names = [epoch["name"] for epoch in EPOCHS]

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x_values,
    y=[1] * len(x_values),
    mode="markers+text",
    marker=dict(size=14, color="#4166f5"),
    text=names,
    textposition="top center",
    hovertext=names,
    hoverinfo="text",
))

fig.update_layout(
    xaxis=dict(
        type="log",
        title="Years since the Big Bang (log scale)",
    ),
    yaxis=dict(visible=False, range=[0, 2]),
    height=350,
    margin=dict(l=10, r=10, t=40, b=40),
    showlegend=False,
)

st.plotly_chart(fig, use_container_width=True)

st.caption(
    "The x-axis uses a logarithmic scale because the time span covered here "
    "is vast - from a tiny fraction of a second to 13.8 billion years."
)

st.divider()

# --- Epoch details, selectable ---
st.header("Epoch Details")

epoch_names = [epoch["name"] for epoch in EPOCHS]
selected_name = st.selectbox("Choose an epoch to learn more", epoch_names)

selected_epoch = next(e for e in EPOCHS if e["name"] == selected_name)

st.subheader(selected_epoch["name"])

# Display the time in the most readable unit for its scale.
t = selected_epoch["time_years"]
seconds = t * 3.15e7
if seconds < 60:
    display_time = f"{seconds:.2e} seconds after the Big Bang"
elif seconds < 3600 * 24:
    display_time = f"{seconds / 60:.1f} minutes after the Big Bang"
elif t < 1_000_000:
    display_time = f"{t:,.0f} years after the Big Bang"
else:
    display_time = f"{t / 1_000_000_000:.2f} billion years after the Big Bang"

st.write(f"**When:** {display_time}")
st.write(selected_epoch["description"])
