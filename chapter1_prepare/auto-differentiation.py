import torch 
x = torch.arange(4.0)
x.requires_grad = True
print(x.grad) #此时还没有梯度
y = 2 * torch.dot(x,x)
print(y)
y.backward()
print(x.grad)

x.grad.zero_()
y = x.sum()
y.backward()
print(x.grad)
