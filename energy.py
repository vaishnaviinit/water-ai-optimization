carbon_factor = 0.82  # kg CO2 per kWh

def compute_energy(pump_pressure, total_flow):
    return 0.001 * pump_pressure * total_flow

def compute_carbon(energy):
    return energy * carbon_factor