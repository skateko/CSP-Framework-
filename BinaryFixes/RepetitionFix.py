from typing import List, Dict
from CSP.CSP import Fix


class RepetitionFix(Fix[tuple[int, int], int]):
    def __init__(self, variables: List[tuple[int, int]]):
        super().__init__(variables)

    def fix_domain(self, domains: Dict[tuple[int, int], List[int]], assignment: Dict[tuple[int, int], int]) -> bool:
        row_size = len(self.variables)
        for i in range(row_size - 2):
            if self.variables[i] in assignment and self.variables[i + 1] in assignment and self.variables[i + 2] not in assignment:
                if assignment[self.variables[i]] == assignment[self.variables[i + 1]]:
                    curr_value = assignment[self.variables[i]]
                    domain = domains[self.variables[i+2]].copy()
                    if curr_value in domain:
                        if len(domain) == 1:
                            return False
                        domain.remove(curr_value)
                    domains[self.variables[i + 2]] = domain
            elif self.variables[i] in assignment and self.variables[i + 1] not in assignment and self.variables[i + 2] in assignment:
                if assignment[self.variables[i]] == assignment[self.variables[i + 2]]:
                    curr_value = assignment[self.variables[i]]
                    domain = domains[self.variables[i+1]].copy()
                    if curr_value in domain:
                        if len(domain) == 1:
                            return False
                        domain.remove(curr_value)
                    domains[self.variables[i + 1]] = domain
            elif self.variables[i] not in assignment and self.variables[i + 1] in assignment and self.variables[i + 2] in assignment:
                if assignment[self.variables[i + 1]] == assignment[self.variables[i + 2]]:
                    curr_value = assignment[self.variables[i + 1]]
                    domain = domains[self.variables[i]].copy()
                    if curr_value in domain:
                        if len(domain) == 1:
                            return False
                        domain.remove(curr_value)
                    domains[self.variables[i]] = domain
        return True