from tkinter import *
from Drawing import Drawing
from Options import Options
from Training import Training
from Queueing import Queueing
from os import path
import sys
import requests


def download_training_data_if_none():
    if path.exists('training-data.csv'):
        return
    training_data = requests.get("https://datahub.io/machine-learning/mnist_784/r/mnist_784.csv", allow_redirects=True)
    if training_data.status_code != 200:
        sys.exit(1) #TODO: error message somehow?
    with open('training-data.csv', 'w') as data_fp:
        data_fp.writelines(training_data.text)

class App(Tk):

    def __init__(self, parent):

        Tk.__init__(self, parent)

        self.title("MNIST Sandbox")

        self.mlp = None

        self.drawing = Drawing(self)
        self.options = Options(self)
        self.training = Training(self)
        self.queueing = Queueing(self)

        self.mainloop()

    def update_mlp(self):
        temp_mlp = self.options.get_mlp()
        if temp_mlp:
            self.mlp = temp_mlp
            self.options.update_options_label(self.mlp)
            self.training.activate()
            self.queueing.activate()

    def train_mlp(self):
        self.training.train_mlp(self.mlp)

    def queue_drawing_in_mlp(self):
        pixels = self.drawing.get_pixel_list()
        self.queueing.queue_drawing(self.mlp, pixels)


if __name__ == "__main__":
    download_training_data_if_none()
    app = App(None)
