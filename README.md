# Srishti Kalachakra
### (Srishti Kalachakra — Creation, Wheel of Time - The Cosmos Explorer)
**An interactive cosmology toolkit — calculators, simulations, and visualizations for exploring the universe, right in your browser.**

Srishti Kalachakra is a from-scratch web application for exploring the fundamentals of cosmology: from calculating cosmological distances and redshifts, to simulating the expansion of the universe, to visualizing the cosmic microwave background and large-scale structure. It's built to be both a hands-on learning tool and a reference-grade scientific calculator — named for creation (*srishti*) and the ever-turning wheel of cosmic time (*kalachakra*).

> This is an original project, not a fork — built to combine rigorous cosmological computation with an approachable, interactive UI.

---

## Features

### Calculators
- **Cosmological Distance Calculator** — compute comoving distance, luminosity distance, and angular diameter distance for a given redshift, using standard ΛCDM parameters (H₀, Ωₘ, ΩΛ, Ωₖ)
- **Redshift ↔ Age Converter** — convert between redshift `z`, lookback time, and age of the universe at that epoch
- **Hubble Parameter Explorer** — visualize how H(z) evolves with redshift under different cosmological models
- **Custom Cosmology Presets** — switch between Planck 2018, WMAP9, and fully custom parameter sets

### Simulations
- **Expansion of the Universe** — interactive scale-factor `a(t)` simulation showing how the universe's expansion rate changes across matter-dominated, radiation-dominated, and dark-energy-dominated eras
- **N-body Gravity Sandbox** — lightweight particle simulation demonstrating gravitational clustering and structure formation
- **Friedmann Equation Playground** — adjust Ωₘ, ΩΛ, Ωᵣ, Ωₖ sliders and watch the expansion history respond in real time

### Visualizations
- **Cosmic Timeline** — a scrollable, zoomable timeline from the Big Bang to today, marking key epochs (inflation, recombination, first stars, reionization)
- **CMB Power Spectrum Viewer** — interactive plot of the angular power spectrum with annotated acoustic peaks
- **3D Observable Universe Map** — a Three.js-powered explorable scene illustrating scale, from Earth to the observable universe horizon

### Learning Modules
- Short, illustrated explainers on core concepts: redshift, the Friedmann equations, dark energy, the CMB, and the distance ladder
- Every calculator and simulation links back to the relevant explainer, so the tool doubles as a study companion

---

## Tech Stack

| Layer | Technology |
|---|---|
| Application | Python + Streamlit (turns a Python script into an interactive web app — no separate frontend framework needed) |
| Cosmology calculations | `astropy.cosmology` — purpose-built library with standard cosmological models (Planck18, WMAP9, etc.) and functions for distances, ages, and Hubble parameter |
| Numerical computing | `NumPy`, `SciPy` |
| Visualization | `Plotly` (interactive 2D charts), `Matplotlib` (static plots) |
| Deployment | GitHub Codespaces for development; Streamlit Community Cloud or a simple server for hosting |

---

## Getting Started

1. **Open**
   - Click `Code -> Codespaces -> Create codespace on main`

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```

4. Open the forwarded port shown in the Codespaces "Ports" tab to view the app.

---

## Project Structure

```
srishti-kalachakra/
├── app.py                  # Main Streamlit application (entry point)
├── requirements.txt        # Python dependencies
├── cosmology/               # Cosmology calculation modules
│   ├── distances.py         # Redshift, distance, age calculations
│   └── models.py             # Cosmological model presets
├── pages/                   # Additional Streamlit pages (calculators, sims, timeline)
└── README.md
```

---

## Roadmap

- [ ] Core distance & redshift calculators
- [ ] Friedmann equation playground with live scale-factor graph
- [ ] Cosmic timeline component
- [ ] CMB power spectrum viewer
- [ ] 3D observable universe scene (Three.js)
- [ ] N-body gravity sandbox
- [ ] Learning module content pass
- [ ] Mobile-responsive layout
- [ ] Shareable/exportable calculation results

---

## Contributing

This project is currently closed-source and maintained solely by the author. It isn't open to external contributions at this time — that may change in the future.

---

## License

**Copyright © 2026 Shriradhakrishnasharnam. All Rights Reserved.**

This source code is proprietary and confidential. Unauthorized copying, modification, distribution, or use of this code, via any medium, is strictly prohibited without express written permission from the author. This project is not currently open source.

---

*Srishti Kalachakra — building with curiosity about the universe, one equation at a time.*
