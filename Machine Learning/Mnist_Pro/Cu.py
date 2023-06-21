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
from PIL import Image, ImageQt
from layout import Ui_MainWindow
from paintboard import PaintBoard
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap, QColor, QIcon
from PyQt5.QtCore import QSize
import sys

# 1797个8*8的数据集
mnist = load_digits()
# random_state设置相同随机种子的值，可复现相同结果
# 将数据集划分1347个训练集和450个测试集
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

        title = "label=" + str(labels[index])   # 构建图片上要显示的title
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

def compare(acc):
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
        ax.text(a, b+0.02, '%.5f' % b, ha='center',
                va='center', fontsize=8, color='r')
    ax.set_title('不同分类方法准确率的比较', fontsize=12)
    plt.show()

# 实例化一个MinMaxScaler对象
mm = preprocessing.MinMaxScaler()
# 对训练集和测试集进行归一化（0,1）之间
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

# 逻辑回归分类
model = LogisticRegression(random_state=0, max_iter=3000)
model.fit(x, y)
z = model.predict(x_test)
sample.append(model)
acc.append(accuracy_score(z, y_test))

plot_embedding(x_test, z, title="SoftMax")
plot_embedding_3d(x_test, z, title="SoftMax")
plot_prediction(x_test, y_test, z, "SoftMax", 10, 16)

# 标准化，均值为0，方差为1
ss = preprocessing.StandardScaler()
train_x = ss.fit_transform(x)
test_x = ss.transform(x_test)

#  K-近邻分类器，指定邻居的数量为5个，指定所有邻居的权重相同，自动选择最优的算法，指定叶子节点的大小为30
model = KNeighborsClassifier(
    n_neighbors=5, weights='uniform', algorithm='auto', leaf_size=30)
model.fit(train_x, y)
z = model.predict(test_x)
sample.append(model)
acc.append(accuracy_score(z, y_test))

plot_embedding(x_test, z, title="KNN")
plot_embedding_3d(x_test, z, title="KNN")
plot_prediction(x_test, y_test, z, "KNN", 10, 16)

# 多层感知器分类器，100个神经元的隐藏层，激活函数为logistic，优化器为adam，学习率为0.0001，最大迭代次数为2000
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

# 支持向量机，设置参数probability=True以便获取预测概率
model = SVC(probability=True)
model.fit(x, y)
z = model.predict(x_test)
sample.append(model)
acc.append(accuracy_score(z, y_test))

plot_embedding(x_test, z, title="SVM")
plot_embedding_3d(x_test, z, title="SVM")
plot_prediction(x_test, y_test, z, "SVM", 10, 16)

# 决策树分类器
model = DecisionTreeClassifier()
model.fit(x, y)
z = model.predict(x_test)
sample.append(model)
acc.append(accuracy_score(z, y_test))

plot_embedding(x_test, z, title="DecisionTree")
plot_embedding_3d(x_test, z, title="DecisionTree")
plot_prediction(x_test, y_test, z, "DecisionTree", 10, 16)

compare(acc)


