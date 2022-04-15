import math
import time
from typing import Dict, List, Optional

import CSP.CSP
from BinaryConstraints.CountConstraint import CountConstraint
from BinaryConstraints.RepetitionConstraint import RepetitionConstraint
from BinaryConstraints.UniqueConstraint import UniqueConstraint
from BinaryFixes.CountFix import CountFix
from BinaryFixes.RepetitionFix import RepetitionFix
from CSP import CSP
from Heuristics.VariablesHeuristics import VariablesByDomainLength
from Heuristics.ValueHeuristics import CountHeuristic, RandomHeuristic

path = r"Data"
title = r'/binary'


def binary_backtrack_prepare(data: List[str], name: str):
    variables: List[tuple[int, int]] = format_data(data)
    n = len(variables)
    row_size = int(math.sqrt(n))
    domains: Dict[tuple[int, int], List[int]] = {}
    for variable in variables:
        domains[variable] = get_domain(variable, data)

    print(name)
    print('data', data)
    print('variables ', variables)
    print('domains', domains)

    # Heuristics.Heuristics.heuristic_by_domain_length(variables, domains)
    # print('variables after heuristic ', variables)

    csp: CSP[tuple[int, int], int] = CSP.CSP(variables, domains)

    for i in range(row_size):
        curr_row = [coordinates for coordinates in variables if coordinates[0] == i]
        curr_col = [coordinates for coordinates in variables if coordinates[1] == i]
        csp.add_constraint(RepetitionConstraint(curr_row))
        csp.add_constraint(RepetitionConstraint(curr_col))
        csp.add_constraint(CountConstraint(curr_row))
        csp.add_constraint(CountConstraint(curr_col))
    csp.add_constraint(UniqueConstraint(variables))
    csp.add_static_variables_heuristic(VariablesByDomainLength(domains))
    # csp.add_value_heuristic(CountHeuristic())
    return csp, variables, n, domains


def binary_forward_prepare(data: List[str], name: str):
    csp, variables, n, domains = binary_backtrack_prepare(data, name)
    row_size = int(math.sqrt(len(variables)))
    for i in range(row_size):
        curr_row = [coordinates for coordinates in variables if coordinates[0] == i]
        curr_col = [coordinates for coordinates in variables if coordinates[1] == i]
        csp.add_fix(RepetitionFix(curr_row))
        csp.add_fix(RepetitionFix(curr_col))
        csp.add_fix(CountFix(curr_row))
        csp.add_fix(CountFix(curr_col))
    return csp, variables, n, domains


def binary_backward(data: List[str], name: str):
    csp, variables, n, domains = binary_backtrack_prepare(data, name)
    start_time = time.time()
    solution: Optional[Dict[tuple[int, int], int]] = csp.run_backtrack()
    print("--- %s seconds ---" % (time.time() - start_time))
    print_solution(solution, variables, n)
    print()


def binary_backward_count(data: List[str], name: str):
    csp, variables, n, domains = binary_backtrack_prepare(data, name)
    start_time = time.time()
    print('number of solutions: ', csp.run_backtrack_count())
    print("--- %s seconds ---" % (time.time() - start_time))


def binary_forward(data: List[str], name: str):
    csp, variables, n, domains = binary_forward_prepare(data, name)
    start_time = time.time()
    solution: Optional[Dict[tuple[int, int], int]] = csp.run_forward()
    print("--- %s seconds ---" % (time.time() - start_time))
    print_solution(solution, variables, n)
    print()


def binary_forward_count(data: List[str], name: str):
    csp, variables, n, domains = binary_forward_prepare(data, name)
    start_time = time.time()
    print('number of solutions: ', csp.run_forward_count())
    print("--- %s seconds ---" % (time.time() - start_time))


def binary_backtrack_data(data: List[str], name: str) -> List[tuple[float, int, int]]:
    csp, variables, n, domains = binary_backtrack_prepare(data, name)
    start_time = time.time()
    backtrack_data: List[tuple[float, int, int]] = [(0, 0, 0)]
    backtrack_data = csp.run_backtrack_data(backtrack_data, start_time)
    backtrack_data.sort(key=lambda pair: pair[0])
    # print(backtrack_data)
    return backtrack_data


def binary_forward_data(data: List[str], name: str) -> List[tuple[float, int, int]]:
    csp, variables, n, domains = binary_forward_prepare(data, name)
    start_time = time.time()
    forward_data: List[tuple[float, int, int]] = [(0, 0, 0)]
    forward_data = csp.run_forward_data(forward_data, start_time)
    forward_data.sort(key=lambda pair: pair[0])
    # print(forward_data)
    return forward_data


def print_solution(solution: Optional[Dict[tuple[int, int], int]], data, n):
    if solution is None:
        print("NO SOLUTION FOUND")
    else:
        print('SOLUTION MATRIX ')
        print(matrix_to_string(solution, data, n))


def format_data(data: List[str]) -> List[tuple[int, int]]:
    pairs: List[tuple[int, int]] = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            item = data[i][j]
            pairs.append((i, j))
    return pairs


def get_domain(variable: tuple[int, int], data: List[str]) -> List[int]:
    item = data[variable[0]][variable[1]]
    if item.isnumeric():
        # print(variable, item)
        return [int(item)]
    else:
        return [0, 1]


def matrix_to_string(solution: Dict[tuple[int, int], int], variables: List[tuple[int, int]], size: int):
    # items = sorted(list(solution.items()), key=lambda pair: (pair[0][0], pair[0][1]))
    sorted_variables = sorted(variables, key=lambda pair: (pair[0], pair[1]))
    output: str = "["
    for i in range(0, len(sorted_variables)):
        if i % math.sqrt(size) == 0 and i != 0:
            output += ']\n['
        if sorted_variables[i] in solution:
            output += f' {solution[sorted_variables[i]]} '
        else:
            output += f' - '
    output += ']'
    return output

