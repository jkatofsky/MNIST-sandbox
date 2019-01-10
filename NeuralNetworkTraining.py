from tkinter import *
from NeuralNetwork import *
import numpy
import os
import random


class NeuralNetworkTraining:

    def __init__(self, parent):

        trainingDataFile = open(os.path.join(os.path.dirname(__file__), "trainingData.csv"), "r")
        self.trainingData = trainingDataFile.readlines()
        trainingDataFile.close()

        self.nnTrainingFrame = Frame(parent, borderwidth=2, relief=RIDGE)
        self.nnTrainingFrame.pack()

        self.inputFrame = Frame(self.nnTrainingFrame)
        self.inputFrame.pack(side=TOP)

        self.trainingOrderInputLabel = Label(self.inputFrame, text="Training Iterations Order:")
        self.trainingOrderInputLabel.pack(side=LEFT)
        self.trainingOrderInput = Entry(self.inputFrame, width=5)
        self.trainingOrderInput.insert(END, "10000")
        self.trainingOrderInput.config(state=DISABLED)
        self.trainingOrderInput.pack(side=LEFT)

        self.trainNetworkButton = Button(self.inputFrame, text="TRAIN NETWORK",
                                         command=parent.trainNeuralNetwork, state=DISABLED)
        self.trainNetworkButton.pack(side=LEFT)

        self.infoFrame = Frame(self.nnTrainingFrame)
        self.infoFrame.pack(side=BOTTOM)

        self.infoString = Label(self.infoFrame, text="N/A")
        self.infoString.pack(side=BOTTOM)

    def trainNeuralNetwork(self, neuralNetwork):
        try:

            trainingTarget = int(self.trainingOrderInput.get())

            trainingData = [random.choice(self.trainingData) for i in range(trainingTarget)]

            for entry in trainingData:

                imageValues = entry.split(",")
                inputs = (numpy.asfarray(imageValues[1:]) / 255.0 * 0.99) + 0.01
                targets = numpy.zeros(10) + 0.01
                targets[int(imageValues[0])] = 0.99
                neuralNetwork.train(inputs, targets)

                self.trainingIterations += 1

            self.updateNeuralNetworkTrainingString()

        except ValueError:
            pass

    def activate(self):
        self.trainingIterations = 0
        self.trainingOrderInput.config(state="normal")
        self.trainNetworkButton.config(state="normal")
        self.updateNeuralNetworkTrainingString()

    def updateNeuralNetworkTrainingString(self):
        string = "Total Training Iterations: " + str(self.trainingIterations)
        self.infoString.config(text=string)
