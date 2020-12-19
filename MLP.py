import numpy
import scipy.special


class MLP:

    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):

        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        self.learning_rate = learning_rate

        self.weights_input_hidden = numpy.random.normal(0.0, (self.hidden_nodes ** -0.5),
                                                        (self.hidden_nodes, self.input_nodes))
        self.weights_hidden_output = numpy.random.normal(0.0, (self.output_nodes ** -0.5),
                                                         (self.output_nodes, self.hidden_nodes))

    def train(self, inputs_list, targets_list):

        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.weights_input_hidden, inputs)
        hidden_outputs = scipy.special.expit(hidden_inputs)

        output_inputs = numpy.dot(self.weights_hidden_output, hidden_outputs)
        outputs = scipy.special.expit(output_inputs)

        output_errors = targets - outputs
        hidden_errors = numpy.dot(self.weights_hidden_output.T, output_errors)

        self.weights_hidden_output += self.learning_rate * numpy.dot((output_errors * outputs * (1.0 - outputs)),
                                                                     numpy.transpose(hidden_outputs))
        self.weights_input_hidden += self.learning_rate * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))

    def query(self, inputs_list):
        inputs = numpy.array(inputs_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.weights_input_hidden, inputs)
        hidden_outputs = scipy.special.expit(hidden_inputs)

        output_inputs = numpy.dot(self.weights_hidden_output, hidden_outputs)
        outputs = scipy.special.expit(output_inputs)

        return outputs
