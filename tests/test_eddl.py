# Copyright (c) 2019 CRS4
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

import pyeddl._core.eddl as eddl


def test_core_layers():
    in2d = eddl.Input([16])
    in4d = eddl.Input([3, 16, 16])
    eddl.Activation(in2d, "relu")
    eddl.Activation(in2d, "relu", 0.02)
    eddl.Activation(in2d, "relu", 0.02, "foo")
    eddl.Softmax(in2d)
    eddl.Sigmoid(in2d)
    eddl.ReLu(in2d)
    eddl.LReLu(in2d)
    eddl.LReLu(in2d, 0.02)
    eddl.Tanh(in2d)
    eddl.Conv(in4d, 16, [1, 1])
    eddl.Conv(in4d, 16, [1, 1], [2, 2], "none")
    eddl.Conv(in4d, 16, [1, 1], [2, 2], "none", 1)
    eddl.Conv(in4d, 16, [1, 1], [2, 2], "none", 1, [1, 1])
    eddl.Conv(in4d, 16, [1, 1], [2, 2], "none", 1, [1, 1], True)
    eddl.Conv(in4d, 16, [1, 1], [2, 2], "none", 1, [1, 1], True, "foo")
    eddl.ConvT(in4d, 16, [1, 1], [2, 2])
    eddl.ConvT(in4d, 16, [1, 1], [2, 2], "none")
    eddl.ConvT(in4d, 16, [1, 1], [2, 2], "none", [1, 1])
    eddl.ConvT(in4d, 16, [1, 1], [2, 2], "none", [1, 1], [1, 1])
    eddl.ConvT(in4d, 16, [1, 1], [2, 2], "none", [1, 1], [1, 1], True)
    eddl.ConvT(in4d, 16, [1, 1], [2, 2], "none", [1, 1], [1, 1], True, "foo")
    eddl.Dense(in2d, 16)
    eddl.Dense(in2d, 16, True)
    eddl.Dense(in2d, 16, True, "foo")
    eddl.Embedding(2, 3)
    eddl.Embedding(2, 3, "foo")
    eddl.Input([16], "foo")
    eddl.UpSampling(in4d, [2, 2])
    eddl.UpSampling(in4d, [2, 2], "nearest")
    eddl.UpSampling(in4d, [2, 2], "nearest", "foo")
    eddl.Reshape(in2d, [1, 4, 4])
    eddl.Reshape(in2d, [1, 4, 4], "foo")
    eddl.Transpose(in2d, [0])
    eddl.Transpose(in2d, [0], "foo")


def test_transformations():
    in2d = eddl.Input([16])
    eddl.Shift(in2d, [1, 1])
    eddl.Shift(in2d, [1, 1], "nearest")
    eddl.Shift(in2d, [1, 1], "nearest", 0.0)
    eddl.Shift(in2d, [1, 1], "nearest", 0.0, "foo")
    eddl.Rotate(in2d, 1.1)
    eddl.Rotate(in2d, 1.1, [0, 0])
    eddl.Rotate(in2d, 1.1, [0, 0], "nearest")
    eddl.Rotate(in2d, 1.1, [0, 0], "nearest", 0.0)
    eddl.Rotate(in2d, 1.1, [0, 0], "nearest", 0.0, "foo")
    eddl.Scale(in2d, [1, 4], True)
    eddl.Scale(in2d, [1, 4], True, "nearest")
    eddl.Scale(in2d, [1, 4], True, "nearest", 0.0)
    eddl.Scale(in2d, [1, 4], True, "nearest", 0.0, "foo")
    eddl.Flip(in2d)
    eddl.Flip(in2d, 0)
    eddl.Flip(in2d, 0, "foo")
    eddl.Crop(in2d, [0, 0], [3, 3], True)
    eddl.Crop(in2d, [0, 0], [3, 3], True, 0.0)
    eddl.Crop(in2d, [0, 0], [3, 3], True, 0.0, "foo")
    eddl.CropAndScale(in2d, [0, 0], [3, 3])
    eddl.CropAndScale(in2d, [0, 0], [3, 3], "nearest")
    eddl.CropAndScale(in2d, [0, 0], [3, 3], "nearest", 0.0)
    eddl.CropAndScale(in2d, [0, 0], [3, 3], "nearest", 0.0, "foo")
    eddl.Cutout(in2d, [0, 0], [3, 3])
    eddl.Cutout(in2d, [0, 0], [3, 3], 0.0)
    eddl.Cutout(in2d, [0, 0], [3, 3], 0.0, "foo")


