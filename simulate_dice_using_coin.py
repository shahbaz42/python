import random

def flip_coin():
    """
    This function randomly returns 0 or 1
    """
    return random.randint(0,1)

def dice_from_coin():
    """
    This function produces the outcomes of a
    dice using the results of a coin toss
    """
    
    binary = str(flip_coin()) + str(flip_coin()) + str(flip_coin())
    num = int(binary, 2)

    while num == 0 or num == 7 :
        binary = str(flip_coin()) + str(flip_coin()) + str(flip_coin())
        num = int(binary, 2)
    
    return num

def generate_freq_dist(experiment, number_of_trials):
    """
    This function generates frequency distribution 
    for the outcomes of an experiment.
    """
    
    dist = {}

    for _ in range(number_of_trials):
        result = experiment()

        if result in dist:
            dist[result] += 1
        else:
            dist[result] = 1
    
    return dist

print(generate_freq_dist(dice_from_coin, 100000))
