from tqdm import tqdm

from app import APP

import argparse
parser = argparse.ArgumentParser(description='trainer parser')
parser.add_argument('app', type=str, help='a name of an app that needs to be trained')
parser.add_argument('--device', type=str, default="cuda", help='device')
parser.add_argument('--batch_size', type=int, default=32, help='batch size')
parser.add_argument('--shuffle', type=bool, default=True, help='a boolean value that indicates whether to shuffle or not')
parser.add_argument('--num_workers', type=int, default=0, help='number of workers to load data')
parser.add_argument('--test_interval', type=int, default=1, help='test interval in epochs')
args = parser.parse_args()

if __name__ == "__main__":
    # Initialize an app
    app = APP[args.app](device=args.device)

    # Initialize dataloader
    train_dataloader = app.get_dataloader(train=True,
                                          batch_size=args.batch_size,
                                          shuffle=args.shuffle,
                                          num_workers=args.num_workers)

    test_dataloader = app.get_dataloader(train=False,
                                          batch_size=args.batch_size,
                                          shuffle=args.shuffle,
                                          num_workers=args.num_workers)

    optimizer = app.get_optimizer()

    # Epoch Index
    epoch = 0

    while True:
        app.model.train()        

        train_pbar = tqdm(train_dataloader, desc="Train ")

        for iter_idx, input_data in enumerate(train_pbar):
            # Initialize gradients to zero
            optimizer.zero_grad()

            output_data = app.forward(input_data=input_data) 

            loss_data = app.backward(input_data=input_data,
                                     output_data=output_data)

            optimizer.step()

            desc = app.get_description(epoch, iter_idx, input_data, output_data, loss_data)
            desc = "Train {}".format(desc)
            train_pbar.set_description(desc)

        if (epoch+1) % args.test_interval == 0:
            app.model.eval()

            test_pbar = tqdm(test_dataloader, desc="Test ")

            for iter_idx, input_data in enumerate(test_pbar):
                output_data = app.forward(input_data=input_data) 

                loss_data = app.backward(input_data=input_data,
                                        output_data=output_data,
                                        train=False)

                desc = app.get_description(epoch, iter_idx, input_data, output_data, loss_data)
                desc = "Test {}".format(desc)
                test_pbar.set_description(desc)

        epoch += 1
