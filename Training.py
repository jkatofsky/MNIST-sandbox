from tkinter import *
from MLP import MLP
import numpy as np
import random


class Training:

    def __init__(self, parent):

        with open("training-data.csv", "r") as data_fp:
            self.data = data_fp.readlines()[1:]

        self.training_frame = Frame(parent, borderwidth=2, relief=RIDGE)
        self.training_frame.pack()

        self.input_frame = Frame(self.training_frame)
        self.input_frame.pack(side=TOP)

        self.batch_input_label = Label(self.input_frame, text="Batch Size:")
        self.batch_input_label.pack(side=LEFT)
        self.batch_input = Entry(self.input_frame, width=5)
        self.batch_input.insert(END, "10000")
        self.batch_input.config(state=DISABLED)
        self.batch_input.pack(side=LEFT)

        self.train_button = Button(self.input_frame, text="TRAIN NETWORK",
                                   command=parent.train_mlp, state=DISABLED)
        self.train_button.pack(side=LEFT)

        self.info_frame = Frame(self.training_frame)
        self.info_frame.pack(side=BOTTOM)

        self.info_label = Label(self.info_frame, text="N/A")
        self.info_label.pack(side=BOTTOM)

    # TODO: lots of magic numbers here
    def train_mlp(self, mlp):
        try:

            target = int(self.batch_input.get())

            data = [random.choice(self.data) for _ in range(target)]

            for entry in data:

                image_vals = entry.split(",")
                inputs = (np.asfarray(image_vals[:-1]) / 255.0 * 0.99) + 0.01
                targets = np.zeros(10) + 0.01
                targets[int(image_vals[-1])] = 0.99
                mlp.train(inputs, targets)

                self.iterations += 1

            self.update_training_info()

        except ValueError:
            pass

    def activate(self):
        self.iterations = 0
        self.batch_input.config(state=NORMAL)
        self.train_button.config(state=NORMAL)
        self.update_training_info()

    def update_training_info(self):
        string = "Total Training Iterations: " + str(self.iterations)
        self.info_label.config(text=string)
