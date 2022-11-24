import os
from os import path
import time
from argparse import ArgumentParser
from collections import defaultdict

import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader
import numpy as np
from PIL import Image

from model.eval_network import PropagationNetwork
from dataset.davis_test_dataset import DAVISTestDataset
from inference_core import InferenceCore

from progressbar import progressbar


test_dataset = DAVISTestDataset('../DAVIS/2017/trainval', imset='2017/val.txt')
test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False, pin_memory=True)
#test_loader = DataLoader(test_dataset,batch_size=1,shuffle=False)

for data in test_loader:
  rgb = data['rgb'].cuda()
  msk = data['gt'][0].cuda()
  info = data['info']
  print(rgb.shape)
  print(msk[:,0].shape)
  print(info['labels'][0])
  break