import torch
from torch import nn

x = torch.ones(3)
y = torch.zeros(4)
# torch.save([x, y], 'xy.pt')
# xy_list = torch.load('xy.pt')
# print(xy_list)
torch.save({'x': x, 'y': y}, 'xy_dict.pt')
xy = torch.load('xy_dict.pt')
print(xy)