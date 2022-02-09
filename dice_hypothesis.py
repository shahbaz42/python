'''
This python code is testing hypothesis
if probability getting any number on  rolling
a dice is almost equal.
'''

import random

def roll_a_dice():
    '''
    function for rolling a dice
    '''
    return random.randint(1,6)

def experiment(number_of_trials):
    '''
    This  Experiment rolls the dice and
    returns the outcome in form of a freq_data
    dictionary
    '''
    freq_data ={}
    for _ in range(number_of_trials):
        outcome = roll_a_dice()
        if outcome in freq_data:
            freq_data[outcome] += 1
        else:
            freq_data[outcome] = 1
    return freq_data

def calculate_probability(freq_data):
    '''
    This function takes in a frequency data dictionary
    and generates a probability dictionary.
    '''
    number_of_trials = 0
    probability_data = {}

    for outcome in freq_data:
        number_of_trials += freq_data[outcome]
    for outcome in freq_data:
        probability_data[outcome] = freq_data[outcome]/number_of_trials

    return probability_data

freq_data_1 = experiment(10000)
print(calculate_probability(freq_data_1))
