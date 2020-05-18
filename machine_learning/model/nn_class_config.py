class NNClassConfig(object):

    def __init__(self, config_dict):
        self.lr = config_dict['lr']
        self.epochs = config_dict['epochs']
        self.device_type = config_dict['device_type']
        self.train_batch_size = config_dict['train_batch_size']
        self.test_batch_size = config_dict['test_batch_size']
        self.network_width = config_dict['network_width']
        self.n_feature = config_dict['n_feature']
