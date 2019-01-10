from tkinter import *
from NeuralNetwork import *


class NeuralNetworkOptions:

    def __init__(self, parent):

        self.nnOptionsFrame = Frame(parent, borderwidth=2, relief=RIDGE)
        self.nnOptionsFrame.pack()

        self.inputFrame = Frame(self.nnOptionsFrame)
        self.inputFrame.pack(side=TOP)

        self.learningRateInputLabel = Label(self.inputFrame, text="Learning Rate:")
        self.learningRateInputLabel.pack(side=LEFT)
        self.learningRateInput = Entry(self.inputFrame, width=5)
        self.learningRateInput.insert(END, "0.3")
        self.learningRateInput.pack(side=LEFT)

        self.hiddenNodesInputLabel = Label(self.inputFrame, text="Hidden Nodes:")
        self.hiddenNodesInputLabel.pack(side=LEFT)
        self.hiddenNodesInput = Entry(self.inputFrame, width=5)
        self.hiddenNodesInput.insert(END, "100")
        self.hiddenNodesInput.pack(side=LEFT)

        self.generateNetworkButton = Button(self.inputFrame, text="GENERATE NETWORK",
                                            command=parent.updateNeuralNetwork)
        self.generateNetworkButton.pack(side=LEFT)

        self.infoFrame = Frame(self.nnOptionsFrame)
        self.infoFrame.pack(side=BOTTOM)
        self.infoString = Label(self.infoFrame, text="N/A")
        self.infoString.pack(side=BOTTOM)

    def getNeuralNetwork(self):
        try:
            hiddenNodes = int(self.hiddenNodesInput.get())
            learningRate = float(self.learningRateInput.get())
            return NeuralNetwork(inputNodes=784, hiddenNodes=hiddenNodes,
                                 outputNodes=10, learningRate=learningRate)
        except ValueError:
            return None

    def updateNeuralNetworkOptionsString(self, neuralNetwork):
        string = "Current Learning Rate: " + str(neuralNetwork.learningRate)
        string += " | Current Hidden Nodes: " + str(neuralNetwork.hiddenNodes)
        self.infoString.config(text=string)
