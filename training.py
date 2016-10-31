

class Training:

    """Trains the perceptron using
    An image
    the perceptron and its methods
    the correct output
    an alfa value.. the learing rate.
    the wanted output."""

    def __init__(self, image, perceptron, corr_output):
        self.image = image
        self.perceptron = perceptron
        self.corr_output = corr_output
        self.alfa = 0.05
        if self.corr_output == self.perceptron.get_mood():
            self.wanted_value = 1
        else:
            self.wanted_value = 0


    def train(self):
        """Controlls the training. Gets the new weights and change from the old."""
        new_weights = self.calc_new_weights()
        self.perceptron.change_weight(new_weights)


    def calc_error(self):
        """Calculates the error between output and correct."""
        error = self.wanted_value - self.perceptron.get_output()

        return error


    def calc_new_weights(self):
        """Calculates the new weights for every weight.
        Input: None
        Output: The new updated weight list."""
        new_weight_arr = []
        error = self.calc_error()

        for i in range(len(self.perceptron.get_weights())):
            prel = []
            for j in range(len(self.perceptron.get_weight_row(i))):
                delta_w = self.alfa * error * (self.image.get_col(i,j)/31)
                new_weight = self.perceptron.get_spec_weight(i, j) + delta_w
                prel.append(new_weight)

            new_weight_arr.append(prel)

        return new_weight_arr