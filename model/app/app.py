
class App:
    def __init__(self, device):
        self.device = device
        self.model = self.get_model().to(self.device)

    def get_model(self):
        raise NotImplementedError()

    def get_dataloader(self, train=True, batch_size=1, shuffle=True, num_workers=0):
        raise NotImplementedError()

    def get_optimizer(self):
        raise NotImplementedError()

    def get_description(self, epoch, iter_idx, input_data, output_data, loss_data):
        raise NotImplementedError()

    def forward(self, input_data):
        raise NotImplementedError()

    def backward(self, input_data, output_data, train=True):
        raise NotImplementedError()
