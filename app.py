import streamlit as st
import matplotlib.pyplot as plt

from network import create_network
from demand import forecast_demand, generate_history
from hydraulics import simulate_network, leak_flow
from anomaly import detect_anomaly
from optimization import optimize_pressure
from energy import compute_energy, compute_carbon

st.set_page_config(layout="wide")

st.title("💧 Autonomous Water Optimization Platform")

# --------------------------
# Controls
# --------------------------

col1, col2, col3 = st.columns(3)

hour = col1.slider("Hour of Day", 0, 23, 3)
pump_pressure = col2.slider("Pump Pressure", 40, 100, 70)
leak_coeff = col3.slider("Leak Coefficient", 0.0, 2.0, 0.0)

# --------------------------
# Simulation
# --------------------------

G = create_network()

predicted = forecast_demand(hour)

G, total_flow = simulate_network(G, pump_pressure)

# Inject leak at node 3
pressure_node3 = G.nodes[3]['pressure']
extra_leak = leak_flow(pressure_node3, leak_coeff)
actual_flow = predicted + extra_leak

# --------------------------
# ML Detection
# --------------------------

history = generate_history()
leak_detected = detect_anomaly(history, actual_flow)

# --------------------------
# Optimization
# --------------------------

optimized_pressure = optimize_pressure(pump_pressure, leak_detected)

G_opt, total_flow_opt = simulate_network(create_network(), optimized_pressure)

energy_before = compute_energy(pump_pressure, total_flow)
energy_after = compute_energy(optimized_pressure, total_flow_opt)

carbon_before = compute_carbon(energy_before)
carbon_after = compute_carbon(energy_after)

# --------------------------
# KPIs
# --------------------------

st.subheader("System KPIs")

k1, k2, k3, k4 = st.columns(4)

k1.metric("Predicted Demand", round(predicted, 2))
k2.metric("Actual Flow", round(actual_flow, 2))
k3.metric("Leak Detected", leak_detected)
k4.metric("Optimized Pressure", round(optimized_pressure, 2))

# --------------------------
# Energy & Carbon
# --------------------------

st.subheader("Energy & Carbon Impact")

e1, e2 = st.columns(2)
e1.metric("Energy Before (kWh)", round(energy_before, 3))
e2.metric("Energy After (kWh)", round(energy_after, 3))

c1, c2 = st.columns(2)
c1.metric("Carbon Before (kg CO2)", round(carbon_before, 3))
c2.metric("Carbon After (kg CO2)", round(carbon_after, 3))

# --------------------------
# Pressure Graph
# --------------------------

st.subheader("Node Pressure Distribution")

pressures = [G.nodes[n]['pressure'] for n in G.nodes]

fig, ax = plt.subplots()
ax.bar(range(len(pressures)), pressures)
ax.set_xlabel("Node")
ax.set_ylabel("Pressure")
ax.set_title("Pressure at Each Node")

st.pyplot(fig)