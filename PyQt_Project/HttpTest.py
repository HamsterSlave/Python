from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5 import uic

class HttpTest(QObject):
    def __init__(self):
        QObject.__init__(self)
        # 从 UI 定义中动态 创建一个相应的窗口对象
        self.ui = uic.loadUi(r"../UI/Httptest.ui")
        # 给 boxMethod 添加选项 GET POST PUT DELETE
        self.ui.comboBox.addItems(
            ['GET', 'POST', 'PUT', 'DELETE'])
        # 让 表格控件宽度随着父窗口的缩放自动缩放
        self.ui.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        # 设定第1列的宽度为 180像素
        self.ui.tableWidget_2.setColumnWidth(0, 180)
        self.ui.pushButton.clicked.connect(self.sendRequest)



app = QApplication([])
# 加载 icon
app.setWindowIcon(QIcon('logo.png'))
httpClient = HttpTest()
httpClient.ui.show()
app.exec_()