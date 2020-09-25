# Copyright (c) 2020 CRS4
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""\
Check usage of getOut and forward in a network with a non-empty lout.
"""

import argparse
import os
import sys

import pyeddl.eddl as eddl
from pyeddl.tensor import Tensor


def main(args):
    if not os.path.isfile(args.input):
        raise RuntimeError("input file '%s' not found" % args.input)

    eddl.download_mnist()

    net = eddl.import_net_from_onnx_file(args.input)
    eddl.build(
        net,
        eddl.rmsprop(0.01),
        ["soft_cross_entropy"],
        ["categorical_accuracy"],
        eddl.CS_GPU([1]) if args.gpu else eddl.CS_CPU(),
        False  # do not initialize weights to random values
    )

    net.resize(args.batch_size)  # resize manually since we don't use "fit"
    eddl.summary(net)

    x_test = Tensor.load("mnist_tsX.bin")
    x_test.div_(255.0)

    sys.stderr.write("forward...\n")
    eddl.forward(net, [x_test])
    sys.stderr.write("forward done\n")

    sys.stderr.write("lout: %r\n" % (net.lout,))
    out = eddl.getOut(net)
    sys.stderr.write("getOut done\n")
    sys.stderr.write("out: %r\n" % (out,))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-size", type=int, metavar="INT", default=1000)
    parser.add_argument("--gpu", action="store_true")
    parser.add_argument("--input", metavar="STRING",
                        default="trained_model.onnx",
                        help="input path of the serialized model")
    main(parser.parse_args(sys.argv[1:]))
