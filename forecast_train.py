from Informer.exp.exp_informer import Exp_Informer as Exp
import torch
from config import args, setting


def train(args):
    print("Args in experiment:")
    print(args)

    # set experiments
    exp = Exp(args)

    # train
    print(">>>>>>>start training : {}>>>>>>>>>>>>>>>>>>>>>>>>>>".format(setting))
    exp.train(setting)

    # test
    print(">>>>>>>testing : {}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<".format(setting))
    exp.test(setting)

    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    if torch.backends.mps.is_available():
        torch.backends.mps.empty_cache()


if __name__ == "__main__":
    train(args)