## GUI类
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
    
        # 初始化参数
        self.mode = 0
        self.result = [0, 0]

        # 初始化UI
        self.setupUi(self)
        self.center()

        # 初始化画板
        self.paintBoard = PaintBoard(self, Size = QSize(224, 224), Fill = QColor(0,0,0,0)) ## 设成255随机抽图像时啥都看不见
        self.paintBoard.setPenColor(QColor(0,0,0,0))
        self.dArea_Layout.addWidget(self.paintBoard)

        self.clearDataArea()

    # 窗口居中
    def center(self):
        # 获得窗口
        framePos = self.frameGeometry()
        # 获得屏幕中心点
        scPos = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        framePos.moveCenter(scPos)
        self.move(framePos.topLeft())
    
    
    # 窗口关闭事件
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()   
    
    # 清除数据待输入区
    def clearDataArea(self):
        self.paintBoard.Clear()
        self.lbDataArea.clear()
        self.lbResult.clear()
        self.lbCofidence.clear()
        self.result = [0, 0]

    """
    回调函数
    """
    # 模式下拉列表回调
    def cbBox_Mode_Callback(self, text):
        if text == '0：Bayes':
            self.mode = 0
            #self.clearDataArea()
            self.pbtGetMnist.setEnabled(True)

            self.paintBoard.setBoardFill(QColor(0,0,0,0))
            self.paintBoard.setPenColor(QColor(0,0,0,0))

        elif text == '1：Softmax':
            self.mode = 1
            #self.clearDataArea()
            self.pbtGetMnist.setEnabled(True)

            self.paintBoard.setBoardFill(QColor(0,0,0,0))
            self.paintBoard.setPenColor(QColor(0,0,0,0))
        elif text == '2：KNN':
            self.mode = 2
            #self.clearDataArea()
            self.pbtGetMnist.setEnabled(True)

            self.paintBoard.setBoardFill(QColor(0,0,0,0))
            self.paintBoard.setPenColor(QColor(0,0,0,0))

        elif text == '3：MLP':
            self.mode = 3
            #self.clearDataArea()
            self.pbtGetMnist.setEnabled(True)

            self.paintBoard.setBoardFill(QColor(0,0,0,0))
            self.paintBoard.setPenColor(QColor(0,0,0,0))  

        elif text == '4：SVM':
            self.mode = 4
            #self.clearDataArea()
            self.pbtGetMnist.setEnabled(True)

            self.paintBoard.setBoardFill(QColor(0,0,0,0))
            self.paintBoard.setPenColor(QColor(0,0,0,0))

        elif text == '5：DecisionTree':
            self.mode = 5
            #self.clearDataArea()
            self.pbtGetMnist.setEnabled(True)

            self.paintBoard.setBoardFill(QColor(0,0,0,0))
            self.paintBoard.setPenColor(QColor(0,0,0,0))

            # 更改背景
            self.paintBoard.setBoardFill(QColor(0,0,0,0))
            self.paintBoard.setPenColor(QColor(0,0,0,0))


    # 数据清除
    def pbtClear_Callback(self):
        self.clearDataArea()
 

    ## 识别
    def pbtPredict_Callback(self):

        img = self.img.reshape(1, 64)

        ## 预测数字
        self.result[0] = sample[self.mode].predict(img)
        self.result[1] = acc[self.mode]

        ## 输出到面板
        self.lbResult.setText("%d" % (self.result[0]))
        self.lbCofidence.setText("%.8f" % (self.result[1]))


  # 随机抽取
    def pbtGetMnist_Callback(self):
        self.clearDataArea()
        
        ## 随机抽取一张测试集图片，放大后显示
        img = x_test[np.random.randint(0, test_x.shape[0])]
        ## 用reshape把load_digits里的(1, 64)数组改成(8, 8)
        img = img.reshape(8, 8)                   # shape:[8,8]  
        ## 存储到self
        self.img = img

        img = img * 0x0c + 0x3f  # 调整灰度值大小 
        pil_img = Image.fromarray(np.uint8(img))
        pil_img = pil_img.resize((224, 224), Image.ANTIALIAS)        # 分辨率放大到(224, 224)

        qimage = ImageQt.ImageQt(pil_img)
        
        # 将qimage类型图像显示在label
        pix = QPixmap.fromImage(qimage)
        self.lbDataArea.setPixmap(pix)
        ###

    # 测试用
    def draw(self, img):

        # 放大后显示
        img = img.reshape(8, 8)                  

        img = img * 0x80      # 恢复灰度值大小 
        pil_img = Image.fromarray(np.uint8(img))
        pil_img = pil_img.resize((224, 224),Image.ANTIALIAS)        # 图像放大显示

        # 将pil图像转换成qimage类型
        qimage = ImageQt.ImageQt(pil_img)

 
        pix = QPixmap.fromImage(qimage)
        self.lbDataArea.setPixmap(pix)

    ## 测试 利用pyplot显示数字
    def pbtTest_Callback(self):

        a = np.array(self.img.reshape(8, 8))
        plt.subplot(111)
        plt.imshow(a, cmap=plt.cm.gray_r, interpolation='nearest')
        plt.show()


if __name__ == "__main__":
    # 实例化一个QApplication对象
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r'../../res/火箭.png'))
    # 创建一个MainWindow对象,用于GUI界面和交互逻辑
    Gui = MainWindow()
    Gui.show()

    sys.exit(app.exec_())