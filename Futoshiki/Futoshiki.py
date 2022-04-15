import math
import random
import time
from typing import Dict, List, Optional

import Heuristics.VariablesHeuristics
from CSP import CSP
from FutoshikiConstraints.MathematicalConstraint import MathematicalConstraint
from FutoshikiConstraints.RepetitionConstraint import RepetitionConstraint
from FutoshikiFixes.MathFix import MathFix
from FutoshikiFixes.UniqueFix import UniqueFix
from Heuristics.VariablesHeuristics import VariablesByDomainLength
from Heuristics.ValueHeuristics import CountHeuristic, RandomHeuristic

path = r"Data"
title = r'/futoshiki'


def futoshiki_backtrack_prepare(data: List[str], name: str):
    variables: List[tuple[int, int]] = format_data(data)
    row_size = int(math.sqrt(len(variables)))
    domains: Dict[tuple[int, int], List[int]] = {}
    n = len(variables)
    for variable in variables:
        domains[variable] = get_domain(variable, data, row_size)

    print(name)
    print('data', data)
    print('variables ', variables)
    print('domains', domains)

    csp: CSP[tuple[int, int], int] = CSP.CSP(variables, domains)
    for i in range(row_size):
        curr_row = [coordinates for coordinates in variables if coordinates[0] == i]
        curr_col = [coordinates for coordinates in variables if coordinates[1] == i]
        csp.add_constraint(RepetitionConstraint(curr_row))
        csp.add_constraint(RepetitionConstraint(curr_col))
    csp.add_constraint(MathematicalConstraint(variables, data))
    csp.add_static_variables_heuristic(VariablesByDomainLength(domains))
    csp.add_value_heuristic(CountHeuristic())
    return csp, variables, n, domains


def futoshiki_forward_prepare(data: List[str], name: str):
    csp, variables, n, domains = futoshiki_backtrack_prepare(data, name)
    row_size = int(math.sqrt(len(variables)))
    for i in range(row_size):
        curr_row = [coordinates for coordinates in variables if coordinates[0] == i]
        curr_col = [coordinates for coordinates in variables if coordinates[1] == i]
        csp.add_fix(UniqueFix(curr_row))
        csp.add_fix(UniqueFix(curr_col))
    csp.add_fix(MathFix(variables, data))
    return csp, variables, n, domains


def futoshiki_backward(data: List[str], name: str):
    csp, variables, n, domains = futoshiki_backtrack_prepare(data, name)
    start_time = time.time()
    solution: Optional[Dict[tuple[int, int], int]] = csp.run_backtrack()
    print("--- %s seconds ---" % (time.time() - start_time))
    print_solution(solution, data, n)
    print()


def futoshiki_backward_count(data: List[str], name: str):
    csp, variables, n, domains = futoshiki_backtrack_prepare(data, name)
    start_time = time.time()
    print('number of solutions: ', csp.run_backtrack_count())
    print("--- %s seconds ---" % (time.time() - start_time))


def futoshiki_forward(data: List[str], name: str):
    csp, variables, n, domains = futoshiki_forward_prepare(data, name)
    start_time = time.time()
    solution: Optional[Dict[tuple[int, int], int]] = csp.run_forward()
    print("--- %s seconds ---" % (time.time() - start_time))
    print_solution(solution, data, n)
    print()


def futoshiki_forward_count(data: List[str], name: str):
    csp, variables, n, domains = futoshiki_forward_prepare(data, name)
    start_time = time.time()
    print('number of solutions: ', csp.run_forward_count())
    print("--- %s seconds ---" % (time.time() - start_time))


def futoshiki_backtrack_data(data: List[str], name: str) -> List[tuple[float, int, int]]:
    csp, variables, n, domains = futoshiki_backtrack_prepare(data, name)
    start_time = time.time()
    backtrack_data: List[tuple[float, int, int]] = [(0, 0, 0)]
    backtrack_data = csp.run_backtrack_data(backtrack_data, start_time)
    backtrack_data.sort(key=lambda pair: pair[0])
    print(backtrack_data)
    return backtrack_data


def futoshiki_forward_data(data: List[str], name: str) -> List[tuple[float, int, int]]:
    csp, variables, n, domains = futoshiki_forward_prepare(data, name)
    start_time = time.time()
    forward_data: List[tuple[float, int, int]] = [(0, 0, 0)]
    forward_data = csp.run_forward_data(forward_data, start_time)
    forward_data.sort(key=lambda pair: pair[0])
    print(forward_data)
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
        if i % 2 == 0:
            for j in range(len(data[i])):
                if j % 2 == 0:
                    item = data[i][j]
                    pairs.append((int(i / 2), int(j / 2)))
    return pairs


def get_domain(variable: tuple[int, int], data: List[str], row_size: int) -> List[int]:
    item = data[variable[0] * 2][variable[1] * 2]
    if item.isnumeric():
        # print(variable, item)
        return [int(item)]
    else:
        returnlist = list(range(1, row_size + 1))
        # random.shuffle(returnlist)
        return returnlist


def matrix_to_string(solution: Dict[tuple[int, int], int], data: List[str], size: int):
    items = sorted(list(solution.items()), key=lambda pair: (pair[0][0], pair[0][1]))
    # print(items)
    counter = 0
    row_number = 0
    output = ""
    for row in data:
        output += "["
        if row_number % 2 == 0:
            for elem in row:
                if counter > len(items) - 1:
                    break
                if elem.isnumeric() or elem == 'x':
                    # print('counter', counter)
                    # print('len', len(items) - 1)
                    output += str(items[counter][1])
                    counter += 1
                elif elem == '-':
                    output += ' '
                else:
                    output += elem
            # output += ']\n['
        else:
            for elem in row:
                if elem == '-':
                    output += "- "
                elif elem == ">":
                    output += "> "
                elif elem == '<':
                    output += "< "
            output = output[:-1]
        output += ']\n'
        row_number += 1
    return output
