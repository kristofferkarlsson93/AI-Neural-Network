#!/usr/bin/env python3
import sys
import random
import time
from image import Image
from perceptron import Perceptron
from training import Training


def get_image_info(filename):
    """Reads a file and returns a 2D-list with the important info from the file.
    The unimportant information is ignored
    Input: a filename (str)
    Output: 2D-list of the pixel values"""
    f = open(filename)
    content = []
    for line in f.readlines():
        if line[0] != "#":
            line = line.strip()
            line = line.split()
            if len(line) > 0:
                if len(line[0]) <= 2:
                    for i in range(len(line)):
                        line[i] = int(line[i])
                    content.append(line)
    f.close()
    return content


def img_create(pix_list):
    """Creates pictures out of the pictures and stores them as objekts in a list.
    Input: a 2D-list of pixel values
    Output: a list of objects created in a 20x20 grid from the pixels"""
    result = []
    start = 0
    stop = 20
    for i in range(len(pix_list)//20):
        prel = []
        for j in range(start, stop):
            prel.append(pix_list[j])
        start += 20
        stop += 20
        image = Image(prel)
        result.append(image)

    return result


def get_facit_info(filename):
    """Reads from a file and returns a list of all information in the file,
    which is the correct answers.
    Input: Filename (str)
    Output: A list."""
    f = open(filename)
    content = []
    for line in f.readlines():
        if line[0] != "#" and len(line) > 0:
            line = line.strip()
            line = line.split()
            line[1] = int(line[1])
            content.append(line[1])
    f.close()

    return content


def create_weights():
    """Creates a 2D-list of randomised weights between 0 and 1.
    Input: None
    Output a 2D-list of weights"""
    result = []
    for i in range(20):
        prel = []
        for j in range(20):
            prel.append(random.random())
        result.append(prel)

    return result


def get_winner(perceptron_array):
    """Returns the perceptron with the greatest output.
    Input: A list of perceptron-objects
    Output: The perceptron with the highest output."""
    res = float()
    winner = 0
    for i in range(len(perceptron_array)):
        output = perceptron_array[i].get_output()
        if output > res:
            res = output
            winner = perceptron_array[i].get_mood()

    return winner


def calc_points(guesses, corr):
    """Checks if the guessed perceptron is the correct one. If so, point goes up by one.
    Input: The guessed perceptrons number
    Output: The number of points (correct guesses"""
    points = 0
    for i in range(len(guesses)):
        if guesses[i] == corr[i]:
            points += 1

    return points

def print_func(result_arr):
    """Prints in sys.stdout"""
    for i in range(len(result_arr)):
        sys.stdout.write("Image%i %i \n" % (i + 1, result_arr[i]))

# Reads the filenames from the Command Prompt.
training_file = sys.argv[1]
facit_file = sys.argv[2]
test_file = sys.argv[3]
test_facit_file = sys.argv[4]

# extracts and oganizes the information from the files given.
training = get_image_info(training_file)
facit = get_facit_info(facit_file)
test = get_image_info(test_file)
test_facit = get_facit_info(test_facit_file)
image_array = img_create(training)
test_image_array = img_create(test)

# Creating four weight lists, one for every perceptron.
happy_weights = create_weights()
sad_weights = create_weights()
mischievous_weights = create_weights()
angry_weights = create_weights()

# Creating the perceptrons, defining there mood and puts them in a list.
happy_p = Perceptron(happy_weights, 1)
sad_p = Perceptron(sad_weights, 2)
mischievous_p = Perceptron(mischievous_weights, 3)
angry_p = Perceptron(angry_weights, 4)
perceptron_array = [happy_p, sad_p, mischievous_p, angry_p]

# The training starts.
percentage = 0
# Trains as long as the score is lower than 75%
while percentage < 0.75:
    print("Training...")
    total_training_result = []
    for i in range(len(image_array)):
        for j in range(len(perceptron_array)):
            # Calculates the output for every perceptron on every image, and trains it.
            perceptron_array[j].activate_1(image_array[i])

            session = Training(image_array[i], perceptron_array[j], facit[i])
            session.train()
        # Look wich perceptron that was most active.
        winner = get_winner(perceptron_array)
        total_training_result.append(winner)

    # Calculates the percentage of correct answers.
    percentage = calc_points(total_training_result, facit)
    percentage = percentage / len(image_array)

    print("I got %.2f percent correct this training round." %(percentage * 100))
    time.sleep(1)

print("Let´s do the test!")
print ("________________________________")
time.sleep(1)

# The test starts.
test_result = []
for k in range(len(test_image_array)):
    for l in range(len(perceptron_array)):
        # Every perceptron react to every image.
        perceptron_array[l].activate_1(test_image_array[k])

    # Check to see wich perceptron was most active.
    test_winner = get_winner(perceptron_array)
    test_result.append(test_winner)

# Prints the finals score.
final_score = calc_points(test_result, test_facit)
print_func(test_result)
print(final_score)
