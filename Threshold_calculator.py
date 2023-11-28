#!/usr/bin/env python3
"""
    We Used this to determine our threshold which is
    based on the highest and lowest score one can get
"""
from numpy.random import randint
from typing import List
import math


def squared_difference(scores: list, mean: float):
    """
        Finds the Squared difference
        :param scores:
        :param mean:
        :return:
    """
    return round((sum((x - mean) ** 2 for x in scores)), 2)


def generate_scores(min_score: int, max_score: int, no_of_scores: int) -> List:
    """
        Generates random scores based on the highest and lowest scores
        :param min_score:
        :param max_score:
        :param no_of_scores:
        :return: List of scores
    """
    return randint(min_score, max_score, no_of_scores)


def find_mean(scores: list) -> float:
    """
        Finds the mean of the scores
        :param scores:
        :return:
    """
    return sum(scores)/len(scores)


if __name__ == '__main__':
    values: list = generate_scores(18, 90, 100)
    mean_score: float = find_mean(values)
    sq_diff = squared_difference(values, mean_score)
    variance = round((sq_diff/mean_score), 2)
    stand_dev = round((math.sqrt(variance)), 2)

    print(values)

    print(f'Mean score: {mean_score}\n'
          f'Squared Difference: {sq_diff}\n'
          f'Variance: {variance}\n'
          f'Standard Deviation: {stand_dev}\n'
          f'Mean+SD: {round((mean_score+stand_dev), 2)}\n'
          f'Mean-SD: {round((mean_score-stand_dev), 2)}')
