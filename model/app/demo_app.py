import torch
import torch.nn as nn
from torch.optim import SGD
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
import torchvision.transforms as transforms

from .app import App


class DemoModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.seq_layer = nn.Sequential(
            nn.Linear(28 * 28, 28 * 14),
            nn.Linear(28 * 14, 28 * 7),
            nn.Linear(28 * 7, 28),
            nn.Linear(28, 10)
        )
        self.linear = nn.Linear(28 * 28, 10)

    def forward(self, x):
        return self.linear(x)


class DemoApp(App):
    def __init__(self, device):
        super().__init__(device)

        self.criterion = nn.CrossEntropyLoss()

    def get_model(self):
        return DemoModel().to(self.device)

    def get_dataloader(self, train=True, batch_size=1, shuffle=True, num_workers=0):
        transform = transforms.Compose([
            transforms.ToTensor(), 
            transforms.Normalize((0.5,), (1.0,))
        ])

        mnist_dataset = MNIST("~/dataset", transform=transform, train=train, download=True)
        mnist_dataloader = DataLoader(mnist_dataset, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers)
        return mnist_dataloader

    def get_optimizer(self):
        return SGD(self.model.parameters(), lr=1e-3)

    def get_description(self, epoch, iter_idx, input_data, output_data, loss_data):
        loss = loss_data.cpu().detach().numpy()
        return "{:2f}".format(loss)

    def forward(self, input_data):
        image = input_data[0].to(self.device)
        image = torch.reshape(image, (-1, 28 * 28))

        logit = self.model(image)

        output_data = {
            "logit": logit
        }

        return output_data

    def backward(self, input_data, output_data, train=True):
        # [batch_size]
        ground_truth = input_data[1].to(self.device)

        # [batch_size, 10 (num_classes)]
        logit = output_data["logit"]

        loss = self.criterion(logit, ground_truth)
        
        if train:
            loss.backward()
        
        return loss
