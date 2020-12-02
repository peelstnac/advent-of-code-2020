import math
from typing import List


x = []
with open('.in', 'r') as fp:
    x = list(map(int, fp.read().split()))


def find(total: int, index: int, left: int) -> List[int]:
    if (left == 1):
        for i in range(index + 1, len(x)):
            if x[i] == total:
                return [x[i]]
        return []
    for i in range(index + 1, len(x)):
        t = find(total - x[i], i, left - 1)
        sol = [x[i]]
        if (len(t) > 0):
            sol.extend(t)
            return sol
    return []


print(math.prod(find(2020, -1, 2)))
print(math.prod(find(2020, -1, 3)))
