"""Knapsack Problem via Branch-and-Bound

Problem: Given items with weights and values and a knapsack with a weight capacity,
determine the maximum total value obtainable without exceeding the capacity."""


class Node:
    def __init__(self, level, profit, weight, bound): # type: ignore
        # Level in the decision tree (index of item being considered)
        self.level = level
        self.profit = profit    # Total profit accumulated
        self.weight = weight    # Total weight accumulated
        self.bound = bound      # Upper bound on maximum profit achievable from this node


def bound(node, n, capacity, items):  # type: ignore
    """Compute the upper bound on the maximum profit in the subproblem defined by this node."""
    if node.weight >= capacity:  # type: ignore
        return 0
    profit_bound = node.profit  # type: ignore
    j = node.level + 1  # type: ignore
    totweight = node.weight  # type: ignore

    # Take items in order while under the capacity
    while j < n and totweight + items[j][0] <= capacity:
        totweight += items[j][0]  # type: ignore
        profit_bound += items[j][1]  # type: ignore
        j += 1  # type: ignore

    # If there is still capacity, take fraction of the next item
    if j < n:
        profit_bound += (capacity - totweight) * items[j][1] / items[j][0] # type: ignore
    return profit_bound  # type: ignore


def knapsack_branch_and_bound(capacity, items):  # type: ignore
    """Solve the 0/1 knapsack problem using branch and bound.
       items: list of tuples (weight, profit). Items are sorted by profit/weight ratio descending."""

    # Sort items by profit/weight ratio descending
    items = sorted(items, key=lambda x: x[1]/x[0], reverse=True) # type: ignore
    n = len(items) # type: ignore
    max_profit = 0
    queue = []

    # Start with a dummy node at level -1.
    v = Node(level=-1, profit=0, weight=0, bound=0)
    v.bound = bound(v, n, capacity, items)  # type: ignore
    queue.append(v)  # type: ignore

    while queue:
        v = queue. pop(0)  # Pop the first node (BFS style) # type: ignore
        if v.level == n - 1 or v.bound <= max_profit:  # type: ignore

            continue

        # Next level (consider the next item)
        u_level = v.level + 1 # type: ignore

        # Case 1: Include the next item if possible
        u = Node(level=u_level,  # type: ignore
                 profit=v.profit + items[u_level][1],  # type: ignore
                 weight=v.weight + items[u_level][0],  # type: ignore
                 bound=0)

        if u.weight <= capacity and u.profit > max_profit:  # type: ignore
            max_profit = u.profit  # type: ignore

        u.bound = bound(u, n, capacity, items)  # type: ignore
        if u.bound > max_profit:  # type: ignore
            queue. append(u)  # type: ignore

        # Case 2: Exclude the next item
        u2 = Node(level=u_level,  # type: ignore
                  profit=v.profit,  # type: ignore
                  weight=v.weight,  # type: ignore
                  bound=0)

        u2.bound = bound(u2, n, capacity, items)  # type: ignore
        if u2.bound > max_profit:  # type: ignore
            queue. append(u2) # type: ignore

    return max_profit # type: ignore

 # Define items as (weight, profit)

items = [(2, 40), (3, 50), (5, 100), (1, 20)]
capacity = 5
result = knapsack_branch_and_bound(capacity, items) # type: ignore
print("Maximum profit for the knapsack problem:", result) # type: ignore


"""Explanation:

Node Representation: Each node represents a decision point—items included so far, total weight, total profit—and an upper bound of future profit.
Bound Calculation: For a node, we estimate the best possible outcome by taking as many of the remaining items (or fractions) as possible (even though only whole items can finally be selected).
Branching: For each decision node, the algorithm creates two child nodes: one that includes the next item and one that excludes it.
Pruning: Nodes whose bound is less than the current maximum profit are dropped from further consideration.

This example illustrates the branch-and-bound technique to systematically search for a solution while avoiding unnecessary calculations."""
