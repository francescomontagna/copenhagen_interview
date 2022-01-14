import numpy as np

def find_parents(node, A):
    """
    Args:
        node (int): index of the node to process. node \in [0, A.shape[0] - 1]
        A (numpy): adjacency matrix of the DAG
    Return:
        parents (list): list with the indices associated to the parents of "node" in A.
    """

    parents  = []

    for i in range(A.shape[0]):
        if A[i, node] == 1:
            parents.append(i)

    return parents


def find_sinks(A):
    """
    Return:
        sink_nodes (list): list with the indices of the sink nodes
    """
    sink_nodes = []
    for i, row in enumerate(A):
        if np.sum(row) == 0:
            sink_nodes.append(i)

    return sink_nodes


def sink_parents(A, D):
    """
    Args:
        A (numpy) : adjacency matrix of the DAG
        D (numpy) : descendants matrix
    """

    sink_nodes = find_sinks(A)
    for s in sink_nodes:
        parents = find_parents(s, A)
        for p in parents:
            A[p, s] = 0
            D[p, s] = 1
            D[p] += D[s]


def descendants(A, D):
    while np.sum(A) > 0:
        sink_parents(A, D)


def main(A, D):
    """
    Args:
        A (numpy) : adjacency matrix of the DAG
    """

    # Assume that the DAG of A is actually acyclic
    descendants(A, D)


def print_result(D):
    for i in range(D.shape[0]):
        result = f"{i+1}: "
        for j in range(len(D[i])):
            if D[i, j] > 0:
                result += f"{j+1}, "

        if result[-2] == ":":
            print(f"{i+1}: ")
        else:
            print(result[0:-2])


if __name__ == "__main__":

    # A = np.array(
    #     [
    #         [0, 1, 1, 0, 0],
    #         [0, 0, 0, 1, 0],
    #         [0, 0, 0, 1, 0],
    #         [0, 0, 0, 0, 0],
    #         [0, 0, 1, 1, 0]
    #     ]
    # )

    A = np.array(
        [
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
        ]
    )

    # Descendants matrix
    D = np.zeros_like(A) 

    main(A, D)
    print_result(D)
