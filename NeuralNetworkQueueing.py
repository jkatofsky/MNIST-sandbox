from tkinter import *
from NeuralNetwork import *
import numpy as numpy


class NeuralNetworkQueueing:

    def __init__(self, parent):

        self.nnQueueingFrame = Frame(parent, borderwidth=2, relief=RIDGE)
        self.nnQueueingFrame.pack()

        self.inputFrame = Frame(self.nnQueueingFrame)
        self.inputFrame.pack(side=TOP)

        self.queueDrawingButton = Button(self.inputFrame, text="QUEUE DRAWN DIGIT",
                                         command=parent.queueDrawnDigitInNeuralNetwork, state=DISABLED)
        self.queueDrawingButton.pack(side=LEFT)

        self.predictionEvaluationLabel = Label(self.inputFrame, text="Is the prediction correct?")
        self.predictionEvaluationLabel.pack(side=LEFT)
        self.radioValue = IntVar()
        self.predictionEvaluationYes = Radiobutton(self.inputFrame, text="Yes",
                                                   variable=self.radioValue, value=1, state=DISABLED)
        self.predictionEvaluationYes.pack(side=LEFT)
        self.predictionEvaluationNo = Radiobutton(self.inputFrame, text="No",
                                                  variable=self.radioValue, value=0, state=DISABLED)
        self.predictionEvaluationNo.pack(side=LEFT)
        self.sendEvaluationButton = Button(self.inputFrame, text="SEND EVALUATION", command=self.sendEvaluation, state=DISABLED)
        self.sendEvaluationButton.pack(side=LEFT)

        self.infoFrame = Frame(self.nnQueueingFrame)
        self.infoFrame.pack(side=BOTTOM)

        self.outputsString = Label(self.infoFrame, text="N/A")
        self.outputsString.pack()
        self.evaluationString = Label(self.infoFrame, text="N/A")
        self.evaluationString.pack()

    def activate(self):
        self.totalDigitsQueued = 0
        self.totalPredictionsCorrect = 0
        self.queueDrawingButton.config(state='normal')
        self.disableEvaluation()
        self.updateEvaluationString()
        self.updateOutputString(None)

    def enableEvaluation(self):
        self.predictionEvaluationYes.config(state='normal')
        self.predictionEvaluationNo.config(state='normal')
        self.sendEvaluationButton.config(state='normal')

    def disableEvaluation(self):
        self.predictionEvaluationYes.config(state=DISABLED)
        self.predictionEvaluationNo.config(state=DISABLED)
        self.sendEvaluationButton.config(state=DISABLED)

    def getOutputString(self, rawOutputs):
        outputs = [output[0] for output in rawOutputs.tolist()]
        percentsDictionary = {}
        for i in range(len(outputs)):
            percentsDictionary[str(i)] = round(outputs[i] / sum(outputs) * 100, 2)
        sortedDigits = sorted(percentsDictionary, key=percentsDictionary.get, reverse=True)
        string = ""
        for i in range(len(sortedDigits)):
            string += sortedDigits[i] + " (" + str(percentsDictionary[sortedDigits[i]]) + "%)"
            if i < len(sortedDigits) - 1:
                string += ", "
        return string

    def updateOutputString(self, outputs):
        if outputs is None:
            string = "N/A"
        else:
            string = "Ordered Digit Predictions and % Certainties: " + self.getOutputString(outputs)
        self.outputsString.config(text=string)

    def updateEvaluationString(self):
        string = "Predictions Correct: " + str(self.totalPredictionsCorrect) + "/" + str(self.totalDigitsQueued)
        if self.totalDigitsQueued is not 0:
            percentage = round(((self.totalPredictionsCorrect / self.totalDigitsQueued) * 100), 2)
        else:
            percentage = "N/A"
        string += " (" + str(percentage) + "%)"
        self.evaluationString.config(text=string)

    def sendEvaluation(self):
        self.totalDigitsQueued += 1
        self.totalPredictionsCorrect += self.radioValue.get()
        self.updateEvaluationString()
        self.disableEvaluation()

    def queueDrawnDigit(self, neuralNetwork, imageValues):
        imageValues = [(255 - value) for value in imageValues]
        print(imageValues)
        inputs = (numpy.asfarray(imageValues) / 255.0 * 0.99) + 0.01
        print(inputs)
        outputs = neuralNetwork.query(inputs)
        print(outputs)
        self.updateOutputString(outputs)
        self.enableEvaluation()
