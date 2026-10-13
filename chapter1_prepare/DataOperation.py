from re import T

import torch
x = torch.arange(12)
X = x.reshape(2,6)
# print(torch.zeros(2,3,4))
# print(torch.ones(2,3,4))
# print(torch.ones(2,3,4))
a = torch.arange(3).reshape(3,-1)
b = torch.arange(2).reshape(1,-1)
c = a+b
X = torch.randn(3,4)
# print(X)
# print(X[0])
# print(X[-1])
# 广播机制
d = torch.arange(27).reshape(3,3,3)
e = torch.arange(9).reshape(3,3,1)
f = d+e