def test_data_augmentation():
    in2d = eddl.Input([16])
    eddl.ShiftRandom(in2d, [1.0, 1.0], [2.0, 2.0])
    eddl.ShiftRandom(in2d, [1.0, 1.0], [2.0, 2.0], "nearest")
    eddl.ShiftRandom(in2d, [1.0, 1.0], [2.0, 2.0], "nearest", 0.0)
    eddl.ShiftRandom(in2d, [1.0, 1.0], [2.0, 2.0], "nearest", 0.0, "foo")
    eddl.RotateRandom(in2d, [1.0, 1.0])
    eddl.RotateRandom(in2d, [1.0, 1.0], [0, 0])
    eddl.RotateRandom(in2d, [1.0, 1.0], [0, 0], "nearest")
    eddl.RotateRandom(in2d, [1.0, 1.0], [0, 0], "nearest", 0.0)
    eddl.RotateRandom(in2d, [1.0, 1.0], [0, 0], "nearest", 0.0, "foo")
    eddl.ScaleRandom(in2d, [1.0, 1.0])
    eddl.ScaleRandom(in2d, [1.0, 1.0], "nearest")
    eddl.ScaleRandom(in2d, [1.0, 1.0], "nearest", 0.0)
    eddl.ScaleRandom(in2d, [1.0, 1.0], "nearest", 0.0, "foo")
    eddl.FlipRandom(in2d, 0)
    eddl.FlipRandom(in2d, 0, "foo")
    eddl.CropRandom(in2d, [4, 4])
    eddl.CropRandom(in2d, [4, 4], "foo")
    eddl.CropScaleRandom(in2d, [1.0, 1.0])
    eddl.CropScaleRandom(in2d, [1.0, 1.0], "nearest")
    eddl.CropScaleRandom(in2d, [1.0, 1.0], "nearest", "foo")
    eddl.CutoutRandom(in2d, [1.0, 1.0], [1.0, 1.0])
    eddl.CutoutRandom(in2d, [1.0, 1.0], [1.0, 1.0], 0.0)
    eddl.CutoutRandom(in2d, [1.0, 1.0], [1.0, 1.0], 0.0, "foo")


def test_losses():
    eddl.getLoss("mse")


def test_metrics():
    eddl.getMetric("mse")


def test_merge_layers():
    in_1 = eddl.Input([16])
    in_2 = eddl.Input([16])
    eddl.Add([in_1, in_2])
    eddl.Add([in_1, in_2], "foo")
    eddl.Average([in_1, in_2])
    eddl.Average([in_1, in_2], "foo")
    eddl.Concat([in_1, in_2])
    eddl.Concat([in_1, in_2], "foo")
    eddl.MatMul([in_1, in_2])
    eddl.MatMul([in_1, in_2], "foo")
    eddl.Maximum([in_1, in_2])
    eddl.Maximum([in_1, in_2], "foo")
    eddl.Minimum([in_1, in_2])
    eddl.Minimum([in_1, in_2], "foo")
    eddl.Subtract([in_1, in_2])
    eddl.Subtract([in_1, in_2], "foo")


def test_noise_layers():
    in2d = eddl.Input([16])
    eddl.GaussianNoise(in2d, 1.1)
    eddl.GaussianNoise(in2d, 1.1, "foo")


def test_normalization_layers():
    in2d = eddl.Input([16])
    eddl.BatchNormalization(in2d)
    eddl.BatchNormalization(in2d, 0.9)
    eddl.BatchNormalization(in2d, 0.9, 0.001)
    eddl.BatchNormalization(in2d, 0.9, 0.001, True)
    eddl.BatchNormalization(in2d, 0.9, 0.001, True, "foo")
    eddl.Norm(in2d)
    eddl.Norm(in2d, 0.001)
    eddl.Norm(in2d, 0.001, "foo")
    eddl.NormMax(in2d)
    eddl.NormMax(in2d, 0.001)
    eddl.NormMax(in2d, 0.001, "foo")
    eddl.NormMinMax(in2d)
    eddl.NormMinMax(in2d, 0.001)
    eddl.NormMinMax(in2d, 0.001, "foo")
    eddl.Dropout(in2d, 0.5)
    eddl.Dropout(in2d, 0.5, "foo")


def test_operator_layers():
    in_1 = eddl.Input([16])
    in_2 = eddl.Input([16])
    eddl.Abs(in_1)
    eddl.Diff(in_1, in_2)
    eddl.Diff(in_1, 1.0)
    eddl.Diff(1.0, in_1)
    eddl.Div(in_1, in_2)
    eddl.Div(in_1, 1.0)
    eddl.Div(1.0, in_1)
    eddl.Exp(in_1)
    eddl.Log(in_1)
    eddl.Log2(in_1)
    eddl.Log10(in_1)
    eddl.Mult(in_1, in_2)
    eddl.Mult(in_1, 1.0)
    eddl.Mult(1.0, in_1)
    eddl.Pow(in_1, in_2)
    eddl.Pow(in_1, 1.0)
    eddl.Sqrt(in_1)
    eddl.Sum(in_1, in_2)
    eddl.Sum(in_1, 1.0)
    eddl.Sum(1.0, in_1)


