from tkinter import *
from VanillaMLP import *
from Drawing import *
from Options import *
from Training import *
from Queueing import *

# TODO
# - The output is still finnicky and far from as accurate as the training dataset. Something seems off.

# - Make GUI more responsive - scroll bars for some text? for the whole window? pop-ups for errors?
# At the least, make it so the window doesn't need to strech greatly to display the output

# - More explicitly seperate Model, View, and Controller using appropriate design patterns

# - Create README

# - Improve directory structure to mirror that of a legit Python App

class App(Tk):

    def __init__(self, parent):

        Tk.__init__(self, parent)

        self.title("Josh's Number-Recognizing Neural Network")

        self.mlp = None

        self.drawing = Drawing(self)
        self.options = Options(self)
        self.training = Training(self)
        self.queueing = Queueing(self)

        self.mainloop()

    def update_mlp(self):
        temp_mlp = self.options.getMLP()
        if temp_mlp:
            self.mlp = temp_mlp
            self.options.update_options_string(self.mlp)
            self.training.activate()
            self.queueing.activate()

    def train_mlp(self):
        self.training.train_mlp(self.mlp)

    def queue_drawing_in_mlp(self):
        pixels = self.drawing.get_pixel_list()
        self.queueing.queue_drawing(self.mlp, pixels)


if __name__ == "__main__":
    app = App(None)
