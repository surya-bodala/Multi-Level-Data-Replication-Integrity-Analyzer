📊 Smart City Risk Analysis System
📌 Overview

This project simulates a Smart City Monitoring System that analyzes different zones based on:

Traffic levels 🚗
Air quality 🌫️
Energy consumption ⚡

It classifies zones, calculates risk scores, detects patterns, and provides a final city-wide decision.

⚙️ Features
🔢 Random data generation for multiple zones
🧠 Risk classification using custom logic
📊 Risk score calculation with weighted factors
📈 Data analysis using NumPy and Pandas
🔍 Pattern detection (multi-risk zones, clusters, stability)
🏙️ Final city status evaluation
🗂️ Data Fields

Each zone contains:

zone → Zone number
traffic → Traffic level (0–100)
air_quality → AQI (0–300)
energy → Energy usage (0–500)
🧮 Risk Classification Logic
High Risk → Air quality > 200 OR traffic > 80
Energy Critical → Energy > 400
Safe Zone → Traffic < 30 AND air quality < 100
Moderate → All other cases
📐 Risk Score Formula

The system calculates a weighted risk score:

Risk Score = (0.3 × Traffic) + (0.4 × Air Quality) + (0.3 × Energy)
🔍 Pattern Detection

The system identifies:

Multi-factor Risk Zones → High risk score + increasing air quality
Stability → Based on variance of traffic
Clusters → Consecutive high-risk zones
📊 Outputs

The program prints:

Full city dataset
Mean values of traffic, air quality, and energy
Top 3 highest risk zones
Risk statistics (max, mean, min)
Pattern detection results
Final decision on city condition
🚦 Final Decision Logic

Based on average risk score:

< 100 → City Stable ✅
100–150 → Moderate Risk ⚠️
150–200 → High Alert 🚨
> 200 → Critical Emergency 🔥
🧑‍💻 Requirements

Install dependencies before running:

pip install pandas numpy
▶️ How to Run
python your_script_name.py
🌍 Smart City Concept

A smart city focuses on:

🌱 Reducing pollution
⚡ Efficient energy management
📡 Data-driven decision making
🌏 Sustainable urban development
