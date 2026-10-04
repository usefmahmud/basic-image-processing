import numpy as np
from PIL import Image

def load(path):
   return np.array(Image.open(path).convert("RGB"))

def save(arr, path):
   Image.fromarray(arr).save(path)