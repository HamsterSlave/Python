import numpy as np
import matplotlib.pyplot as plt
def L2(vecXi,vecXj):
    return np.sqrt(np.sum(np.power(vecXi-vecXj,2)))
def kMeans(S,k,distMeas=L2):
    m = np.shape(S)[0]
    sampleTag = np.zeros(m)

    n = np.shape(S)[1]
    clusterCents = np.mat(np.zeros((k, n)))
    for j in range(n):
        minJ = min(S[:,j])
        rangeJ = float(max(S[:,j]) - minJ)
        clusterCents[:,j] = np.mat(minJ + rangeJ * np.random.rand(k,1))

    sampleTagChanged = True
    SSE = 0.0
    while sampleTagChanged:
        sampleTagChanged = False
        SSE = 0.0

        for i in range(m):
            minD = np.inf
            minIndex = -1
            for j in range(k):
                d = distMeas(clusterCents[j,:],S[i,:])
                if d < minD:
                    minD = d
                    minIndex = j
            if sampleTag[i] != minIndex:
                sampleTagChanged = True
            sampleTag[i] = minIndex
            SSE += minD ** 2
            # print(clusterCents)
            # plt.scatter(S[ :,0], S[:,1],c = sampleTag, linewidths = np.power( sampleTag + 0.5, 2))
            # #plt.show()
        print(SSE)

        for i in range(k):
            ClustI = S[np.nonzero(sampleTag[:] == i)[0]]
            clusterCents[i, :] = np.mean(ClustI, axis=0)
    return clusterCents,sampleTag, SSE
if __name__ == '__main__':
    samples = np.loadtxt("kmeansSamples.txt")
    clusterCents, sampleTag, SSE = kMeans(samples,3)
    plt.scatter(samples[:,0], samples[:,1], c=sampleTag,linewidths=np.power(sampleTag+0.5,2))
    plt.show()
    print(clusterCents)
    print(SSE)