import torch
import os
from torchvision.utils import save_image

# create a tensor of random numbers
x = torch.randn(4, 3, 32, 32)
file_name = 'validation.png'
# save the tensor as an image file
save_image(x, file_name,normalize=True, range=(-1, 1), padding=4)
