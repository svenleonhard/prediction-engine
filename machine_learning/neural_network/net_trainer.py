from machine_learning.neural_network.accuracy import Accuracy
from machine_learning.helper.loss_writer import LossWriter
import torch

import logging

logger = logging.getLogger(__name__)

class NetTrainer(object):

    def __init__(self, criterion, optimizer, model, epochs, device, lr):
        self.criterion = criterion
        self.optimizer = optimizer
        self.model = model
        self.epochs = epochs
        self.device = device
        self.lr = lr
        self.loss_writer = LossWriter()

    def train(self, train_loader):
        self.train_init_log()
        self.model.train()
        for epoch in range(1, self.epochs+1):
            self.epoch(epoch, train_loader)
        return self.model

    def epoch(self,e,train_loader):
        epoch_loss = 0
        epoch_acc = 0
        for X_batch, y_batch in train_loader:
            self.optimizer.zero_grad()
            X_batch, y_batch = X_batch.to(self.device), y_batch.to(self.device)
                
            y_pred = self.model(X_batch)
            
            loss = self.criterion(y_pred, y_batch.unsqueeze(1))
            accuracy = Accuracy.binary(y_pred, y_batch.unsqueeze(1))
                
            loss.backward()
            self.optimizer.step()
                
            epoch_loss += loss.item()
            epoch_acc += accuracy.item()
        self.epoch_log(e, epoch_loss, train_loader, epoch_acc)


    def train_init_log(self):
        logger.info("Start training")
        logger.info("Learning rate: %s", self.lr)
        logger.info("Epochs: %s", self.epochs)
        logger.info("Network: %s", self.model)
        logger.info("Using device: %s", self.device)

    def epoch_log(self, e, epoch_loss, train_loader, epoch_acc):
        self.loss_writer.add(epoch_loss)
        print('Epoch {0:03d}: | Loss: {1:.5f} | Acc: {2:.5f}'.format(e, epoch_loss/len(train_loader), epoch_acc/len(train_loader)))
