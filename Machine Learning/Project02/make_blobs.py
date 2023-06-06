import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn import metrics
from zqscore import ZQ_score

from sklearn.datasets import make_blobs
X3_1, y3_1 = make_blobs(n_samples=300, n_features=2, centers=[[0,0]], cluster_std=[1.2], random_state=15)
X3_2, y3_2 = make_blobs(n_samples=700, n_features=2, centers=[[5,5]], cluster_std=[1.8], random_state=15)
X3 = np.vstack((X3_1, X3_2))
plt.axes(aspect='equal')
plt.scatter(X3_1[:, 0], X3_1[:, 1], marker='o', color='r')
plt.scatter(X3_2[:, 0], X3_2[:, 1], marker='+', color='b')
plt.show()

clus = KMeans(n_clusters=2, random_state=0).fit(X3)
plt.axes(aspect='equal')
plt.scatter(X3[:, 0], X3[:, 1], marker='+', c=clus.labels_)
plt.show()
print("SC:\t"+str(metrics.silhouette_score(X3, clus.labels_, metric='euclidean')))
print("DBI:\t"+str(metrics.davies_bouldin_score(X3, clus.labels_)))
print("CH:\t"+str(metrics.calinski_harabasz_score(X3, clus.labels_)))
print("ZQ:\t"+str(ZQ_score(X3, clus.labels_)))

clus = DBSCAN(eps=1, min_samples=25).fit(X3)
plt.axes(aspect='equal')
plt.scatter(X3[:, 0], X3[:, 1], marker='+', c=clus.labels_)
plt.show()
print("SC:\t"+str(metrics.silhouette_score(X3, clus.labels_, metric='euclidean')))
print("DBI:\t"+str(metrics.davies_bouldin_score(X3, clus.labels_)))
print("CH:\t"+str(metrics.calinski_harabasz_score(X3, clus.labels_)))
print("ZQ:\t"+str(ZQ_score(X3, clus.labels_)))
#
gm = GaussianMixture(n_components=2, random_state=0).fit(X3)
y3_pred = gm.predict(X3)
plt.axes(aspect='equal')
plt.scatter(X3[:, 0], X3[:, 1], marker='+', c=y3_pred)
plt.show()
print("SC:\t"+str(metrics.silhouette_score(X3, y3_pred, metric='euclidean')))
print("DBI:\t"+str(metrics.davies_bouldin_score(X3, y3_pred)))
print("CH:\t"+str(metrics.calinski_harabasz_score(X3, y3_pred)))
print("ZQ:\t"+str(ZQ_score(X3, y3_pred)))