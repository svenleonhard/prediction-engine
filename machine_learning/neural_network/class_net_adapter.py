from machine_learning.neural_network.class_net import ClassNet
from machine_learning.neural_network.net_trainer import NetTrainer
from machine_learning.neural_network.net_adapter import NetAdapter

from sklearn.preprocessing import StandardScaler    
from sklearn.model_selection import train_test_split
from machine_learning.neural_network.class_data_preprocessing import ClassDataPreprocessing

import torch
import torch.nn as nn
import torch.optim as optim

import logging

logger = logging.getLogger(__name__)

class ClassNetAdapter(NetAdapter):

    def __init__(self, nn_config):
        NetAdapter.__init__(self, nn_config, nn.BCEWithLogitsLoss(), optim.Adam, ClassNet)

 
