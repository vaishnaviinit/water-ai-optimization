import numpy as np

def forecast_demand(hour):
    return 50 + 30 * np.sin((hour / 24) * 2 * np.pi)

def generate_history():
    history = []
    for h in range(24):
        history.append(forecast_demand(h))
    return np.array(history).reshape(-1, 1)