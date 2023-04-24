import typing as ty
import itertools

from nltk.tree import Tree


def paraphrase(tree: Tree, limit: int) -> ty.List[Tree]:
    """Generate a paraphrases for a given parse tree

    Args:
        tree: parse tree
        limit: max amount of paraphrases

    Returns:
        A list with parse trees as paraphrases
    """

    trees = []

    def parse(node):
        # Stop condition for recursion
        if is_leaf(node):
            return

        # We can do permutations if node meets several conditions:
        # 1. have several child NP nodes
        # 2. between these child nodes must be a , or CC node
        # Also we are not interested in node values, just label and index

        # Find all child NP nodes
        nps = []
        for i, n in enumerate(node):
            if n.label() == "NP":
                nps.append(i)

        # Check for the 1-st condition: node must have several child NP nodes
        if len(nps) >= 2:
            # Check for the 2-st condition: between child NP nodes must be a , or CC node
            # We can just check if node indexes have a difference in 2, that indicates that
            # there are some element between them... Yeah, we need to check if this element
            # is , or CC, but...
            # ¯\_(ツ)_/¯

            # Form a pairs of indexes, so we can check if difference between them is 2
            combinations = []
            for i in range(len(nps) - 1):
                combinations.append([nps[i], nps[i + 1]])

            # Check difference between pairs. If at least one pair doesnt meet condition when
            # dont generate permutations
            # ? not sure if its allowed
            counter = 0
            for pair in combinations:
                difference = pair[1] - pair[0]
                if difference == 2:
                    counter += 1

            if counter == len(combinations):
                permutations = generate_permutations(nps)
                # The very first permutation is already in tree, so we skip it
                reference = permutations.pop(0)

                if len(permutations) > limit:
                    permutations = permutations[0:limit]

                # Start applying permutations to a tree. First apply permutation, deep copy tree
                # and reapply permutation again, so tree returns to its initial state
                for permutation in permutations:
                    swap(node, reference, permutation)
                    trees.append(tree.copy(deep=True))
                    swap(node, permutation, reference)
                return

        # Continue parsing whole tree using recursion
        for n in node:
            parse(n)

    parse(tree)
    return trees


def generate_permutations(data):
    return list(itertools.permutations(data))


def is_leaf(node):
    if len(node) == 1:
        return True
    return False


def swap(node, reference, permutation):
    nodes = []
    for i in permutation:
        # ! Deep copying nodes into list may be memory consuming
        nodes.append(node[i].copy(deep=True))

    n = 0
    for r in reference:
        node[r] = nodes[n]
        n += 1
