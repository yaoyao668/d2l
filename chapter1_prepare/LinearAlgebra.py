import torch

A = torch.arange(20, dtype=torch.float).reshape(5,4)
# A_sum = A.sum()
# A_sum_axis0 = A.sum(dim=0)
# A_sum_axis1 = A.sum(dim=1)
# print(A_sum_axis0.shape)
# print(A_sum_axis1.shape)

# # Practice 4
# X = torch.arange(24, dtype=torch.float).reshape(2,3,4)
# X1 = torch.arange(120, dtype=torch.float).reshape(5,4,6)
# print(len(X))
# print(len(X1))
# print(X.size())

# Practice 6
A_sum_dim1 = A.sum(dim=1)
# print(A_sum_dim1)
print(A)
A_sum_dim0 = A.sum(dim=0)
print(A_sum_dim0)
print(A/A_sum_dim0)
# print(A/A_sum_dim1)
