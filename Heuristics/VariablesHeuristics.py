from typing import List, Dict

from CSP.CSP import VariablesHeuristic


# def heuristic_by_domain_length(variables: List[tuple[int, int]], domains: Dict[tuple[int, int], List[int]]):
#     variables.sort(key=lambda x: len(domains[x]))

class VariablesByDomainLength(VariablesHeuristic[List[tuple[int, int]]]):
    def __init__(self, domains: Dict[tuple[int, int], List[int]]):
        self.domains = domains

    def Heuristic(self, variables: List[tuple[int, int]]) -> None:
        variables.sort(key=lambda x: len(self.domains[x]))
