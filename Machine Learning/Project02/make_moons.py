import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn import metrics
from zqscore import ZQ_score

from sklearn.datasets import make_moons
noisy_moons = make_moons(n_samples=1000, noise=.05, random_state=15)
X4 = noisy_moons[0]
plt.axes(aspect='equal')
plt.scatter(X4[:, 0], X4[:, 1], marker='o', c='g')
plt.show()

# clus = KMeans(n_clusters=2, random_state=0).fit(X4)
# plt.axes(aspect='equal')
# plt.scatter(X4[:, 0], X4[:, 1], marker='o', c=clus.labels_)
# plt.show()
# print("SC:\t"+str(metrics.silhouette_score(X4, clus.labels_, metric='euclidean')))
# print("DBI:\t"+str(metrics.davies_bouldin_score(X4, clus.labels_)))
# print("CH:\t"+str(metrics.calinski_harabasz_score(X4, clus.labels_)))
# print("ZQ:\t"+str(ZQ_score(X4, clus.labels_)))

# clus = DBSCAN(eps=0.1, min_samples=3).fit(X4)
# plt.axes(aspect='equal')
# plt.scatter(X4[:, 0], X4[:, 1], marker='o', c=clus.labels_)
# plt.show()
# print("SC:\t"+str(metrics.silhouette_score(X4, clus.labels_, metric='euclidean')))
# print("DBI:\t"+str(metrics.davies_bouldin_score(X4, clus.labels_)))
# print("CH:\t"+str(metrics.calinski_harabasz_score(X4, clus.labels_)))
# print("ZQ:\t"+str(ZQ_score(X4, clus.labels_)))
#
gm = GaussianMixture(n_components=2, random_state=0).fit(X4)
y2_pred = gm.predict(X4)
plt.axes(aspect='equal')
plt.scatter(X4[:, 0], X4[:, 1], marker='o', c=y2_pred)
plt.show()
print("SC:\t"+str(metrics.silhouette_score(X4, y2_pred, metric='euclidean')))
print("DBI:\t"+str(metrics.davies_bouldin_score(X4, y2_pred)))
print("CH:\t"+str(metrics.calinski_harabasz_score(X4, y2_pred)))
print("ZQ:\t"+str(ZQ_score(X4, y2_pred)))