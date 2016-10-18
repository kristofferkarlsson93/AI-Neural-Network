import math


class Perceptron:
    """Controls the perceptrons. Each percetron has:
    A weight-list
    A mood
    An Output"""


    def __init__(self, weight_arr, mood):
        self.weights = weight_arr
        self.mood = mood
        self.output = 0

    def change_weight(self, new_weight_arr):
        """Change the weight list for the perceptron-object.
        Input: 2D-list
        Output: None"""
        self.weights = new_weight_arr

    def get_weights(self):
        """Returns the weightlist"""
        return self.weights

    def get_weight_row(self, i):
        """Returns a row of weights"""
        return self.weights[i]

    def get_spec_weight(self, i, j):
        """Returns a specific column in the weight list"""
        return self.weights[i][j]

    def get_mood(self):
        """Returns the perceptrons mood"""
        return self.mood

    def get_output(self):
        """Returns the perceptrons output"""
        return self.output

    def activate_1(self, image):
        """For every pixel the function calculates the pixel times its weight."""
        result = float()
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                result += (image.get_col(i, j)/31) * self.weights[i][j]

        self.output = self.activate_2(result)


    def activate_2(self, act_1):
        """Calculates the perceptrons output.
        Input: The summed result from activate 1.
        Output: The result output."""
        x = act_1
        e = math.e
        result = 1/(1 + e **-x)
        #print (result)
        return result