from sklearn.preprocessing import StandardScaler    
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import Dataset, DataLoader
import pandas as pd

class ClassDataPreprocessing(object):

    def __init__(self, train_batch_size, test_batch_size):
        self.train_batch_size = train_batch_size
        self.test_batch_size = test_batch_size
        self.scaler = StandardScaler()
        
    def train_loader(self, input_train, label_train):
        self.input_train = self.scaler.fit_transform(input_train)
        train_data = TrainData(torch.FloatTensor(input_train), 
                    torch.FloatTensor(label_train))
        return DataLoader(dataset=train_data, batch_size=self.train_batch_size, shuffle=True)
        
    def test_loader(self, input_test):
        self.input_test = self.scaler.fit_transform(input_test)
        test_data = TestData(torch.FloatTensor(input_test))
        return DataLoader(dataset=test_data, batch_size=self.test_batch_size)

    def _encode_delay(self, df, delay_limit = 60):
        df.loc[df["delay"] > delay_limit, 'delay'] = 1
        df.loc[(df["delay"] <= delay_limit) & (df["delay"] != 1), 'delay'] = 0
        return df

class TestData(Dataset):
    
    def __init__(self, input_data):
        self.input_data = input_data
        
    def __getitem__(self, index):
        return self.input_data[index]
        
    def __len__ (self):
        return len(self.input_data)

class TrainData(Dataset):
    
    def __init__(self, input_data, label_data):
        self.input_data = input_data
        self.label_data = label_data
        
    def __getitem__(self, index):
        return self.input_data[index], self.label_data[index]
        
    def __len__ (self):
        return len(self.input_data)
