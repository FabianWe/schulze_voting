
# schulze_voting
The Schulze voting procedure is explained in more detail on [Wikipedia](https://en.wikipedia.org/wiki/Schulze_method). This pure python library can be used to evaluate such votings.

## Installation
Just install via pip:
```bash
pip install schulze_voting
```
## Creating a Schulze Voting
This library supports weighted votes, that is each person / group that casts a vote can have a weight > 0 (for example weighted according to a number of people the group represents).
Suppose that there are 4 options to vote for (*A*, *B*, *C* and *D*). The voter wants to rank *A* > *B* = *D* > *C*. And the voter has a weight of 2. Then this vote can be created with the following code:
```python
vote = SchulzeVote([0, 1, 2, 1], 2)
```
The lists simply assigns each option a rank (smaller rank means ranked higher). So here *A* has the highest rank, *B* and *D* both have the second highest rank and *C* has the lowest rank.

There a different methods to compute (intermediate) results from lists of such votes:

 - `compute_d`
 - `compute_p`
 - `rank_p`
 - `evaluate_schulze`: Computes the matrices d and p and ranks p.

The ranking of p is returned as a list of list of ints. The first list contains all options that are ranked highest, the next list all entries ranked second best and so on.

So if the result is that A = C > B = D > E the result would contain `[[0, 2], [1, 3], [4]]`.

See the source code for more documentation and examples.

## License
**MIT License**

Copyright (c) 2018 Fabian Wenzelmann

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
