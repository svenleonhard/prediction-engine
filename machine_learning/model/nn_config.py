class NNConfig:

    def __init__(self, config_dict):
        self.epochs = config_dict['epochs']
        self.lr = config_dict['lr']
        self.n_feature = config_dict['n_feature']
        self.n_hidden_1 = config_dict['n_hidden_1']
        self.n_hidden_2 = config_dict['n_hidden_2']
        self.n_output = config_dict['n_output']
