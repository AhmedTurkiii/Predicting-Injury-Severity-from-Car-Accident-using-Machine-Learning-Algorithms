import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create sample feature importance data (replace with your actual data)
feature_importance = pd.DataFrame({
    'feature': [
        'Speed at Impact',
        'Weather Conditions',
        'Road Surface',
        'Time of Day',
        'Vehicle Type',
        'Driver Age',
        'Traffic Volume',
        'Intersection Type',
        'Light Conditions',
        'Road Type'
    ],
    'importance': [0.25, 0.18, 0.15, 0.12, 0.10, 0.08, 0.05, 0.04, 0.02, 0.01]
})

# Create the visualization
plt.figure(figsize=(12, 8))
sns.set_style("whitegrid")

# Create horizontal bar plot
bars = plt.barh(feature_importance['feature'], feature_importance['importance'])

# Customize the plot
plt.title('Top 10 Predictors of Injury Severity', fontsize=16, pad=20)
plt.xlabel('Feature Importance', fontsize=12)
plt.ylabel('Features', fontsize=12)

# Add value labels on the bars
for bar in bars:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2, f'{width:.2f}', 
             ha='left', va='center', fontsize=10)

# Adjust layout
plt.tight_layout()

# Save the plot
plt.savefig('injury_predictors.png', dpi=300, bbox_inches='tight')
plt.close() 