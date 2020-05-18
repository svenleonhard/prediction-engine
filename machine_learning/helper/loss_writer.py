import pandas as pd

class LossWriter(object):

    def __init__(self):
        self.losses = []

    def add(self, loss):
        self.losses.append(loss)

    def write(self):
        df = pd.DataFrame(self.losses)
        df.to_csv('datasets/loss.csv')
