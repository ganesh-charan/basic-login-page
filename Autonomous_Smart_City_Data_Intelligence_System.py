import random
import math
import numpy as np
import pandas as pd

def generate_data(n=6):
    data = []
    for i in range(1, n+1):
        data.append({
            "zone": i,
            "traffic": random.randint(0, 100),
            "air_quality": random.randint(0, 300),
            "energy": random.randint(0, 500)
        })
    data[0] = {"zone": 1, "traffic": 0, "air_quality": 50, "energy": 100}
    data[1] = {"zone": 2, "traffic": 90, "air_quality": 300, "energy": 450}
    data[2] = {"zone": 3, "traffic": 100, "air_quality": 250, "energy": 500}
    return data

def classify_zone(r):
    if r["air_quality"] > 200 or r["traffic"] > 80:
        return "High Risk"
    elif r["energy"] > 400:
        return "Energy Critical"
    elif r["traffic"] < 30 and r["air_quality"] < 100:
        return "Safe Zone"
    else:
        return "Moderate"

def calculate_risk(r):
    return r["traffic"]*0.4 + r["air_quality"]*0.4 + r["energy"]*0.2

def custom_sort(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i]["traffic"] < data[j]["traffic"]:
                data[i], data[j] = data[j], data[i]
    return data

def detect_patterns(df):
    patterns = {}
    threshold = df["risk_score"].mean()
    patterns["high_risk_zones"] = df[(df["risk_score"] > threshold) & (df["air_quality"].diff() > 0)]["zone"].tolist()
    patterns["stability"] = "Stable Traffic" if df["traffic"].var() < 200 else "Unstable Traffic"
    clusters = []
    temp = []
    for i in range(len(df)):
        if df.loc[i, "risk_score"] > threshold:
            temp.append(df.loc[i, "zone"])
        else:
            if len(temp) >= 2:
                clusters.append(temp)
            temp = []
    patterns["clusters"] = clusters
    return patterns

def final_decision(avg):
    if avg < 100:
        return "City Stable"
    elif avg < 200:
        return "Moderate Risk"
    elif avg < 300:
        return "High Alert"
    else:
        return "Critical Emergency"

data = generate_data()
random.shuffle(data)

for r in data:
    r["category"] = classify_zone(r)
    r["risk_score"] = calculate_risk(r)
    r["adjusted_risk"] = math.sqrt(r["risk_score"])

df = pd.DataFrame(data)

np_array = df[["traffic", "air_quality", "energy"]].values
means = np.mean(np_array, axis=0)

sorted_data = custom_sort(data.copy())
top3 = sorted_data[:3]

max_risk = df["risk_score"].max()
avg_risk = df["risk_score"].mean()
min_risk = df["risk_score"].min()
risk_tuple = (max_risk, avg_risk, min_risk)

patterns = detect_patterns(df)
decision = final_decision(avg_risk)

unique_categories = set(df["category"])

print(df)
print(means)
print(top3)
print(risk_tuple)
print(patterns)
print(unique_categories)
print(decision)