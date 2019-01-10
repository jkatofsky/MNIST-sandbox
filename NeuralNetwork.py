import numpy
import scipy.special


class NeuralNetwork:

    def __init__(self, inputNodes, hiddenNodes, outputNodes, learningRate):

        self.inputNodes = inputNodes
        self.hiddenNodes = hiddenNodes
        self.outputNodes = outputNodes

        self.learningRate = learningRate

        self.weightsInputHidden = numpy.random.normal(0.0, (self.hiddenNodes ** -0.5),
                                                      (self.hiddenNodes, self.inputNodes))
        self.weightsHiddenOutput = numpy.random.normal(0.0, (self.outputNodes ** -0.5),
                                                       (self.outputNodes, self.hiddenNodes))

    def train(self, inputsList, targetsList):

        inputs = numpy.array(inputsList, ndmin=2).T
        targets = numpy.array(targetsList, ndmin=2).T

        hiddenInputs = numpy.dot(self.weightsInputHidden, inputs)
        hiddenOutputs = scipy.special.expit(hiddenInputs)

        outputInputs = numpy.dot(self.weightsHiddenOutput, hiddenOutputs)
        outputs = scipy.special.expit(outputInputs)

        outputErrors = targets - outputs
        hiddenErrors = numpy.dot(self.weightsHiddenOutput.T, outputErrors)

        self.weightsHiddenOutput += self.learningRate * numpy.dot((outputErrors * outputs * (1.0 - outputs)),
                                                                  numpy.transpose(hiddenOutputs))
        self.weightsInputHidden += self.learningRate * numpy.dot((hiddenErrors * hiddenOutputs * (1.0 - hiddenOutputs)), numpy.transpose(inputs))


    def query(self, inputsList):
        inputs = numpy.array(inputsList, ndmin=2).T

        hiddenInputs = numpy.dot(self.weightsInputHidden, inputs)
        hiddenOutputs = scipy.special.expit(hiddenInputs)

        outputInputs = numpy.dot(self.weightsHiddenOutput, hiddenOutputs)
        outputs = scipy.special.expit(outputInputs)

        return outputs
