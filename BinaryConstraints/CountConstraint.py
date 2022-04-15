from typing import List, Dict
from CSP.CSP import Constraint


class CountConstraint(Constraint[tuple[int, int], int]):
    def __init__(self, variables: List[tuple[int, int]]):
        super().__init__(variables)

    def satisfied(self, assignment: Dict[tuple[int, int], int]) -> bool:
        row_size = len(self.variables)
        items = [assignment[coordinates] for coordinates in self.variables if coordinates in assignment]
        if not (len(items) > row_size / 2):
            return True
        else:
            zero_counter = 0
            one_counter = 0
            for value in items:
                if value == 0:
                    zero_counter += 1
                else:
                    one_counter += 1
            if zero_counter > row_size / 2 or one_counter > row_size / 2:
                return False
            return True
