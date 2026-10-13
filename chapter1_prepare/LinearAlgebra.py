import torch

A = torch.arange(20, dtype=torch.float).reshape(5,4)
A_sum = A.sum()
A_sum_axis0 = A.sum(dim=0)
A_sum_axis1 = A.sum(dim=1)
print(A_sum_axis0.shape)
print(A_sum_axis1.shape)

