'''
There is a biased coin that returns
    HEAD : 80% of times
    TAIL : 20% of times

This program generates the results
of a fair coin from biased coin using
John Von Neumann method
'''

import random

BIAS_PARAMETER = 0.8
NUMBER_OF_TRIALS = 100000

def biased_coin():
    '''
    This function returns HEAD or TAIL
    depending upon the BIAS_PARAMETER
    '''
    random_number = random.random()

    if random_number < BIAS_PARAMETER :
        return "HEAD"
    return "TAIL"

def experiment_with(coin_function, number_of_trials):
    '''
    This function tosses the coin using coin_function and
    returns the outcome in form of a freq_data dictionary
    '''
    freq_data ={}
    for _ in range(number_of_trials):
        outcome = coin_function()
        if outcome in freq_data:
            freq_data[outcome] += 1
        else:
            freq_data[outcome] = 1
    return freq_data

def von_neumann_method():
    '''
    1. Toss the coin twice
    2. If the results match, start over forgetting both results
    3. if the results differ use the first result forgetting the rest
    '''
    toss1 = biased_coin()
    toss2 = biased_coin()

    if toss1 == toss2 :
        von_neumann_method()
        return "INCONCLUSIVE"
    return toss1

print("Experiment with biased coin")
result_1 = experiment_with(biased_coin, NUMBER_OF_TRIALS)
print(result_1)
print("Bias : ", result_1["HEAD"]/NUMBER_OF_TRIALS)
print("\n")
print("Experiment with biased coin using von neumann method")
result_2 = experiment_with(von_neumann_method, NUMBER_OF_TRIALS)
print(result_2)
print("Bias : ", result_2["HEAD"]/(result_2["HEAD"]+result_2["TAIL"]))
