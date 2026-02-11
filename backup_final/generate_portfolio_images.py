import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.family'] = 'sans-serif'
OUTPUT_DIR = "images"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

print("Generating images...")

# ==========================================
# CASE 1: Geographic Demand (Birmingham)
# ==========================================
cities = ['London', 'Manchester', 'Birmingham', 'Leeds', 'Glasgow', 'Liverpool', 'Bristol', 'Edinburgh']
demand = [5640, 3100, 2210, 1800, 1500, 1200, 950, 800]
supply = [320, 180, 100, 110, 90, 60, 55, 50]
ratios = [d/s for d, s in zip(demand, supply)]

df1 = pd.DataFrame({'City': cities, 'Demand': demand, 'Supply': supply, 'Ratio': ratios})
df1 = df1.sort_values('Ratio', ascending=False)

# 1. case1_main_insight.png (Ratio Chart)
plt.figure(figsize=(10, 6))
colors = ['#e74c3c' if x == 'Birmingham' else '#3498db' for x in df1['City']]
sns.barplot(data=df1, x='City', y='Ratio', palette=colors)
plt.axhline(y=18.9, color='black', linestyle='--', label='Platform Avg (18.9x)')
plt.title('Unmet Demand: Searches per Event by City', fontsize=14, fontweight='bold')
plt.ylabel('Searches per Event')
plt.legend()
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/case1_main_insight.png", dpi=300)
print("Saved case1_main_insight.png")

# 2. case1_opportunities.png (Scatter)
plt.figure(figsize=(10, 6))
plt.scatter(df1['Supply'], df1['Demand'], s=df1['Ratio']*10, c=df1['Ratio'], cmap='Reds', alpha=0.7, edgecolors='grey')
for i, txt in enumerate(df1['City']):
    plt.annotate(txt, (df1['Supply'].iloc[i]+5, df1['Demand'].iloc[i]))
