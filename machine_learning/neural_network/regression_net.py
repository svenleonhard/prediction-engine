import torch
from torch.autograd import Variable
import torch.nn.functional as F
import torch.utils.data as Data
from sklearn.preprocessing import StandardScaler

import numpy as np
import logging

logger = logging.getLogger(__name__)

class RegressionNet(torch.nn.Module):
    def __init__(self, n_feature, network_width=10):
        super(RegressionNet, self).__init__()
        # self.hidden = torch.nn.Linear(n_feature, n_hidden)   # hidden layer
        # self.predict = torch.nn.Linear(n_hidden, n_output)   # output layer
        # self.linear = torch.nn.Linear(n_feature, n_output)
        self.hid1 = torch.nn.Linear(n_feature, network_width)  # 13-(10-10)-1
        self.hid2 = torch.nn.Linear(network_width, network_width)
        self.oupt = torch.nn.Linear(network_width, 1)

        self.dropout = torch.nn.Dropout(p=0.1)
        self.batchnorm1 = torch.nn.BatchNorm1d(network_width)
        # torch.nn.init.xavier_uniform_(self.hid1.weight)  # glorot
        # torch.nn.init.zeros_(self.hid1.bias)
        # torch.nn.init.xavier_uniform_(self.hid2.weight)
        # torch.nn.init.zeros_(self.hid2.bias)
        # torch.nn.init.xavier_uniform_(self.oupt.weight)
        # torch.nn.init.zeros_(self.oupt.bias)

    def forward(self, x):
        # x = torch.sigmoid(self.hidden(x))
        # # x = torch.sigmoid(x)      # activation function for hidden layer
        # x = self.predict(x)             # linear output
        # # return self.linear(x)
        # return x
        # z = torch.tanh(self.hid1(x))
        # z = torch.sigmoid(self.hid2(z))
        # z = torch.tanh(self.hid3(z))
        # z = self.oupt(z)
        # return z
        x = torch.sigmoid(self.hid1(x))
        x = self.dropout(x)
        # z = torch.tanh(self.hid2(z))
        # z = torch.tanh(self.hid2(z))
        # z = torch.tanh(self.hid3(z))
        x = self.oupt(x)
        return x