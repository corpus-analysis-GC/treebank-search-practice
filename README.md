# Treebank search practice

The file [`data/thoward.parse`](data/thoward.parse) contains just over 1,000
sentences from the [Penn-Helsinki Parsed Corpus of Early Modern English, release
3](https://www.ling.upenn.edu/histcorpora/PPCEME-RELEASE-3).

A Python executable [`harness.py`](harness.py) (as in "test harness") is
provided to help you search it: all you need to do is to insert the appropriate
query string where indicated, and then execute it.

# What to do

Your mission, should you choose to accept it, is to find all instances of

1.  the word *Duke*
2.  the word *the* or *The*: use `|` for disjunction
3.  noun phrases (tag `NP`)
4.  noun phrases headed by a determiner (tag `NP` immediately dominating `D`)
5.  definite noun phrases headed by the definite determiner `the`/`The`; use
    parentheses for grouping/precedence
6.  matrix clauses (tag `IP-MAT`)
7.  matrix clauses headed by a verb in the preterite ("simple past"; tag
    `IP-MAT` immediately dominating `VBD`)
8.  matrix clauses headed by a verb in the preterite which take a PP complement
    (tag `IP-MAT` immediately dominating `VBD` and `PP` sisters in any order)

Bonus: can you think of other English definite determiners and use it to expand
the scope of (5)?

To do this, edit and then execute [`harness.py`](harness.py).

# Notes

The Penn Treebank data used in the homework uses different tags, e.g., it uses
`NN` instead of `N` and `DT` instead of `D`; it also uses "deeper" trees (e.g.,
it has a `VP` node containing the verb and its complements). **When in doubt,
just read the data file.**

Please do not circulate the attached data beyond this class, as it is not
licensed for this.

# Solutions

[`solutions.txt`](solutions.txt) contains the solutions.
