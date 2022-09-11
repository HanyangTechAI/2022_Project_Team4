

class App:
    def __init__(self, device):
        self.device = device

    def get_model(self):
        raise NotImplementedError()

    def get_dataloader(self):
        raise NotImplementedError()

    def get_criterion(self):
        raise NotImplementedError()

    def train(self):
        raise NotImplementedError()

