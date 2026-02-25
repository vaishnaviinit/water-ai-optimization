from sklearn.ensemble import IsolationForest

def detect_anomaly(history, actual_value):
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(history)

    prediction = model.predict([[actual_value]])

    if prediction[0] == -1:
        return True
    return False