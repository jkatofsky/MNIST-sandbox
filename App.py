from tkinter import *
from NeuralNetwork import *
from Drawing import *
from NeuralNetworkOptions import *
from NeuralNetworkTraining import *
from NeuralNetworkQueueing import *

# General bugfixing
# The output is still very finnicky and nowhere near as accurate as the training dataset. Something seems off.
# Possible points of error:
# My drawing functionality creates pixel values that are very removed from the training data.
# My way of handling the output values (and perhaps how it pertains to their scientific notaion when they are in a numpy array) means that I'm displaying them incorrectly, and that the network is actually giving solid output

# General GUI Ideas:
# Make more responsive - scroll bars for some text? for the whole window? pop-ups for errors?
# At the least, make it so the window doesn't need to strech greatly to display the output

# NeuralNetwork:
# Give the ability to have more than one hidden layers
# Generally rethink the structure
# Don't use numpy stuff unecessarily


class App(Tk):

    def __init__(self, parent):

        Tk.__init__(self, parent)

        self.title("Josh's Number-Recognizing Neural Network")

        self.neuralNetwork = None

        self.drawing = Drawing(self)

        self.neuralNetworkOptions = NeuralNetworkOptions(self)

        self.neuralNetworkTraining = NeuralNetworkTraining(self)

        self.neuralNetworkQueueing = NeuralNetworkQueueing(self)

        self.mainloop()

    def updateNeuralNetwork(self):
        tempNeuralNetwork = self.neuralNetworkOptions.getNeuralNetwork()
        if tempNeuralNetwork:
            self.neuralNetwork = tempNeuralNetwork
            self.neuralNetworkOptions.updateNeuralNetworkOptionsString(self.neuralNetwork)
            self.neuralNetworkTraining.activate()
            self.neuralNetworkQueueing.activate()

    def trainNeuralNetwork(self):
        self.neuralNetworkTraining.trainNeuralNetwork(self.neuralNetwork)

    def queueDrawnDigitInNeuralNetwork(self):
        imagePixels = self.drawing.getDrawingPixelList()
        self.neuralNetworkQueueing.queueDrawnDigit(self.neuralNetwork, imagePixels)


if __name__ == "__main__":
    app = App(None)
