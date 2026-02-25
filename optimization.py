def optimize_pressure(current_pressure, leak_detected):
    if leak_detected:
        return current_pressure * 0.85
    return current_pressure