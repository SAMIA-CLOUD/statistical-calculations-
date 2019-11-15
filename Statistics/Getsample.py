import random


def getSample(data, sample_size):
    random_values = random.sample(data, k=sample_size - 1)
    return random_values
