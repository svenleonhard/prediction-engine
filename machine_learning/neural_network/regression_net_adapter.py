
from machine_learning.neural_network.net_adapter import NetAdapter
from machine_learning.neural_network.regression_net import RegressionNet

import torch
import torch.nn as nn
import torch.optim as optim

import logging

logger = logging.getLogger(__name__)

class RegressionNetAdapter(NetAdapter):

    def __init__(self, nn_config):
        NetAdapter.__init__(self, nn_config, nn.MSELoss(), optim.SGD, RegressionNet)
