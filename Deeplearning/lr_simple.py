import torch
import numpy as np
import random
import torch.utils.data as Date
import torch.nn as nn
from torch.nn import init
import torch.optim as optim


def linreg(X, w, b):  # 本函数已保存在d2lzh_pytorch包中方便以后使用
    return torch.mm(X, w) + b

def squared_loss(y_hat, y):  # 本函数已保存在d2lzh_pytorch包中方便以后使用
    # 注意这里返回的是向量, 另外, pytorch里的MSELoss并没有除以 2
    return (y_hat - y.view(y_hat.size())) ** 2 / 2

def sgd(params, lr, batch_size):  # 本函数已保存在d2lzh_pytorch包中方便以后使用
    for param in params:
        param.data -= lr * param.grad / batch_size  # 注意这里更改param时用的param.data


num_inputs = 2
num_examples = 1000
true_w = [2, -3.4]
true_b = 4.2
features = torch.randn(num_examples, num_inputs, dtype=torch.float32)
a = true_w[0]
labels = true_w[0] * features[:, 0] + true_w[1] * features[:, 1] + true_b
labels += torch.tensor(np.random.normal(0, 0.01, size=labels.size()), dtype=torch.float32)

batch_size = 10
dataset = Date.TensorDataset(features,labels)
data_iter = Date.DataLoader(dataset, batch_size,shuffle=True)
for X, y in data_iter:
    print(X, y)
    break
# 定义模型
# class LinearNet(nn.Module):
#     def __init__(self, n_feature):
#         super(LinearNet, self).__init__()
#         self.linear = nn.Linear(n_feature, 1)
#     # forward 定义前向传播
#     def forward(self, x):
#         y = self.linear(x)
#         return y
#
# net = LinearNet(num_inputs)
# print(net) # 使用print可以打印出网络的结构
# 写法一
net = nn.Sequential(
    nn.Linear(num_inputs, 1)
    # 此处还可以传入其他层
    )

# 写法二
# net = nn.Sequential()
# net.add_module('linear', nn.Linear(num_inputs, 1))
# # net.add_module ......

# # 写法三
# from collections import OrderedDict
# net = nn.Sequential(OrderedDict([
#           ('linear', nn.Linear(num_inputs, 1))
#           # ......
#         ]))
#
# print(net)
# print(net[0])

for param in net.parameters():
    print(param)
#初始化模型参数
init.normal_(net[0].weight, mean=0, std=0.01)
init.constant_(net[0].bias, val=0)  # 也可以直接修改bias的data: net[0].bias.data.fill_(0)
#定义损失函数
loss = nn.MSELoss()
#定义优化算法
optimizer = optim.SGD(net.parameters(), lr=0.03)
print(optimizer)
#训练模型
num_epochs = 3
for epoch in range(1, num_epochs + 1):
    for X, y in data_iter:
        output = net(X)
        l = loss(output, y.view(-1, 1))
        optimizer.zero_grad() # 梯度清零，等价于net.zero_grad()
        l.backward()
        optimizer.step()
    print('epoch %d, loss: %f' % (epoch, l.item()))
dense = net[0]
print(true_w, dense.weight)
print(true_b, dense.bias)