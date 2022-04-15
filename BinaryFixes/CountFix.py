from typing import List, Dict
from CSP.CSP import Fix


class CountFix(Fix[tuple[int, int], int]):
    def __init__(self, variables: List[tuple[int, int]]):
        super().__init__(variables)

    def fix_domain(self, domains: Dict[tuple[int, int], List[int]], assignment: Dict[tuple[int, int], int]) -> bool:
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
            if zero_counter == row_size / 2:
                for variable in self.variables:
                    if variable not in assignment:
                        domain = domains[variable].copy()
                        if 0 in domain:
                            if len(domain) == 1:
                                return False
                            domain.remove(0)
                        domains[variable] = domain
            elif one_counter == row_size / 2:
                for variable in self.variables:
                    if variable not in assignment:
                        domain = domains[variable].copy()
                        if 1 in domain:
                            if len(domain) == 1:
                                return False
                            domain.remove(1)
                        domains[variable] = domain
        return True
