import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.manifold import TSNE
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from matplotlib import offsetbox

mnist = load_digits()
x, x_test, y, y_test = train_test_split(
    mnist.data, mnist.target, test_size=0.25, random_state=40)

acc = []
sample = []


def plot_prediction(images, labels, prediction, text, index, num=10):
    fig = plt.figure(figsize=(7, 7))
    fig.suptitle(text)
    if num > 16:
        num = 16
    for i in range(0, num):
        ax = plt.subplot(4, 4, i + 1)

        ax.imshow(np.reshape(images[index], (8, 8)),
                  cmap=plt.cm.gray_r, interpolation='nearest')

        title = "label=" + str(labels[index])  # 构建图片上要显示的title
        if len(prediction) > 0:
            title += ", predict=" + str(prediction[index])

        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        index += 1
    plt.show()


# Scale and visualize the embedding vectors


def plot_embedding(test_x, test_y, title=None):
    tsne = TSNE(n_components=2, init='pca', random_state=0)
    X = tsne.fit_transform(test_x)
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    X = (X - x_min) / (x_max - x_min)  # 正则化

    plt.figure()
    ax = plt.subplot(111)
    for i in range(X.shape[0]):
        plt.text(X[i, 0], X[i, 1], str(test_y[i]),
                 color=plt.cm.Set1(test_y[i] / 10.),
                 fontdict={'weight': 'bold', 'size': 9})

    if hasattr(offsetbox, 'AnnotationBbox'):
        # only print thumbnails with matplotlib > 1.0
        shown_images = np.array([[1., 1.]])  # just something big
        for i in range(X.shape[0]):
            dist = np.sum((X[i] - shown_images) ** 2, 1)
            if np.min(dist) < 4e-3:
                # don't show points that are too close
                continue
            shown_images = np.r_[shown_images, [X[i]]]
            imagebox = offsetbox.AnnotationBbox(
                offsetbox.OffsetImage(test_x[i].reshape(
                    (8, 8)), cmap=plt.cm.gray_r),
                X[i]
            )
            ax.add_artist(imagebox)

    if title is not None:
        plt.title(title)

    plt.xticks([])
    plt.yticks([])


def plot_embedding_3d(test_x, test_y, title=None):
    tsne = TSNE(n_components=3, init='pca', random_state=0)
    X = tsne.fit_transform(test_x)
    # 坐标缩放到[0,1]区间
    x_min, x_max = np.min(X, axis=0), np.max(X, axis=0)
    X = (X - x_min) / (x_max - x_min)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    for i in range(X.shape[0]):
        ax.text(X[i, 0], X[i, 1], X[i, 2], str(test_y[i]),
                color=plt.cm.Set1(test_y[i] / 10.),
                fontdict={'weight': 'bold', 'size': 9})
    if title is not None:
        plt.title(title)

    plt.xticks([])
    plt.yticks([])


mm = preprocessing.MinMaxScaler()
train_x = mm.fit_transform(x)
test_x = mm.transform(x_test)

# 多项式朴素贝叶斯
model = MultinomialNB()
model.fit(train_x, y)
z = model.predict(test_x)
sample.append(model)
acc.append(accuracy_score(z, y_test))

plot_embedding(x_test, z, title="MultinomialNB")
plot_embedding_3d(x_test, z, title="MultinomialNB")
plot_prediction(x_test, y_test, z, "MultinomialNB", 10, 16)

model = LogisticRegression(random_state=0, max_iter=3000)
model.fit(x, y)
z = model.predict(x_test)
sample.append(model)
acc.append(accuracy_score(z, y_test))

plot_embedding(x_test, z, title="SoftMax")
plot_embedding_3d(x_test, z, title="SoftMax")
plot_prediction(x_test, y_test, z, "SoftMax", 10, 16)

ss = preprocessing.StandardScaler()
train_x = ss.fit_transform(x)
test_x = ss.transform(x_test)

model = KNeighborsClassifier(
    n_neighbors=5, weights='uniform', algorithm='auto', leaf_size=30)
model.fit(train_x, y)
z = model.predict(test_x)
sample.append(model)
acc.append(accuracy_score(z, y_test))

plot_embedding(x_test, z, title="KNN")
plot_embedding_3d(x_test, z, title="KNN")
plot_prediction(x_test, y_test, z, "KNN", 10, 16)

model = MLPClassifier(hidden_layer_sizes=(100,),
                      activation='logistic', solver='adam',
                      learning_rate_init=0.0001, max_iter=2000)
model.fit(x, y)
z = model.predict(x_test)
sample.append(model)
acc.append(accuracy_score(z, y_test))

plot_embedding(x_test, z, title="MLP")
plot_embedding_3d(x_test, z, title="MLP")
plot_prediction(x_test, y_test, z, "MLP", 10, 16)

model = SVC()
model.fit(x, y)
z = model.predict(x_test)
sample.append(model)
acc.append(accuracy_score(z, y_test))

plot_embedding(x_test, z, title="SVM")
plot_embedding_3d(x_test, z, title="SVM")
plot_prediction(x_test, y_test, z, "SVM", 10, 16)

model = DecisionTreeClassifier()
model.fit(x, y)
z = model.predict(x_test)
sample.append(model)
acc.append(accuracy_score(z, y_test))

plot_embedding(x_test, z, title="DecisionTree")
plot_embedding_3d(x_test, z, title="DecisionTree")
plot_prediction(x_test, y_test, z, "DecisionTree", 10, 16)

plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei']
name = ['Bayes', 'SoftMax', 'KNN', 'MLP', 'SVC', "DecisionTree"]
theta = np.linspace(0, 2 * np.pi, len(name), endpoint=False)
theta = np.concatenate((theta, [theta[0]]))
acc = np.concatenate((acc, [acc[0]]))

ax = plt.subplot(111, projection='polar')  # 构建图例
ax.plot(theta, acc, 'm-', lw=1, alpha=0.75)  # 绘图
ax.fill(theta, acc, 'b', alpha=0.1)  # 填充
ax.set_thetagrids(theta[0:6] * 180 / np.pi, name)  # 替换标签
ax.set_ylim(0.7, 1.0)  # 设置极轴的区间
ax.set_theta_zero_location('N')  # 设置极轴方向
for a, b in zip(theta, acc):
    ax.text(a, b + 0.02, '%.5f' % b, ha='center', va='center', fontsize=8, color='r')
ax.set_title('不同分类方法准确率的比较', fontsize=12)
plt.show()