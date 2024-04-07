# -*- coding: utf-8 -*-

import numpy as np
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

####
# "manually"
####

# load the dataset and get familiar with the data
iris = load_iris()
data = iris.data

# compute the mean and center the data
mu = np.mean(data, axis=0)
data -= mu

# compute covariance matrix
cov = np.cov(data, rowvar=False)

# compute eigenvectors and eigenvalues
eigenvalues, eigenvectors = np.linalg.eig(cov)

# multiply transposed eigenvectors by zero mean matrix transposed
newdata = np.dot(eigenvectors.T, data.T)

# first 6 final scores
first_6_scores = newdata[:, :6].T
print(first_6_scores)



#### 
# using PCA from sklearn
####

pca = PCA()
pc = pca.fit_transform(iris.data)

# variance
explained_variance = pca.explained_variance_ratio_

# eigenvectors (loadings)
loadings = pca.components_

# first 6 final scores
pca_first_6_scores = pc[:6, :]

print(np.isclose(pca_first_6_scores, first_6_scores))
print(np.isclose(pca_first_6_scores, -first_6_scores))

# plot projection on two principal components
plt.figure()
plt.scatter(pc[:, 0], pc[:, 1], c=iris.target, cmap='viridis')
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA: Projection on Two Principal Components")
plt.colorbar(label="Target Class")
plt.show()