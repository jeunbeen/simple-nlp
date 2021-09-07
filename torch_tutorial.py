import torch
import numpy as np

# 2*2 matrix
x = torch.Tensor([[1,2],[3,4]])
x = torch.from_numpy(np.array([[1,2], [3,4]]))

# same code using numpy
x = np.array([[1,2], [3,4]])

# autograd
x = torch.FloatTensor(2,2)
y = torch.FloatTensor(2,2)
y.requires_grad_(True)
z = (x+y) + torch.FloatTensor(2,2)

# no gradient
x = torch.FloatTensor(2,2)
y = torch.FloatTensor(2,2)
y.requires_grad_(True)
with torch.no_grad():
    z = (x+y) + torch.FloatTensor(2,2)

