import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Sample data: career scores for two roles
data = {
    'role': ['Data Analyst'] * 50 + ['Software Developer'] * 50,
    'score': np.concatenate([np.random.normal(70, 10, 50), np.random.normal(80, 10, 50)])
}
df = pd.DataFrame(data)

# Box plot of scores
plt.figure(figsize=(8,6))
sns.boxplot(x='role', y='score', data=df)
plt.title("Career Score Distribution")
plt.show()

# Histogram of scores
plt.figure(figsize=(8,6))
sns.histplot(df['score'], kde=True, color='green')
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()
