import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn import metrics
from zqscore import ZQ_score

# 在高维空间中产生一个有核的类球状实验数据
from sklearn.datasets import make_gaussian_quantiles
# 在四维空间中以原点为中心产生高斯分布的数据，该数据从中心向外分为9层
X1, y1 = make_gaussian_quantiles(n_samples=10000, n_features=4, n_classes=9, mean=[0,0,0,0],cov=5)
print(X1)
# 只保留最内的类圆形和倒数第二外层
for i in range(len(y1)-1, -1, -1):
    if y1[i]==1 or y1[i]==2 or y1[i]==3 or y1[i]==4 or y1[i]==5 or y1[i]==6 or y1[i]==8:
        X1 = np.delete(X1, i, axis=0)
        y1 = np.delete(y1, i, axis=0)
print(len(y1))

# 降维后，在二维平面上画出图形
pca = PCA(n_components=2).fit(X1)
X1_pca = pca.transform(X1)
plt.axes(aspect='equal')
plt.scatter(X1_pca[:, 0], X1_pca[:, 1], marker='+', c=y1)
plt.show()

clus = KMeans(n_clusters=2, random_state=0).fit(X1)
plt.axes(aspect='equal')
plt.scatter(X1_pca[:, 0], X1_pca[:, 1], marker='+', c=clus.labels_)
plt.show()
print("SC:\t"+str(metrics.silhouette_score(X1, clus.labels_, metric='euclidean')))
print("DBI:\t"+str(metrics.davies_bouldin_score(X1, clus.labels_)))
print("CH:\t"+str(metrics.calinski_harabasz_score(X1, clus.labels_)))
print("ZQ:\t"+str(ZQ_score(X1, clus.labels_)))

clus = DBSCAN(eps=2, min_samples=4).fit(X1)
plt.axes(aspect='equal')
plt.scatter(X1_pca[:, 0], X1_pca[:, 1], marker='+', c=clus.labels_)
plt.show()
print("SC:\t"+str(metrics.silhouette_score(X1, clus.labels_, metric='euclidean')))
print("DBI:\t"+str(metrics.davies_bouldin_score(X1, clus.labels_)))
print("CH:\t"+str(metrics.calinski_harabasz_score(X1, clus.labels_)))
print("ZQ:\t"+str(ZQ_score(X1, clus.labels_)))

gm = GaussianMixture(n_components=2, random_state=0).fit(X1)
y1_pred = gm.predict(X1)
plt.axes(aspect='equal')
plt.scatter(X1_pca[:, 0], X1_pca[:, 1], marker='+', c=y1_pred)
plt.show()
print("SC:\t"+str(metrics.silhouette_score(X1, y1_pred, metric='euclidean')))
print("DBI:\t"+str(metrics.davies_bouldin_score(X1, y1_pred)))
print("CH:\t"+str(metrics.calinski_harabasz_score(X1, y1_pred)))
print("ZQ:\t"+str(ZQ_score(X1, y1_pred)))