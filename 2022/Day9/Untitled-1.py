# %%
from typing import Union
import numpy as np
from os import chdir
chdir(r'D:\Documents\Code\Py\AdventOfCode\2022\Day9')


# %%
with open("test.txt") as file:
    lines = file.readlines()


# %%
moves = [line.strip().split(" ") for line in lines]


# %%
class Position():
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __sub__(self, other) -> list[int, int]:
        diff_x = self.x-other.x
        diff_y = self.y-other.y
        return [diff_x, diff_y]

    def __add__(self, other):
        x = self.x+other.x
        y = self.y+other.y
        return Position(x, y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def copy(self):
        return Position(self.x, self.y)


# %%
def update_tail_pos(tail_pos:Position,head_pos:Position,tail_visited:list=None):

    if issubclass(type(tail_pos),list):
        update_tail_pos(tail_pos[0],head_pos)
        for i,pos in enumerate(tail_pos[1:-1]):
            update_tail_pos(pos,tail_pos[i])
        update_tail_pos(tail_pos[-1],tail_pos[-2],tail_visited)
        return

    diffs=head_pos-tail_pos
    diff_x,diff_y=diffs

    if abs(diff_x)<=1 and abs(diff_y)<=1:
        return tail_pos, tail_visited

    if 0 in diffs:
        if diff_x==0:
            tail_pos.y+=int(diff_y/abs(diff_y))
        else:
            tail_pos.x+=int(diff_x/abs(diff_x))
    else:
        tail_pos.x+=int(diff_x/abs(diff_x))
        tail_pos.y+=int(diff_y/abs(diff_y))
    
    if tail_visited != None:
        if not tail_pos in tail_visited:
            tail_visited.append(tail_pos.copy())

# %%
def encode_direction(direction: str) -> Position:
    if direction == "U":
        return Position(0, 1)
    if direction == "D":
        return Position(0, -1)
    if direction == "L":
        return Position(-1, 0)
    if direction == "R":
        return Position(1, 0)


# %%
head_pos = Position()
tail_pos = Position()
tail_visited = [tail_pos.copy()]
positions=[]

for direction, amount in moves:
    amount = int(amount)
    direction = encode_direction(direction)

    for i in range(amount):
        head_pos += direction
        update_tail_pos(
            tail_pos, head_pos, tail_visited)
        positions.append((head_pos, tail_pos))
        print(head_pos,tail_pos)


print(head_pos, tail_pos)


# %%
len(tail_visited)


# %% [markdown]
# # Part 2

# %%
def add_marker(pos: Position, marker: str, output: np.ndarray) -> None:
    try:
        output[output.shape[0]-pos.y-1, pos.x]=marker  # Flip the y-axis
    except IndexError:
        pass


# %%

def format_output(head_pos:Position,tail_pos:Union[list[Position],Position],shape:tuple[int]=(5,5))->str:

    
    temp_output = np.full(shape, ".", str)
    add_marker(head_pos, "H", temp_output)
    if not issubclass(type(tail_pos),list):
        add_marker(tail_pos,"T",temp_output)
    else:
        for i,pos in enumerate(tail_pos):
            add_marker(pos,str(i+1),temp_output)

    output=""

    for row in temp_output:
        for item in row:
            output+= item
        output+="\n"
    output+="\n"
    return output



# %%
for head_pos, tail_pos in positions:
    print(format_output(head_pos, tail_pos))

# %%
head_pos = Position()
tail_pos = [Position(),Position(),Position()]
tail_visited = [Position()]
positions=[]

for direction, amount in moves:
    amount = int(amount)
    direction = encode_direction(direction)

    for i in range(amount):
        head_pos += direction
        update_tail_pos(
            tail_pos, head_pos, tail_visited)
        positions.append((head_pos, tail_pos))
        print(head_pos) 
        for pos in tail_pos:
            print(pos)


# %%
i=0
for head_pos, tail_pos in positions:
    print(i,"\n",head_pos)
    _=[print(pos) for pos in tail_pos]
    i+=1
    print(format_output(head_pos,tail_pos))
    "\n"


