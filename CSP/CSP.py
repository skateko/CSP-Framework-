import copy
import math
import time
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Dict, List, Optional

V = TypeVar('V')
D = TypeVar('D')


class VariablesHeuristic(Generic[V], ABC):  # Generic lets us have only these values
    @abstractmethod
    def Heuristic(self, variables: List[V]) -> None:
        ...


class ValuesHeuristic(Generic[D], ABC):  # Generic lets us have only these values
    @abstractmethod
    def Heuristic(self, values: List[D], solution: Dict[V, D]) -> None:
        ...


# Abstract class for constraints
class Constraint(Generic[V, D], ABC):  # Generic lets us have only these values
    # Variables for constraint
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    # Method to override - is for letting program know if constraint is satisfied
    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...


class Fix(Generic[V, D], ABC):
    def __init__(self, variables: List[V]):
        self.variables = variables

    @abstractmethod
    def fix_domain(self, domains: Dict[V, List[D]], assignment: Dict[V, D]) -> bool:
        ...


# Variables are of type V
# They have ranges of values - domains - of type D
# Constraints determine if a variable's domain selection is valid
class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        self.variables: List[V] = variables  # Variables to put constraints on
        self.domains: Dict[V, List[D]] = domains  # Domain of each variable
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        self.fixes: Dict[V, List[Fix[V, D]]] = {}
        self.static_variable_heuristic: Optional[VariablesHeuristic[V]] = None
        self.values_heuristic: Optional[ValuesHeuristic[D]] = None

        for variable in self.variables:
            self.constraints[variable] = []
            self.fixes[variable] = []
            if variable not in self.domains:
                raise LookupError("Variables should have a domain assigned to it")

    # Method to add a constraint to our problem
    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable declared in constraint doesnt exist in CSP problem")
            else:
                self.constraints[variable].append(constraint)

    # Method to add a constraint to our problem
    def add_fix(self, fix: Fix[V, D]) -> None:
        for variable in fix.variables:
            if variable not in self.variables:
                raise LookupError("Variable declared in Fix doesnt exist in CSP problem")
            else:
                self.fixes[variable].append(fix)

    # Method to check if a given configuration of variables and selected domains satisfies constraints
    # This method goes through every constraint for a given variable (variable added to the assignment)
    def are_all_constr_satisfied(self, variable: V, solution: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(solution):
                return False
        return True

    def fix_domains(self, variable: V, domains: Dict[V, List[D]], solution: Dict[V, D]) -> bool:
        for fix in self.fixes[variable]:
            if not fix.fix_domain(domains, solution):
                return False
        return True

    def add_static_variables_heuristic(self, static_variable_heuristic: VariablesHeuristic[V]):
        self.static_variable_heuristic = static_variable_heuristic

    def add_value_heuristic(self, value_heuristic: ValuesHeuristic[D]):
        self.values_heuristic = value_heuristic

    # Backtracking is the idea that once you hit a wall in your search, you
    # go back to the last known point where you made a decision before the wall,
    # and choose a different path.

    def backtrack_search(self, solution: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        # assignment is complete if every variable is assigned
        if len(solution) == len(self.variables):
            return solution

        # variables in CSP but not in assignment
        unassigned_variables: List[V] = [v for v in self.variables if v not in solution]

        # every possible domain value of the first unassigned variable
        first: V = unassigned_variables[0]
        domains_var = self.domains[first].copy()
        if self.values_heuristic is not None:
            self.values_heuristic.Heuristic(domains_var, solution)
        for curr_domain in domains_var:
            solution_copy = solution.copy()
            solution_copy[first] = curr_domain
            # if current solution is valid, continue
            # print(first)
            # print(Binary.matrix_to_string(solution_copy, self.variables, len(self.variables)))
            if self.are_all_constr_satisfied(first, solution_copy):
                result: Optional[Dict[V, D]] = self.backtrack_search(solution_copy)
                # print('wyjscie z drzewa')
                if result is not None:
                    return result
        # If there is not solution utilizing the existing set we return none, algorithm
        # will backtrack to the point where a different assignment can be made
        return None

    def backtrack_search_count(self, solution: Dict[V, D] = {}) -> int:
        # assignment is complete if every variable is assigned
        if len(solution) == len(self.variables):
            return 1

        solution_counter = 0

        # variables in CSP but not in assignment
        unassigned_variables: List[V] = [v for v in self.variables if v not in solution]

        # every possible domain value of the first unassigned variable
        first: V = unassigned_variables[0]
        domains_var = self.domains[first].copy()
        if self.values_heuristic is not None:
            self.values_heuristic.Heuristic(domains_var, solution)
        for curr_domain in domains_var:  # self.domains[first]
            solution_copy = solution.copy()
            solution_copy[first] = curr_domain
            # if current solution is valid, continue
            if self.are_all_constr_satisfied(first, solution_copy):
                solution_counter += self.backtrack_search_count(solution_copy)
                # print('domain,', curr_domain, 'counter ', counter)
        # If there is not solution utilizing the existing set we return none, algorithm
        # will backtrack to the point where a different assignment can be made
        return solution_counter

    def forward_search(self, domains: Dict[V, List[D]], solution: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        # assignment is complete if every variable is assigned
        if len(solution) == len(self.variables):
            return solution

        # variables in CSP but not in assignment
        unassigned_variables: List[V] = [v for v in self.variables if v not in solution]
        # sorted(unassigned_variables, key=lambda x: len(domains[x]))

        # every possible domain value of the first unassigned variable
        first: V = unassigned_variables[0]
        domains_var = domains[first].copy()
        if self.values_heuristic is not None:
            self.values_heuristic.Heuristic(domains_var, solution)
        for value in domains_var:
            solution_copy = solution.copy()
            solution_copy[first] = value
            # print(first)
            # print(self.matrix_to_string(solution_copy, self.variables, len(self.variables)))
            if self.are_all_constr_satisfied(first, solution_copy):
                domains_copy = domains.copy()  # self.domains[first].copy()
                if self.fix_domains(first, domains_copy, solution_copy):
                    result: Optional[Dict[V, D]] = self.forward_search(domains_copy, solution_copy)
                    if result is not None:
                        return result
        return None

    def forward_search_count(self, domains: Dict[V, List[D]], solution: Dict[V, D] = {}) -> int:
        # assignment is complete if every variable is assigned
        if len(solution) == len(self.variables):
            return 1

        solution_counter = 0
        # variables in CSP but not in assignment
        unassigned_variables: List[V] = [v for v in self.variables if v not in solution]

        # every possible domain value of the first unassigned variable
        first: V = unassigned_variables[0]
        domains_var = domains[first].copy()
        if self.values_heuristic is not None:
            self.values_heuristic.Heuristic(domains_var, solution)
        for value in domains_var:
            solution_copy = solution.copy()
            solution_copy[first] = value
            # domains_copy = copy.deepcopy(domains)  # self.domains[first].copy()
            # domains_copy = copy.copy(domains)
            # domains_copy = domains.copy()
            if self.are_all_constr_satisfied(first, solution_copy):
                domains_copy = domains.copy()  # self.domains[first].copy()
                if self.fix_domains(first, domains_copy, solution_copy):
                    solution_counter += self.forward_search_count(domains_copy, solution_copy)
        return solution_counter

    def backtrack_data(self, data: List[tuple[float, int, int]], start_time: float,
                       solution: Dict[V, D] = {}) -> List[tuple[float, int, int]]:
        # assignment is complete if every variable is assigned
        if len(solution) == len(self.variables):
            last_item = data[-1]
            data.append((time.time() - start_time, last_item[1], last_item[2] + 1))  # (czas, wezly, rozwiazania)
            return data

        last_item = data[-1]
        data.append((time.time() - start_time, last_item[1] + 1, last_item[2]))
        # variables in CSP but not in assignment
        unassigned_variables: List[V] = [v for v in self.variables if v not in solution]

        # every possible domain value of the first unassigned variable
        first: V = unassigned_variables[0]
        domains_var = self.domains[first].copy()
        # print('before in csp', domains_var)
        if self.values_heuristic is not None:
            self.values_heuristic.Heuristic(domains_var, solution)
        # print('after in csp', domains_var)
        for curr_domain in domains_var:
            solution_copy = solution.copy()
            solution_copy[first] = curr_domain
            if self.are_all_constr_satisfied(first, solution_copy):
                data = self.backtrack_data(data, start_time, solution_copy)
        return data

    def forward_data(self, data: List[tuple[float, int, int]], start_time: float, domains: Dict[V, List[D]],
                     solution: Dict[V, D] = {}) -> List[tuple[float, int, int]]:
        # assignment is complete if every variable is assigned
        if len(solution) == len(self.variables):
            last_item = data[-1]
            data.append((time.time() - start_time, last_item[1], last_item[2] + 1))  # (czas, wezly, rozwiazania)
            return data

        last_item = data[-1]
        data.append((time.time() - start_time, last_item[1] + 1, last_item[2]))

        # variables in CSP but not in assignment
        unassigned_variables: List[V] = [v for v in self.variables if v not in solution]

        # every possible domain value of the first unassigned variable
        first: V = unassigned_variables[0]
        domains_var = domains[first].copy()
        # print('before in csp', domains_var)
        if self.values_heuristic is not None:
            self.values_heuristic.Heuristic(domains_var, solution)
        # print('after in csp', domains_var)
        for value in domains_var:
            solution_copy = solution.copy()
            solution_copy[first] = value
            # domains_copy = copy.deepcopy(domains)  # self.domains[first].copy()
            # domains_copy = copy.copy(domains)
            # domains_copy = domains.copy()
            if self.are_all_constr_satisfied(first, solution_copy):
                domains_copy = domains.copy()  # self.domains[first].copy()
                if self.fix_domains(first, domains_copy, solution_copy):
                    data = self.forward_data(data, start_time, domains_copy, solution_copy)
        return data

    def __run_static_heuristic(self):
        if self.static_variable_heuristic is not None:
            self.static_variable_heuristic.Heuristic(self.variables)
            print('variables after heuristic ', self.variables)

    def run_backtrack(self):
        self.__run_static_heuristic()
        solution: Optional[Dict[tuple[int, int], int]] = self.backtrack_search()
        return solution

    def run_forward(self):
        self.__run_static_heuristic()
        solution: Optional[Dict[tuple[int, int], int]] = self.forward_search(self.domains)
        return solution

    def run_backtrack_count(self):
        self.__run_static_heuristic()
        solution_count: int = self.backtrack_search_count()
        return solution_count

    def run_forward_count(self):
        self.__run_static_heuristic()
        solution_count: int = self.forward_search_count(self.domains)
        return solution_count

    def run_backtrack_data(self, backtrack_data: List[tuple[float, int, int]]
                           , start_time: float) -> List[tuple[float, int, int]]:
        self.__run_static_heuristic()
        return self.backtrack_data(backtrack_data, start_time)

    def run_forward_data(self, backtrack_data: List[tuple[float, int, int]]
                         , start_time: float) -> List[tuple[float, int, int]]:
        self.__run_static_heuristic()
        return self.forward_data(backtrack_data, start_time, self.domains)