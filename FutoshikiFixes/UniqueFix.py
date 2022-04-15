from typing import List, Dict
from CSP.CSP import Fix


class UniqueFix(Fix[tuple[int, int], int]):
    def __init__(self, variables: List[tuple[int, int]]):
        super().__init__(variables)

    def fix_domain(self, domains: Dict[tuple[int, int], List[int]], assignment: Dict[tuple[int, int], int]) -> bool:
        items = [assignment[coordinates] for coordinates in self.variables if coordinates in assignment]
        for variable in self.variables:
            if variable not in assignment:
                domain = domains[variable].copy()
                for value in items:
                    if value in domain:
                        if len(domain) == 1:
                            return False
                        domain.remove(value)
                domains[variable] = domain
        return True

