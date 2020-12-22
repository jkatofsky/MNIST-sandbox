from tkinter import *
from MLP import MLP


class Options:

    def __init__(self, parent):

        self.options_frame = Frame(parent, borderwidth=2, relief=RIDGE)
        self.options_frame.pack()

        self.input_frame = Frame(self.options_frame)
        self.input_frame.pack(side=TOP)

        self.learning_rate_input_label = Label(self.input_frame, text="Learning Rate:")
        self.learning_rate_input_label.pack(side=LEFT)
        self.learning_rate_input = Entry(self.input_frame, width=5)
        self.learning_rate_input.insert(END, "0.3")
        self.learning_rate_input.pack(side=LEFT)

        self.hidden_nodes_input_label = Label(self.input_frame, text="Hidden Nodes:")
        self.hidden_nodes_input_label.pack(side=LEFT)
        self.hidden_nodes_input = Entry(self.input_frame, width=5)
        self.hidden_nodes_input.insert(END, "100")
        self.hidden_nodes_input.pack(side=LEFT)

        self.generate_mlp_button = Button(self.input_frame, text="GENERATE NEURAL NETWORK",
                                          command=parent.update_mlp)
        self.generate_mlp_button.pack(side=LEFT)

        self.info_frame = Frame(self.options_frame)
        self.info_frame.pack(side=BOTTOM)
        self.info_label = Label(self.info_frame, text="N/A")
        self.info_label.pack(side=BOTTOM)

    def get_mlp(self):
        try:
            hidden_nodes = int(self.hidden_nodes_input.get())
            learning_rate = float(self.learning_rate_input.get())
            return MLP(input_nodes=784, hidden_nodes=hidden_nodes,
                              output_nodes=10, learning_rate=learning_rate)
        except ValueError:
            return None

    def update_options_label(self, mlp):
        string = "Current Learning Rate: " + str(mlp.learning_rate)
        string += " | Current Hidden Nodes: " + str(mlp.hidden_nodes)
        self.info_label.config(text=string)
