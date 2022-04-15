import math
from typing import List, Dict
from CSP.CSP import Constraint


class MathematicalConstraint(Constraint[tuple[int, int], int]):
    def __init__(self, variables: List[tuple[int, int]], data: List[str]):
        super().__init__(variables)
        self.variables: List[tuple[int, int]] = variables
        self.data = data

    def satisfied(self, assignment: Dict[tuple[int, int], int]) -> bool:
        row_size = int(math.sqrt(len(self.variables)))
        items = list(assignment.items())

        index_to_check = len(items) - 1
        last_added = items[index_to_check]
        last_added_row: int = last_added[0][0]
        last_added_collumn: int = last_added[0][1]
        last_original_coords = (last_added_row * 2, last_added_collumn * 2)

        # print((last_added_row, last_added_collumn))
        constraint_row = last_original_coords[0]
        if last_added_collumn > 0:
            if (last_added_row, last_added_collumn - 1) in assignment.keys():
                value = assignment[(last_added_row, last_added_collumn - 1)]
                constraint_left_col = last_original_coords[1] - 1
                constraint_left = self.data[constraint_row][constraint_left_col]
                if constraint_left == '>':
                    if value < last_added[1]:
                        return False
                elif constraint_left == '<':
                    if value > last_added[1]:
                        return False

        if last_added_collumn < row_size - 1:
            if (last_added_row, last_added_collumn + 1) in assignment.keys():
                # print(assignment[(last_added_row, last_added_collumn + 1)])
                value = assignment[(last_added_row, last_added_collumn + 1)]
                constraint_right_col = last_original_coords[1] + 1
                constraint_right = self.data[constraint_row][constraint_right_col]
                if constraint_right == '>':
                    if value > last_added[1]:
                        return False
                elif constraint_right == '<':
                    if value < last_added[1]:
                        return False

        if last_added_row > 0:
            if (last_added_row - 1, last_added_collumn) in assignment.keys():
                value = assignment[(last_added_row - 1, last_added_collumn)]
                constraint_row = last_original_coords[0] - 1
                constraint_upper_col = int(last_original_coords[1] / 2)
                constraint_upper = self.data[constraint_row][constraint_upper_col]
                if constraint_upper == '>':
                    # print((last_added_row - 1, last_added_collumn), (last_added_row, last_added_collumn))
                    if last_added[1] > value:  # last added jest na dole
                        return False
                elif constraint_upper == '<':
                    if last_added[1] < value:
                        return False

        if last_added_row < row_size - 1:
            if (last_added_row + 1, last_added_collumn) in assignment.keys():
                value = assignment[(last_added_row + 1, last_added_collumn)]
                constraint_row = last_original_coords[0] + 1
                constraint_down_col = int(last_original_coords[1] / 2)
                constraint_down = self.data[constraint_row][constraint_down_col]
                if constraint_down == '>':
                    if last_added[1] < value:
                        return False
                elif constraint_down == '<':
                    if last_added[1] > value:
                        return False
        return True