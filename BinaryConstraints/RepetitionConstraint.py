from typing import List, Dict
from CSP.CSP import Constraint


class RepetitionConstraint(Constraint[tuple[int, int], int]):
    def __init__(self, variables: List[tuple[int, int]]):
        super().__init__(variables)

    def satisfied(self, assignment: Dict[tuple[int, int], int]) -> bool:
        row_size = len(self.variables)
        for i in range(row_size - 2):
            if self.variables[i] not in assignment or self.variables[i + 1] not in assignment or self.variables[i + 2] not in assignment:
                continue
            if assignment[self.variables[i]] == assignment[self.variables[i + 1]] == assignment[self.variables[i + 2]]:
                return False
        return True
