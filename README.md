
# Autonomous Water Optimization Platform

## Overview

The Autonomous Water Optimization Platform is a simulation-based intelligent control system designed to detect water distribution anomalies and optimize pump pressure to reduce energy consumption and carbon emissions.

The system models a simplified water distribution network, applies machine learning-based anomaly detection to identify abnormal flow behavior (potential leaks), and dynamically adjusts pump pressure to minimize environmental impact.

This project demonstrates the integration of hydraulic modeling, data-driven anomaly detection, and sustainability-focused optimization in a unified software prototype.

---

## Problem Statement

Urban water utilities lose a significant percentage of treated water due to:

* Micro-leaks in aging infrastructure
* Excessive pressure in distribution systems
* Pump mismanagement
* Lack of real-time optimization

Water loss not only wastes water but also increases energy consumption, since pumping accounts for a major portion of operational costs. In regions where electricity generation is carbon-intensive, this directly increases CO₂ emissions.

This platform addresses:

* Leak detection using anomaly detection
* Pressure optimization for leak mitigation
* Energy and carbon impact estimation

---

## System Architecture

The platform follows a modular architecture:

Sensors / Simulated Data
→ Hydraulic Model
→ Anomaly Detection (Isolation Forest)
→ Pressure Optimization
→ Energy & Carbon Calculation
→ Streamlit Dashboard

---

## Core Components

### 1. Hydraulic Simulation

A simplified graph-based water network model is implemented using NetworkX.
Pressure at nodes is computed as a function of pump pressure and distributed head loss.

Leak discharge is modeled using:

Q_leak = k × sqrt(P)

Where:

* k = leak coefficient
* P = pressure at the leak node

---

### 2. Demand Modeling

Water demand is modeled using a sinusoidal time-based function:

Demand = 50 + 30 sin(2πh/24)

This simulates daily variation in water consumption.

---

### 3. Anomaly Detection

The system uses Isolation Forest from scikit-learn to detect abnormal deviations between predicted demand and actual flow.

* The model is trained on normal demand history.
* Significant deviations are classified as anomalies.
* Detected anomalies trigger pressure optimization.

---

### 4. Pressure Optimization

When a leak is detected:

Pump pressure is reduced by a fixed proportional factor to minimize excess flow and reduce system stress.

This demonstrates closed-loop intelligent control logic.

---

### 5. Energy and Carbon Estimation

Energy consumption is approximated using:

Energy ∝ Pump Pressure × Total Flow

Carbon emissions are calculated using India's average grid emission factor:

CO₂ = Energy × 0.82 kg per kWh

This highlights the water–energy–carbon nexus.

---

## Features

* Graph-based hydraulic network model
* Leak simulation at selected node
* Machine learning anomaly detection
* Automatic pressure optimization
* Energy consumption estimation
* Carbon footprint calculation
* Interactive Streamlit dashboard

---

## Technology Stack

* Python 3
* Streamlit
* NetworkX
* NumPy
* Scikit-learn
* Matplotlib

---

## How to Run

1. Clone the repository:

   git clone [https://github.com/yourusername/water-ai-optimization.git](https://github.com/yourusername/water-ai-optimization.git)

2. Navigate into the project folder:

   cd water-ai-optimization

3. Install dependencies:

   pip install -r requirements.txt

4. Run the application:

   streamlit run app.py

The dashboard will open at:

[http://localhost:8501](http://localhost:8501)

---

## Use Case

This prototype can be extended to integrate with real SCADA systems and IoT-based sensor networks in:

* Industrial campuses
* Smart buildings
* Gated communities
* Urban water utilities

In a real deployment scenario, simulated inputs would be replaced with live sensor feeds for flow, pressure, and pump energy data.

---

## Limitations

* Uses simplified hydraulic equations
* Does not model full nonlinear head-loss equations
* Leak localization is fixed in current version
* Uses synthetic demand data

This project is a functional MVP demonstrating architectural feasibility rather than a production-ready hydraulic solver.

---

## Future Improvements

* Integration with EPANET digital twin models
* Multi-node leak localization
* Reinforcement learning-based pump control
* Real-time SCADA integration
* Deployment to cloud infrastructure
* Advanced energy modeling

---

## Author

Vaishnavi Chaudhary
Autonomous Water Optimization Research Prototype
