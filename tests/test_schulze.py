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

from schulze_voting import *
import pytest
import sys


def test_schulze_one():
    # From <http://de.wikipedia.org/wiki/Schulze-Methode#Beispiel_1>
    v1 = SchulzeVote([0, 2, 1, 4, 3], 5)
    v2 = SchulzeVote([0, 4, 3, 1, 2], 5)
    v3 = SchulzeVote([3, 0, 4, 2, 1], 8)
    v4 = SchulzeVote([1, 2, 0, 4, 3], 3)
    v5 = SchulzeVote([1, 3, 0, 4, 2], 7)
    v6 = SchulzeVote([2, 1, 0, 3, 4], 2)
    v7 = SchulzeVote([4, 3, 1, 0, 2], 7)
    v8 = SchulzeVote([2, 1, 4, 3, 0], 8)

    r = evaluate_schulze([v1, v2, v3, v4, v5, v6, v7, v8], 5)

    assert r.d == [[0, 20, 26, 30, 22],
                   [25, 0, 16, 33, 18],
                   [19, 29, 0, 17, 24],
                   [15, 12, 28, 0, 14],
                   [23, 27, 21, 31, 0]]

    assert r.p == [[0, 28, 28, 30, 24],
                   [25, 0, 28, 33, 24],
                   [25, 29, 0, 29, 24],
                   [25, 28, 28, 0, 24],
                   [25, 28, 28, 31, 0]]

    assert r.candidate_wins == [[4], [0], [2], [1], [3]]


def test_schulze_two():
    # From <http://de.wikipedia.org/wiki/Schulze-Methode#Beispiel_2>
    v1 = SchulzeVote([0, 1, 2, 3], 3)
    v2 = SchulzeVote([1, 2, 3, 0], 2)
    v3 = SchulzeVote([3, 1, 2, 0], 2)
    v4 = SchulzeVote([3, 1, 0, 2], 2)

    r = evaluate_schulze([v1, v2, v3, v4], 4)

    assert r.d == [[0, 5, 5, 3],
                   [4, 0, 7, 5],
                   [4, 2, 0, 5],
                   [6, 4, 4, 0]]

    assert r.p == [[0, 5, 5, 5],
                   [5, 0, 7, 5],
                   [5, 5, 0, 5],
                   [6, 5, 5, 0]]

    # candidate wins not tested because any permutation in the lists would be
    # fine...


if __name__ == '__main__':
    pytest.main(sys.argv)