def test_reduction_layers():
    in2d = eddl.Input([16])
    eddl.ReduceMean(in2d)
    eddl.ReduceMean(in2d, [0])
    eddl.ReduceMean(in2d, [0], False)
    eddl.ReduceVar(in2d)
    eddl.ReduceVar(in2d, [0])
    eddl.ReduceVar(in2d, [0], False)
    eddl.ReduceSum(in2d)
    eddl.ReduceSum(in2d, [0])
    eddl.ReduceSum(in2d, [0], False)
    eddl.ReduceMax(in2d)
    eddl.ReduceMax(in2d, [0])
    eddl.ReduceMax(in2d, [0], False)
    eddl.ReduceMin(in2d)
    eddl.ReduceMin(in2d, [0])
    eddl.ReduceMin(in2d, [0], False)


def test_generator_layers():
    eddl.GaussGenerator(0.0, 1.0, [10])
    eddl.UniformGenerator(0.0, 5.0, [10])


def test_optimizers():
    eddl.adadelta(0.01, 0.9, 0.0001, 0.0)
    eddl.adam()
    eddl.adam(0.01)
    eddl.adam(0.01, 0.9)
    eddl.adam(0.01, 0.9, 0.999)
    eddl.adam(0.01, 0.9, 0.999, 0.0001)
    eddl.adam(0.01, 0.9, 0.999, 0.0001, 0.0)
    eddl.adam(0.01, 0.9, 0.999, 0.0001, 0.0, False)
    eddl.adagrad(0.01, 0.0001, 0.0)
    eddl.adamax(0.01, 0.9, 0.999, 0.0001, 0.0)
    eddl.nadam(0.01, 0.9, 0.999, 0.0001, 0.0)
    eddl.rmsprop()
    eddl.rmsprop(0.01)
    eddl.rmsprop(0.01, 0.9)
    eddl.rmsprop(0.01, 0.9, 0.0001)
    eddl.rmsprop(0.01, 0.9, 0.0001, 0.0)
    eddl.sgd()
    eddl.sgd(0.01)
    eddl.sgd(0.01, 0.0)
    eddl.sgd(0.01, 0.0, 0.0)
    eddl.sgd(0.01, 0.0, 0.0, False)


def test_pooling_layers():
    in4d = eddl.Input([3, 16, 16])
    eddl.AveragePool(in4d)
    eddl.AveragePool(in4d, [2, 2])
    eddl.AveragePool(in4d, [2, 2], [2, 2])
    eddl.AveragePool(in4d, [2, 2], [2, 2], "none")
    eddl.AveragePool(in4d, [2, 2], [2, 2], "none", "foo")
    eddl.MaxPool(in4d)
    eddl.MaxPool(in4d, [2, 2])
    eddl.MaxPool(in4d, [2, 2], [2, 2])
    eddl.MaxPool(in4d, [2, 2], [2, 2], "none")
    eddl.MaxPool(in4d, [2, 2], [2, 2], "none", "foo")


def test_recurrent_layers():
    in2d = eddl.Input([16])
    eddl.RNN(in2d, 1, 1)
    eddl.RNN(in2d, 1, 1, True)
    eddl.RNN(in2d, 1, 1, True, 0.0)
    eddl.RNN(in2d, 1, 1, True, 0.0, False)
    eddl.RNN(in2d, 1, 1, True, 0.0, False, "foo")
    eddl.LSTM(in2d, 1, 1)
    eddl.LSTM(in2d, 1, 1, True)
    eddl.LSTM(in2d, 1, 1, True, 0.0)
    eddl.LSTM(in2d, 1, 1, True, 0.0, False)
    eddl.LSTM(in2d, 1, 1, True, 0.0, False, "foo")


def test_initializers():
    in2d = eddl.Input([16])
    eddl.GlorotNormal(in2d)
    eddl.GlorotNormal(in2d, 1234)
    eddl.GlorotUniform(in2d)
    eddl.GlorotUniform(in2d, 1234)
    eddl.RandomNormal(in2d)
    eddl.RandomNormal(in2d, 0.0)
    eddl.RandomNormal(in2d, 0.0, 0.1)
    eddl.RandomNormal(in2d, 0.0, 0.1, 1234)
    eddl.RandomUniform(in2d)
    eddl.RandomUniform(in2d, 0.0)
    eddl.RandomUniform(in2d, 0.0, 0.1)
    eddl.RandomUniform(in2d, 0.0, 0.1, 1234)
    eddl.Constant(in2d)
    eddl.Constant(in2d, 0.1)


def test_regularizers():
    in2d = eddl.Input([16])
    eddl.L2(in2d, 0.001)
    eddl.L1(in2d, 0.001)
    eddl.L1L2(in2d, 0.001, 0.001)


def test_computing_services():
    eddl.CS_CPU()
    eddl.CS_CPU(1)
    eddl.CS_GPU([1])
    eddl.CS_GPU([1], 1)
    eddl.CS_FGPA([1])
    eddl.CS_FGPA([1], 1)
    eddl.CS_COMPSS("foo.xml")