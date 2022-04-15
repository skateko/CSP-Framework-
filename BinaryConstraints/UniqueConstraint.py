import math
from typing import List, Dict
from CSP.CSP import Constraint


class UniqueConstraint(Constraint[tuple[int, int], int]):
    def __init__(self, variables: List[tuple[int, int]]):
        super().__init__(variables)
        self.variablesSorted = sorted(variables, key=lambda pair: (pair[0], pair[1]))

    def satisfied(self, assignment: Dict[tuple[int, int], int]) -> bool:
        row_size = int(math.sqrt(len(self.variables)))
        maxed_rows = []
        maxed_collumns = []

        for i in range(row_size):
            curr_row = [assignment[coordinates] for coordinates in self.variablesSorted if
                        coordinates[0] == i and coordinates in assignment]
            curr_col = [assignment[coordinates] for coordinates in self.variablesSorted if
                        coordinates[1] == i and coordinates in assignment]

            if len(curr_row) == row_size:
                maxed_rows.append(curr_row)

            if len(curr_col) == row_size:
                maxed_collumns.append(curr_col)

        if not (len(maxed_rows) == len(set(map(tuple, maxed_rows))) and len(maxed_collumns) == len(
                set(map(tuple, maxed_collumns)))):
            return False
        return True
