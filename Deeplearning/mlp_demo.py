import matplotlib.pyplot as plt
import sys
import numpy as np
import torch
sys.path.append("..")
import d2lzh_pytorch as d2l


def xyplot(num,x_vals, y_vals, name):
    d2l.plt.figure(num)
    d2l.set_figsize(figsize=(5,2.5))
    d2l.plt.plot(x_vals.detach().numpy(),y_vals.detach().numpy())
    d2l.plt.xlabel('x')
    d2l.plt.ylabel(name + '(x)')
    d2l.plt.show()


x = torch.arange(-8.0, 8.0, 0.1, requires_grad=True)
y = x.relu()
xyplot(1,x, y, 'relu')
y.sum().backward()
xyplot(2,x,x.grad,'grad of ralu')

z = x.sigmoid()
xyplot(3,x,z,'sigmoid')
x.grad.zero_()
z.sum().backward()
xyplot(4,x,x.grad,'grad of sigmoid')

l = x.tanh()
xyplot(5,x,l,'tanh')
x.grad.zero_()
l.sum().backward()
xyplot(6,x,x.grad,'grad of tanh')
