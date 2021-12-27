#!/usr/bin/env python3
import doctest
import statistics as stat

# Question 4


def compute_budget(total_budget: float, citizen_votes: list[list]) -> list[float]:
    """
    >>> compute_budget(100, [[100, 0, 0], [0, 0, 100]])
    [50.0, 0, 50.0]
    >>> compute_budget(100, [[100, 0, 0]])
    [100, 0, 0]
    >>> compute_budget(100,[[100,0,0,0],[100,0,0,0],[0,0,100,0],[0,0,0,100]])
    [50.0, 0, 25.0, 25.0]
    >>> compute_budget(100, [[100, 0, 0,0],[0, 0, 100,0],[0,100,0,0],[0, 0, 0,100]])
    [25.0, 25.0, 25.0, 25.0]
    >>> compute_budget(100, [[100, 0, 0,0],[0,100,0,0],[100, 0, 0,0],[0, 0, 0,100]])
    [50.0, 25.0, 0, 25.0]
    >>> compute_budget(100, [ [0, 100, 0],[100, 0, 0], [100, 0, 0], [0, 100, 0], [0, 100, 0], [0, 0, 100],[0, 0, 100], [0, 0, 100], [0, 0, 100], [0, 100, 0] ])
    [20.0, 40.0, 40.0]
    >>> compute_budget(100, [ [100, 0, 0],[100, 0, 0], [100, 0, 0], [100, 0, 0], [0, 100, 0], [0, 0, 100],[0, 0, 100], [0, 0, 100], [0, 0, 100], [0, 100, 0] ])
    [40.0, 20.0, 40.0]
    """
    costs_subjs = dict()
    budget = list()
    amount_citizens = len(citizen_votes)
    amount_subjects = len(citizen_votes[0])

    for s in range(amount_subjects):
        costs_subjs[s] = list()
        for vote in citizen_votes:
            costs_subjs[s].append(vote[s])

        for i in range(1, amount_citizens):
            costs_subjs[s].append(i * total_budget / amount_citizens)

        # add the median value for each subject
        budget.append(stat.median(costs_subjs[s]))
    return budget


if __name__ == "__main__":
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
