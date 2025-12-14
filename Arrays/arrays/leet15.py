import itertools
from typing import List

nums = [-1,0,1,2,-1,-4]
a = set()
ac = itertools.combinations(nums, 3)

for i in ac:
    if sum(i) == 0:
        a.add(tuple(sorted(i)))  # sort & store as tuple to avoid duplicates

print([list(x) for x in a])
