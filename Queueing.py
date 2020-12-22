from tkinter import *
from MLP import *
import numpy as np


class Queueing:

    def __init__(self, parent):

        self.queueing_frame = Frame(parent, borderwidth=2, relief=RIDGE)
        self.queueing_frame.pack()

        self.input_frame = Frame(self.queueing_frame)
        self.input_frame.pack(side=TOP)

        self.queue_drawing_button = Button(self.input_frame, text="QUEUE DRAWN DIGIT",
                                           command=parent.queue_drawing_in_mlp, state=DISABLED)
        self.queue_drawing_button.pack(side=LEFT)

        self.prediction_eval_label = Label(self.input_frame, text="Is the prediction correct?")
        self.prediction_eval_label.pack(side=LEFT)
        self.radio_value = IntVar()
        self.prediction_eval_yes = Radiobutton(self.input_frame, text="Yes",
                                               variable=self.radio_value, value=1, state=DISABLED)
        self.prediction_eval_yes.pack(side=LEFT)
        self.prediction_eval = Radiobutton(self.input_frame, text="No",
                                           variable=self.radio_value, value=0, state=DISABLED)
        self.prediction_eval.pack(side=LEFT)
        self.send_eval_button = Button(self.input_frame, text="SEND EVALUATION", command=self.send_evaluation, state=DISABLED)
        self.send_eval_button.pack(side=LEFT)

        self.info_frame = Frame(self.queueing_frame)
        self.info_frame.pack(side=BOTTOM)

        self.output_label = Label(self.info_frame, text="N/A")
        self.output_label.pack()
        self.eval_label = Label(self.info_frame, text="N/A")
        self.eval_label.pack()

    def activate(self):
        self.digits_queued = 0
        self.predictions_correct = 0
        self.queue_drawing_button.config(state=NORMAL)
        self.disable_evaluation()
        self.update_evaluation_string()
        self.update_output_string(None)

    def enable_evaluation(self):
        self.prediction_eval_yes.config(state=NORMAL)
        self.prediction_eval.config(state=NORMAL)
        self.send_eval_button.config(state=NORMAL)

    def disable_evaluation(self):
        self.prediction_eval_yes.config(state=DISABLED)
        self.prediction_eval.config(state=DISABLED)
        self.send_eval_button.config(state=DISABLED)

    def get_output_string(self, raw_outputs):
        outputs = [output[0] for output in raw_outputs.tolist()]
        precent_dict = {}
        for i in range(len(outputs)):
            precent_dict[str(i)] = round(outputs[i] / sum(outputs) * 100, 2)
        sorted_digits = sorted(precent_dict, key=precent_dict.get, reverse=True)
        string = ""
        # TODO: use join()
        for i in range(len(sorted_digits)):
            string += sorted_digits[i] + " (" + str(precent_dict[sorted_digits[i]]) + "%)"
            if i < len(sorted_digits) - 1:
                string += ", "
        return string

    def update_output_string(self, outputs):
        if outputs is None:
            string = "N/A"
        else:
            string = "Ordered Digit Predictions and % Certainties: " + self.get_output_string(outputs)
        self.output_label.config(text=string)

    #TODO: cleanup
    def update_evaluation_string(self):
        string = "Predictions Correct: " + str(self.predictions_correct) + "/" + str(self.digits_queued)
        if self.digits_queued != 0:
            percentage = round(((self.predictions_correct / self.digits_queued) * 100), 2)
        else:
            percentage = "N/A"
        string += " (" + str(percentage) + "%)"
        self.eval_label.config(text=string)

    def send_evaluation(self):
        self.digits_queued += 1
        self.predictions_correct += self.radio_value.get()
        self.update_evaluation_string()
        self.disable_evaluation()

    def queue_drawing(self, mlp, image_vals):
        image_vals = [(255 - value) for value in image_vals]
        print(image_vals)
        inputs = (np.asfarray(image_vals) / 255.0 * 0.99) + 0.01
        print(inputs)
        outputs = mlp.query(inputs)
        print(outputs)
        self.update_output_string(outputs)
        self.enable_evaluation()
