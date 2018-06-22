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
    def __init__(self, ranking, weight=1):
        self.ranking = ranking
        self.weight = weight


class SchulzeRes(object):
    def __init__(self):
        self.d = None
        self.p = None
        self.percents = None
        self.votes_required = -1
        self.n = -1


def compute_d(votes, n):
    res = [ [0 for _ in range(n)] for _ in range(n) ]
    for vote in votes:
        w = vote.weight
        ranking = vote.ranking
        for i in range(n):
            for j in range(i+1, n):
                if ranking[i] < ranking[j]:
                    res[i][j] += w
                elif ranking[j] < ranking[j]:
                    res[j][i] += w
    return res


def compute_p(d, n):
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
