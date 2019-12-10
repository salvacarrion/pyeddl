"""\
VGG16 for CIFAR10 with batch normalization.
"""

import argparse
import sys

import pyeddl._core.eddl as eddl
import pyeddl._core.eddlT as eddlT


def Block1(layer, filters):
    return eddl.ReLu(
        eddl.BatchNormalization(eddl.Conv(layer, filters, [1, 1], [1, 1]))
    )


def Block3_2(layer, filters):
    layer = eddl.ReLu(
        eddl.BatchNormalization(eddl.Conv(layer, filters, [3, 3], [1, 1]))
    )
    layer = eddl.ReLu(
        eddl.BatchNormalization(eddl.Conv(layer, filters, [3, 3], [1, 1]))
    )
    return layer


def main(args):
    eddl.download_cifar10()

    num_classes = 10

    in_ = eddl.Input([3, 32, 32])

    layer = in_
    layer = eddl.CropScaleRandom(layer, [0.8, 1.0])
    layer = eddl.Flip(layer, 1)
    layer = eddl.MaxPool(Block3_2(layer, 64))
    layer = eddl.MaxPool(Block3_2(layer, 128))
    layer = eddl.MaxPool(Block1(Block3_2(layer, 256), 256))
    layer = eddl.MaxPool(Block1(Block3_2(layer, 512), 512))
    layer = eddl.MaxPool(Block1(Block3_2(layer, 512), 512))
    layer = eddl.Reshape(layer, [-1])
    layer = eddl.ReLu(eddl.BatchNormalization(eddl.Dense(layer, 512)))

    out = eddl.Activation(eddl.Dense(layer, num_classes), "softmax")
    net = eddl.Model([in_], [out])

    eddl.build(
        net,
        eddl.sgd(0.01, 0.9),
        ["soft_cross_entropy"],
        ["categorical_accuracy"],
        eddl.CS_GPU([1]) if args.gpu else eddl.CS_CPU()
    )

    eddl.summary(net)
    eddl.plot(net, "model.pdf", "TB")

    x_train = eddlT.load("cifar_trX.bin")
    y_train = eddlT.load("cifar_trY.bin")
    eddlT.div_(x_train, 255.0)

    x_test = eddlT.load("cifar_tsX.bin")
    y_test = eddlT.load("cifar_tsY.bin")
    eddlT.div_(x_test, 255.0)

    for i in range(args.epochs):
        eddl.fit(net, [x_train], [y_train], args.batch_size, 1)
        eddl.evaluate(net, [x_test], [y_test])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--epochs", type=int, metavar="INT", default=10)
    parser.add_argument("--batch-size", type=int, metavar="INT", default=100)
    parser.add_argument("--gpu", action="store_true")
    main(parser.parse_args(sys.argv[1:]))
