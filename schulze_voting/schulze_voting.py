# -*- coding: utf-8 -*-

# MIT License
#
# Copyright (c) 2018 Fabian Wenzelmann
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from collections import defaultdict


class SchulzeVote(object):
    """Class for a Schulze votingself.

    It contains the weight of a voter (default 1) and the ranking. That is
    if there are n options to vote for for each option it contains the ranking
    position.

    Attributes:
        ranking (list of int): For each option the position in the ranking.
        weight (int): Weight of the voter (how many votes a single voter has).

    Example:
        Suppose that there are 4 options to vote for (A, B, C and D). The voter
        wants to rank A > B = D > C. This can be created with:

        >>> vote = SchulzeVote([0, 1, 2, 1])
    """
    def __init__(self, ranking, weight=1):
        self.ranking = ranking
        self.weight = weight


class SchulzeRes(object):
    """Class that contains all (intermediate) results for the Schulze voting.

    For details see <https://en.wikipedia.org/wiki/Schulze_method>.

    This result contains the matrices d and p as well as the computed ranking.
    A result is generally computed by the evaluate_schulze function.

    Attributes:
        d (list of list of int): The matrix d
        p (list of list of int): The matrix p
        candidate_wins (list of list of int): A list describing which options
            win against the other options. The first list contains all options
            that are ranked highest, the next list all entries ranked second
            best and so on.
    """
    def __init__(self):
        self.d = None
        self.p = None
        self.candidate_wins = None


def compute_d(votes, n):
    """Compute the matrix d given the Schulze votes.

    Args:
        votes (list of SchulzeVote): All votes to compute the matrix from.
        n (int): The number of options in the vote. All rankings in votes must
            have length n. This is not checked, however an IndexError may be
            raised if rankings are too short.

        Returns:
            list of list of int: The matrix d.

    """
    res = [ [0 for _ in range(n)] for _ in range(n) ]
    for vote in votes:
        w = vote.weight
        ranking = vote.ranking
        for i in range(n):
            for j in range(i+1, n):
                if ranking[i] < ranking[j]:
                    res[i][j] += w
                elif ranking[j] < ranking[i]:
                    res[j][i] += w
    return res


def compute_p(d, n):
    """Compute the matrix p given the matrix d.

    Args:
        d (list of list of int): The matrix d.
        n (int): Number of options in the vote.

    Returns:
        list of list of int: The matrix p.
    """
    res = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                if d[i][j] > d[j][i]:
                    res[i][j] = d[i][j]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if i == k or j == k:
                    continue
                res[j][k] = max(res[j][k], min(res[j][i], res[i][k]))
    return res


def rank_p(p, n):
    """Rank the matrix p and rank all options as described in SchulzeRes.

    Inspired by <https://github.com/mgp/schulze-method/blob/master/schulze.py>.

    Args:
        p (list of list of int): The matrix p.
        n (int): Number of options in the vote.

    Returns:
        list of list of int: A list describing which options
            win against the other options. The first list contains all options
            that are ranked highest, the next list all entries ranked second
            best and so on.
    """
    candidate_wins = defaultdict(list)
    for i in range(n):
        num_wins = 0
        for j in range(n):
            if i == j:
                continue
            if p[i][j] > p[j][i]:
                num_wins += 1
        candidate_wins[num_wins].append(i)
    sorted_wins = sorted(candidate_wins.keys(), reverse=True)
    return [candidate_wins[key] for key in sorted_wins]


def evaluate_schulze(votes, n):
    """Compute the matrices d and p, rank the matrix p and return a SchulzeRes.

    Args:
        votes (list of SchulzeVote): All votes to compute the matrix from.
        n (int): The number of options in the vote. All rankings in votes must
            have length n. This is not checked, however an IndexError may be
            raised if rankings are too short.

    Returns:
        SchulzeRes: All (intermediate) results for the voting.
    """
    res = SchulzeRes()
    res.d = compute_d(votes, n)
    res.p = compute_p(res.d, n)
    res.candidate_wins = rank_p(res.p, n)
    return res
