from typing import List, Dict
from CSP.CSP import Constraint


class RepetitionConstraint(Constraint[tuple[int, int], int]):
    def __init__(self, variables: List[tuple[int, int]]):
        super().__init__(variables)

    def satisfied(self, assignment: Dict[tuple[int, int], int]) -> bool:
        items = [assignment[coordinates] for coordinates in self.variables if coordinates in assignment]
        if len(set(items)) != len(items):
            return False
        return True
