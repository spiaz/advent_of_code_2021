#%%
test_report = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]

expect = 7


#%%
def sum_increases(x):
    return sum([(x1 - x0)> 0 for x0, x1 in zip(x[:-1], x[1:])])

assert sum_increases(test_report) == expect

# %%
from pathlib import Path

input = Path('input01.txt').read_text().split()
input = [int(x) for x in input]
sum_increases(input) # 1233

# %%  PART 2

x = test_report
# %%
def sum3(x):
    return [x1 + x2 + x3 for x1, x2, x3 in zip(x[:-2], x[1:-1], x[2:])]

assert sum_increases(sum3(test_report)) == 5
# %%

sum_increases(sum3(input))
# %%
