#%%
from pathlib import Path
from collections import defaultdict
from typing import List, Tuple

test_input = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


def parse(t):
    l = t.split("\n")
    instr = [x.split() for x in l if len(x) > 0]

    d = defaultdict(lambda: 0)

    for k, v in instr:
        d[k] += int(v)
    return d


def sum_pos(d):
    return d["forward"] - d["backward"], d["down"] - d["up"]


i = parse(test_input)
h, v = sum_pos(i)
assert h * v == 150

p = Path("input01.txt")
input = p.read_text()
i = parse(input)
h, v = sum_pos(i)
h * v
# %% PART 2


class Instruction:
    def __init__(self, instr: str, val: str):
        self.instr = instr
        self.val = int(val)


Instruction(instr="azz", val=0)
Instruction(*["azz", 0])

#%%


def aim_parse(t: str) -> List[Instruction]:
    l = t.split("\n")
    instr = [Instruction(*s.split()) for s in l if len(s) > 0]
    return instr


def aim_pos(instructions: List[Instruction]) -> Tuple[int, int]:
    horiz, vert, aim = 0, 0, 0

    for i in instructions:
        if i.instr == "forward":
            vert += i.val * aim
            horiz += i.val
        if i.instr == "up":
            aim -= i.val
        elif i.instr == "down":
            aim += i.val
    return horiz, vert


i = aim_parse(test_input)
h, v = aim_pos(i)
assert h * v == 900
# %%
i = aim_parse(input)
h, v = aim_pos(i)
h * v

# %%