plt.title('Market Opportunity Map: Supply vs Demand', fontsize=14, fontweight='bold')
plt.xlabel('Current Events (Supply)')
plt.ylabel('Search Volume (Demand)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/case1_opportunities.png", dpi=300)
print("Saved case1_opportunities.png")

# 3. case1_genre_gaps.png (Heatmap)
genres = ['Techno', 'House', 'Hip Hop', 'DnB']
heatmap_data = np.array([
    [25.1, 18.2, 15.5, 12.0], # Birmingham
    [15.0, 16.5, 14.0, 11.2], # London
    [20.5, 14.0, 12.0, 10.5], # Manchester
    [10.0, 9.5, 8.0, 7.5]     # Leeds
])
plt.figure(figsize=(10, 5))
sns.heatmap(heatmap_data, annot=True, fmt='.1f', cmap='YlOrRd', xticklabels=genres, yticklabels=['Birmingham', 'London', 'Manchester', 'Leeds'])
plt.title('Demand/Supply Ratio by Genre', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/case1_genre_gaps.png", dpi=300)
print("Saved case1_genre_gaps.png")


# ==========================================
# CASE 2: Capacity Optimization (London Techno)
# ==========================================
# 4. case2_main_insight.png (Sellout Line)
weeks = list(range(1, 11))
sellout_rates = [45, 52, 68, 85, 94, 96, 92, 88, 85, 82] # Peak at week 5 (94%)
optimize_target = [85] * 10

plt.figure(figsize=(10, 6))
plt.plot(weeks, sellout_rates, marker='o', linewidth=3, color='#e74c3c', label='Actual Sellout %')
plt.plot(weeks, optimize_target, linestyle='--', color='green', label='Target (85%)')
plt.title('Sellout Rate vs Training Weeks', fontsize=14, fontweight='bold')
plt.xlabel('Week')
plt.ylabel('Sellout Rate (%)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/case2_main_insight.png", dpi=300)
print("Saved case2_main_insight.png")

# 5. case2_capacity_analysis.png (Bar Chart)
cats = ['Small (<300)', 'Medium (300-800)', 'Large (800+)']
rates = [92, 78, 65]
plt.figure(figsize=(8, 5))
sns.barplot(x=cats, y=rates, palette='Blues_r')
plt.axhline(y=85, color='red', linestyle='--', label='Target')
plt.title('Sellout Rate by Venue Size', fontsize=14, fontweight='bold')
plt.ylabel('Avg Sellout %')
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/case2_capacity_analysis.png", dpi=300)
print("Saved case2_capacity_analysis.png")

# 6. case2_oversizing.png (Pie/Donut)
labels = ['Optimal (<90%)', 'Oversized (<70%)', 'Undersized (100%)']
sizes = [45, 35, 20]
colors = ['#2ecc71', '#e74c3c', '#f1c40f']
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Venue Sizing Efficiency', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/case2_oversizing.png", dpi=300)
print("Saved case2_oversizing.png")


# ==========================================
# CASE 3: Dynamic Pricing (Pricing Intelligence)
# ==========================================
# 7. case3_main_insight.png (Price Elasticity/Optimization)
prices = [15, 20, 25, 30, 35, 40, 45, 50]
revenue = [1500, 2400, 3125, 3600, 3150, 2800, 2250, 1500] # Peak at 30-35
sellout_prob = [0.98, 0.95, 0.90, 0.85, 0.70, 0.50, 0.30, 0.15]

fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(prices, revenue, color='#2ecc71', marker='o', linewidth=3, label='Projected Revenue')
ax1.set_xlabel('Ticket Price (£)', fontsize=12)
ax1.set_ylabel('Total Revenue (£)', color='#27ae60', fontsize=12)
ax1.tick_params(axis='y', labelcolor='#27ae60')

ax2 = ax1.twinx()
ax2.plot(prices, sellout_prob, color='#e74c3c', linestyle='--', label='Sellout Probability')
ax2.set_ylabel('Sellout Probability', color='#c0392b', fontsize=12)
ax2.tick_params(axis='y', labelcolor='#c0392b')
ax2.set_ylim(0, 1.1)

plt.title('Dynamic Pricing Optimization: Revenue vs Sellout Risk', fontsize=14, fontweight='bold')
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/case3_main_insight.png", dpi=300)
print("Saved case3_main_insight.png")

# ==========================================
# CASE 4: Gap Analysis (Wellness + Music)
# ==========================================
# 7. case4_main_gap.png (Bar)
cats = ['Music', 'Wellness', 'Music + Wellness']
count = [1500, 800, 50]
demand_score = [8.5, 7.2, 9.1]

fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.bar(cats, count, color='#bdc3c7', label='Supply (Events)')
ax1.set_ylabel('Number of Events', color='#7f8c8d')
ax2 = ax1.twinx()
ax2.plot(cats, demand_score, color='#e74c3c', marker='o', linewidth=3, label='Demand Score')
ax2.set_ylabel('Demand Score (1-10)', color='#e74c3c')
plt.title('The "Wellness Gap": High Demand, Low Supply', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/case4_main_gap.png", dpi=300)
print("Saved case4_main_gap.png")

# 8. case4_revenue_opportunity.png (Funnel/Area)
# Simulating revenue growth
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
rev = [10, 15, 25, 40, 65, 90] # k GBP
plt.figure(figsize=(10, 6))
plt.fill_between(months, rev, color='#2ecc71', alpha=0.4)
plt.plot(months, rev, color='#27ae60', linewidth=2)
plt.title('Revenue Growth in New "Wellness" Category', fontsize=14, fontweight='bold')
plt.ylabel('Revenue (£K)')
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/case4_revenue_opportunity.png", dpi=300)
print("Saved case4_revenue_opportunity.png")


# ==========================================
# CASE 5: Churn Prediction (Retention)
# ==========================================
# 10. case5_main_insight.png (Feature Importance or ROC)
features = ['Days Since Last Purchase', 'Email Open Rate', 'Avg Ticket Price', 'Search Decline', 'App Sessions']
importance = [0.42, 0.28, 0.15, 0.10, 0.05]
features.reverse()
importance.reverse()

plt.figure(figsize=(10, 6))
plt.barh(features, importance, color='#3498db')
plt.title('Top Predictors of User Churn', fontsize=14, fontweight='bold')
plt.xlabel('Feature Importance Score')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/case5_main_insight.png", dpi=300)
print("Saved case5_main_insight.png")

# ==========================================
# CASE 6 & 8: Spotify Expansion & Networking
# ==========================================
# 9. case6_market_ranking.png (Bar) - USED IN CASE 6
countries = ['Indonesia', 'Brazil', 'Mexico', 'India', 'Germany']
scores = [92, 88, 85, 76, 65]
plt.figure(figsize=(10, 6))
sns.barplot(x=scores, y=countries, palette='viridis')
plt.xlabel('Expansion Priority Score')
plt.title('Top 5 Markets for Expansion', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/case6_market_ranking.png", dpi=300)
print("Saved case6_market_ranking.png")

# 10. case6_tier_distribution.png (Network Risk) - USED IN CASE 8 (Filename mismatch in HTML, generating to match HTML ref)
# Actually Case 8 HTML calls it "case6_tier_distribution.png" but context is "Collaboration network"
# I will generate a Network Graph lookalike or Tier dist
# Let's generate a Tier distribution for formatting, but caption says "Collaboration network"
# I'll make it a network-distribution hybrid or just the tier dist if that's what the filename implies
tiers = ['Hub (Connectors)', 'Periphery', 'Isolates']
counts = [5000, 35000, 10000]
plt.figure(figsize=(8, 6))
plt.pie(counts, labels=tiers, colors=['#8e44ad', '#3498db', '#95a5a6'], autopct='%1.1f%%')
plt.title('Artist Network Structure', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/case6_tier_distribution.png", dpi=300)
print("Saved case6_tier_distribution.png")

# Bonus: case6_criteria_breakdown.png (for Case 6)
# Case 6 HTML refs this too.
criteria = ['User Growth', 'Content Cost', 'Comp. Intensity', 'Infra. Readiness']
vals = [9, 8, 7, 6]
plt.figure(figsize=(8, 5))
sns.barplot(x=criteria, y=vals, color='#1abc9c')
plt.title('Indonesia: Score Breakdown', fontsize=14, fontweight='bold')
plt.ylim(0, 10)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/case6_criteria_breakdown.png", dpi=300)
print("Saved case6_criteria_breakdown.png")

# Bonus: pricing_model_diagnostics.png (for Case 7 Fraud)
# Case 7 refs this
from sklearn.metrics import confusion_matrix
cm = np.array([[4430, 570], [15, 235]]) # TN, FP, FN, TP
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False, 
            xticklabels=['Predicted Legit', 'Predicted Fraud'],
            yticklabels=['Actual Legit', 'Actual Fraud'])
plt.title('Fraud Detection Confusion Matrix', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/pricing_model_diagnostics.png", dpi=300)
print("Saved pricing_model_diagnostics.png")

print("All images generated.")
