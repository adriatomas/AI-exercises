from torch.utils.data import Dataset
import os
from torchvision.transforms.functional import rotate
from torchvision.io import read_image
import torch

class SkinCancerPredictionDatasetLoader(Dataset):
    def __init__(self, url):
      benign_files = self.__set_benign_files__(url)
      malignant_files = self.__set_malignant_files__(url)
      self.files = benign_files + malignant_files

    def __set_benign_files__(self, url):
      files = []
      for img in os.listdir(f'{url}/benign'):
        files.append((f'{url}/benign/{img}', 0, 0))
        files.append((f'{url}/benign/{img}', 0, 1))
        files.append((f'{url}/benign/{img}', 0, 2))
        files.append((f'{url}/benign/{img}', 0, 3))
      
      return files

    def __set_malignant_files__(self, url):
      files = []
      for img in os.listdir(f'{url}/malignant'):
        files.append((f'{url}/malignant/{img}', 1, 0))
        files.append((f'{url}/malignant/{img}', 1, 1))
        files.append((f'{url}/malignant/{img}', 1, 2))
        files.append((f'{url}/malignant/{img}', 1, 3))
      
      return files

    def __len__(self):
      return len(self.files)
    
    def __rotate__(self, img, position):
      angle = position * 90

      return rotate(img, angle)

    def __getitem__(self, idx):
      file, label, rotation = self.files[idx]
      image_rotated = self.__rotate__(read_image(file), rotation)
      
      return image_rotated/255, torch.tensor(label)