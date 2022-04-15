from typing import List
from tabulate import tabulate

def create_nodes_table(backtrack_data: List[tuple[float, int, int]], forward_data: List[tuple[float, int, int]], title: str):
    backtrack = []
    counter: int = 0
    for item in backtrack_data:
        if item[2] == counter:
            backtrack.append((counter, item[1]))
            counter += 1

    forward = []
    counter = 0
    for item in forward_data:
        if item[2] == counter:
            forward.append((counter, item[1]))
            counter += 1

    data = [[item[0][0], item[0][1], item[1][1]] for item in zip(backtrack, forward)]
    col_names = ['SOLUTION COUNT', 'BT NODES', 'FC NODES']

    print(title)
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))



def create_time_table(backtrack_data: List[tuple[float, int, int]], forward_data: List[tuple[float, int, int]], title: str):
    backtrack = []
    counter: int = 0
    for item in backtrack_data:
        if item[2] == counter:
            backtrack.append((counter, item[0]))
            counter += 1

    forward = []
    counter = 0
    for item in forward_data:
        if item[2] == counter:
            forward.append((counter, item[0]))
            counter += 1

    data = [[item[0][0], item[0][1], item[1][1]] for item in zip(backtrack, forward)]
    col_names = ['SOLUTION COUNT', 'BT TIME [S]', 'FC TIME [S]']

    print(title)
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
