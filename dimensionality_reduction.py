import numpy as np
import matplotlib.pyplot as plt
import umap

# Generate sample high-dimensional data
X = np.random.rand(200, 50)  # 200 samples with 50 features each

# Apply UMAP to reduce dimensions to 2
reducer = umap.UMAP(n_components=2, random_state=42)
X_reduced = reducer.fit_transform(X)

# Plotting the results
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c='blue', alpha=0.6)
plt.title("UMAP Dimensionality Reduction")
plt.xlabel("Component 1")
plt.ylabel("Component 2")
plt.show()
