import random
from typing import List, Dict
from CSP.CSP import ValuesHeuristic
from collections import Counter


class CountHeuristic(ValuesHeuristic[int]):
    def Heuristic(self, values: List[int], solution: Dict[List[tuple[int, int]], int]) -> None:
        if len(values) == 1:
            return
        values.reverse()
        counter = Counter(solution.values())
        values.sort(key=lambda x: counter[x])


class RandomHeuristic(ValuesHeuristic[int]):
    def Heuristic(self, values: List[int], solution: Dict[List[tuple[int, int]], int]) -> None:
        random.shuffle(values)
