#!/usr/bin/env python
"""Tree queries for Thomas Howard data."""

from typing import List

from nltk import tgrep, tree


DATA = "data/thoward.parse"


def print_nodes(query: str, trees: List[tree.ParentedTree]) -> None:
    """Prints all nodes matching the query.

    Args:
        query: a TGrep2 query string.
        trees: a list of one or more `ParentedTree`s to be queried.
    """
    for nodes in tgrep.tgrep_nodes(query, trees):
        # This iterator is yields lists of nodes, one per sentence, with any
        # (possibly none) matches for that sentence.
        for node in nodes:
            print(node)


def main() -> None:
    # Loads collection of trees.
    trees = []
    with open(DATA, "r") as source:
        for line in source:
            trees.append(tree.ParentedTree.fromstring(line.rstrip()))
    # TODO: Insert your query string where the ellipsis is.
    print_nodes(..., trees)


if __name__ == "__main__":
    main()
