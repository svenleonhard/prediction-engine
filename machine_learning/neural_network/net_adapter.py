from machine_learning.neural_network.class_net import ClassNet
from machine_learning.neural_network.net_trainer import NetTrainer

from sklearn.preprocessing import StandardScaler    
from sklearn.model_selection import train_test_split
from machine_learning.neural_network.class_data_preprocessing import ClassDataPreprocessing

import torch
import torch.nn as nn

import logging

logger = logging.getLogger(__name__)

class NetAdapter(object):

    def __init__(self, nn_config, criterion, optim, model):
        self.lr = nn_config.lr
        self.epochs = nn_config.epochs
        self.model = model(n_feature=nn_config.n_feature, network_width=nn_config.network_width)
        device = torch.device(nn_config.device_type)
        self.model.to(device)
        optimizer = optim(self.model.parameters(), lr=self.lr)
        self.train_batch_size = nn_config.train_batch_size
        self.test_batch_size = nn_config.test_batch_size
        self.data_preprocessor = ClassDataPreprocessing(self.train_batch_size, self.test_batch_size)
        self.net_trainer = NetTrainer(criterion, optimizer, self.model, self.epochs, device, self.lr)

    def train(self, x_train, y_train):
        self.model = self.net_trainer.train(self.data_preprocessor.train_loader(x_train, y_train))

    def predict(self, x_test):
        y_pred_list = []
        self.model.eval()
        with torch.no_grad():
            for X_batch in self.data_preprocessor.test_loader(x_test):
                y_test_pred = self.model(X_batch)
                y_test_pred = torch.sigmoid(y_test_pred)
                y_test_pred = torch.round(y_test_pred)
                y_pred_list.append(y_test_pred.cpu().numpy())
        y_pred_list = [a.squeeze().tolist() for a in y_pred_list]
        return y_pred_list
