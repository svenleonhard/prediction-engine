import torch
from torch.autograd import Variable
import torch.nn.functional as F
import torch.utils.data as Data
from sklearn.preprocessing import StandardScaler
from machine_learning.helper.loss_writer import LossWriter

import matplotlib.pyplot as plt

import numpy as np
import imageio
import logging

logger = logging.getLogger(__name__)

class Network:
    
    def __init__(self, nn_config):
        self.lr = nn_config.lr
        self.epochs = nn_config.epochs
        self.scaler = StandardScaler()
        self.model = Net(nn_config.n_feature, nn_config.network_width,nn_config.network_width, 1)
        self.optimizer = torch.optim.SGD(self.model.parameters(), lr=self.lr, momentum=0.85)
        self.loss_func = torch.nn.MSELoss()
        self.loss_writer = LossWriter()

    def train(self, x_train, y_train):
        self.scaler.fit(x_train)
        x_scaled = self.scaler.transform(x_train)

        x = self.preprocess(x_scaled)
        y = self.preprocess(y_train)

        for t in range(self.epochs):
            # logger.info('epocch: %s', t)
            self.train_step(x, y)
        self.loss_writer.write()

    def train_step(self, x, y):
        prediction = self.model(x)
        prediction = torch.flatten(prediction)
        
        loss = self.loss_func(prediction, y)
        self.loss_writer.add(loss.item())
        # logger.info(loss.item())
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

    def preprocess(self, data):
        tensor = torch.from_numpy(data)
        return Variable(tensor.float())

    def predict(self, x):
        x = self.scaler.transform(x)
        x = self.preprocess(x)
        prediction = self.model(x)
        prediction = torch.flatten(prediction)
        return prediction.detach().numpy()

    def calc_loss(self, prediction, actual):
        actual = torch.from_numpy(actual)
        return self.loss_func(prediction, Variable(actual))


class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden_1, n_hidden_2, n_output):
        super(Net, self).__init__()
        # self.hidden = torch.nn.Linear(n_feature, n_hidden)   # hidden layer
        # self.predict = torch.nn.Linear(n_hidden, n_output)   # output layer
        # self.linear = torch.nn.Linear(n_feature, n_output)
        self.hid1 = torch.nn.Linear(n_feature, n_hidden_1)  # 13-(10-10)-1
        self.hid2 = torch.nn.Linear(n_hidden_1, n_hidden_2)
        self.oupt = torch.nn.Linear(n_hidden_2, n_output)
        torch.nn.init.xavier_uniform_(self.hid1.weight)  # glorot
        torch.nn.init.zeros_(self.hid1.bias)
        torch.nn.init.xavier_uniform_(self.hid2.weight)
        torch.nn.init.zeros_(self.hid2.bias)
        torch.nn.init.xavier_uniform_(self.oupt.weight)
        torch.nn.init.zeros_(self.oupt.bias)

    def forward(self, x):
        # x = torch.sigmoid(self.hidden(x))
        # # x = torch.sigmoid(x)      # activation function for hidden layer
        # x = self.predict(x)             # linear output
        # # return self.linear(x)
        # return x
        z = torch.sigmoid(self.hid1(x))
        # z = torch.sigmoid(self.hid2(x))
        # z = torch.sigmoid(self.hid2(z))
        # z = torch.tanh(self.hid3(z))
        z = self.oupt(z)
        return z