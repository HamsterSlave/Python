import traceback

import requests
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5 import uic

class HttpTest(QObject):
    def __init__(self):
        QObject.__init__(self)
        # 从 UI 定义中动态 创建一个相应的窗口对象
        self.ui = uic.loadUi(r"../UI/Httptest.ui")
        # 给 comboBox 添加选项 GET POST PUT DELETE
        self.ui.comboBox.addItems(
            ['GET', 'POST', 'PUT', 'DELETE'])
        # 给 comboBox_2 添加选项 GET POST PUT DELETE
        # 让 表格控件宽度随着父窗口的缩放自动缩放
        self.ui.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        # 设定第1列的宽度为 180像素
        self.ui.tableWidget_2.setColumnWidth(0, 180)
        # 信号处理：发送请求
        self.ui.pushButton.clicked.connect(self.sendRequest)
        # 信号处理：添加消息头
        self.ui.pushButton_3.clicked.connect(self.addOneHeader)
        # 信号处理：删除消息头
        self.ui.pushButton_2.clicked.connect(self.delOneHeader)
        # 信号处理：清除
        self.ui.pushButton_4.clicked.connect(self.delAll)

    def sendRequest(self):
        method = self.ui.comboBox.currentText()
        url = self.ui.lineEdit.text()
        payload = self.ui.textEdit_2.toPlainText()

        # 获取消息头
        headers = {}
        ht = self.ui.tableWidget_2
        for row in range(ht.rowCount()):
            k = ht.item(row, 0).text()
            v = ht.item(row, 1).text()
            if k.strip() == '':
                continue
            headers[k] = v

        req = requests.Request(method,
                               url,
                               headers=headers,
                               data=payload
                               )


        prepared = req.prepare()

        self.pretty_print_request(prepared)
        s = requests.Session()

        try:
            r = s.send(prepared)
            self.pretty_print_response(r)
        except:
            self.ui.outputWindow.append(
                traceback.format_exc())

    def addOneHeader(self):

        # rowCount = self.ui.headersTable.rowCount()
        # 要插入的行始终是当前行 的下一行
        addRowNumber = self.ui.tableWidget_2.currentRow() + 1
        self.ui.tableWidget_2.insertRow(addRowNumber)

    def delOneHeader(self):

        self.ui.tableWidget_2.removeRow(
            self.ui.tableWidget_2.currentRow()
        )

    def delAll(self):
        self.ui.textEdit.clear()

    def pretty_print_request(self,req):

        if req.body is None:
            msgBody = ''
        else:
            msgBody = req.body

        self.ui.textEdit.append(
            '{}\n{}\n{}\n\n{}'.format(
            '\n\n----------- 发送请求 -----------',
            req.method + ' ' + req.url,
            '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
            msgBody,
        ))

    def pretty_print_response(self,res):
        self.ui.textEdit.append(
            '{}\nHTTP/1.1 {}\n{}\n\n{}'.format(
            '\n\n----------- 得到响应 -----------',
            res.status_code,
            '\n'.join('{}: {}'.format(k, v) for k, v in res.headers.items()),
            res.text,
        ))


app = QApplication([])
# 加载 icon
app.setWindowIcon(QIcon(r'../res/火箭.png'))
httpClient = HttpTest()
httpClient.ui.show()
app.exec_()