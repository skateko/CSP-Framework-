import math
from typing import List, Dict
from CSP.CSP import Fix


class MathFix(Fix[tuple[int, int], int]):
    def __init__(self, variables: List[tuple[int, int]], data: List[str]):
        super().__init__(variables)
        self.variables: List[tuple[int, int]] = variables
        self.data = data

    def fix_domain(self, domains: Dict[tuple[int, int], List[int]], assignment: Dict[tuple[int, int], int]) -> bool:
        row_size = int(math.sqrt(len(self.variables)))

        index_to_check = list(assignment.keys())[-1]
        last_added_value = assignment[index_to_check]
        last_added_row: int = index_to_check[0]
        last_added_collumn: int = index_to_check[1]
        last_original_coords = (last_added_row * 2, last_added_collumn * 2)

        # print((last_added_row, last_added_collumn))
        constraint_row = last_original_coords[0]
        if last_added_collumn > 0:
            if (last_added_row, last_added_collumn - 1) not in assignment:
                constraint_left_col = last_original_coords[1] - 1
                constraint_left = self.data[constraint_row][constraint_left_col]
                if constraint_left == '>':
                    curr_domain = domains[(last_added_row, last_added_collumn - 1)].copy()
                    for i in range(0, last_added_value + 1):
                        if i in curr_domain:
                            if len(curr_domain) == 1:
                                return False
                            curr_domain.remove(i)
                    domains[(last_added_row, last_added_collumn - 1)] = curr_domain
                elif constraint_left == '<':
                    curr_domain = domains[(last_added_row, last_added_collumn - 1)].copy()
                    for i in range(last_added_value, row_size):
                        if i in curr_domain:
                            if len(curr_domain) == 1:
                                return False
                            curr_domain.remove(i)
                    domains[(last_added_row, last_added_collumn - 1)] = curr_domain

        if last_added_collumn < row_size - 1:
            if (last_added_row, last_added_collumn + 1) not in assignment:
                constraint_right_col = last_original_coords[1] + 1
                constraint_right = self.data[constraint_row][constraint_right_col]
                if constraint_right == '>':
                    curr_domain = domains[(last_added_row, last_added_collumn + 1)].copy()
                    for i in range(last_added_value, row_size):
                        if i in curr_domain:
                            if len(curr_domain) == 1:
                                return False
                            curr_domain.remove(i)
                    domains[(last_added_row, last_added_collumn + 1)] = curr_domain
                elif constraint_right == '<':
                    curr_domain = domains[(last_added_row, last_added_collumn + 1)].copy()
                    for i in range(0, last_added_value + 1):
                        if i in curr_domain:
                            if len(curr_domain) == 1:
                                return False
                            curr_domain.remove(i)
                    domains[(last_added_row, last_added_collumn + 1)] = curr_domain

        if last_added_row > 0:
            if (last_added_row - 1, last_added_collumn) not in assignment:
                constraint_row = last_original_coords[0] - 1
                constraint_upper_col = int(last_original_coords[1] / 2)
                constraint_upper = self.data[constraint_row][constraint_upper_col]
                if constraint_upper == '>':
                    curr_domain = domains[(last_added_row - 1, last_added_collumn)].copy()
                    for i in range(0, last_added_value + 1):
                        if i in curr_domain:
                            if len(curr_domain) == 1:
                                return False
                            curr_domain.remove(i)
                    domains[(last_added_row - 1, last_added_collumn)] = curr_domain
                elif constraint_upper == '<':
                    curr_domain = domains[(last_added_row - 1, last_added_collumn)].copy()
                    for i in range(last_added_value, row_size):
                        if i in curr_domain:
                            if len(curr_domain) == 1:
                                return False
                            curr_domain.remove(i)
                    domains[(last_added_row - 1, last_added_collumn)] = curr_domain

        if last_added_row < row_size - 1:
            if (last_added_row + 1, last_added_collumn) not in assignment:
                constraint_row = last_original_coords[0] + 1
                constraint_down_col = int(last_original_coords[1] / 2)
                constraint_down = self.data[constraint_row][constraint_down_col]
                if constraint_down == '>':
                    curr_domain = domains[(last_added_row + 1, last_added_collumn)].copy()
                    for i in range(last_added_value, row_size):
                        if i in curr_domain:
                            if len(curr_domain) == 1:
                                return False
                            curr_domain.remove(i)
                    domains[(last_added_row + 1, last_added_collumn)] = curr_domain
                elif constraint_down == '<':
                    curr_domain = domains[(last_added_row + 1, last_added_collumn)].copy()
                    for i in range(0, last_added_value + 1):
                        if i in curr_domain:
                            if len(curr_domain) == 1:
                                return False
                            curr_domain.remove(i)
                    domains[(last_added_row + 1, last_added_collumn)] = curr_domain
        return True