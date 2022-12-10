
from os import chdir
# %%
chdir(r'D:\Documents\Code\Py\AdventOfCode\2015\Day5')
with open("test.txt") as file:
    lines=file.readlines()

lines=[line.strip() for line in lines]

# %%
lines_and_status=[] # 1 is nice, 0 is naughty

for line in lines:
    # conditions to satisfy:
    vowels=["a","e","i","o","u"]
    n_vowels=0
    forbidden_combinations=["ab", "cd", "pq", "xy"]
    forbidden_found=False
    double_found =False

    for i, char in enumerate(line):
        

        if char in vowels:
            n_vowels+=1
        if i == len(line)-1:
            break
        if line[i:i+2] in forbidden_combinations:
            forbidden_found=True
        if char==line[i+1]:
            double_found=True

    if (not forbidden_found) and double_found and n_vowels>=3:
        lines_and_status.append([line,1])
    else:
        lines_and_status.append([line,0])

# %%
lines_and_status

# %%
nice_lines=[line for line in lines_and_status if line[1]==1]
len(nice_lines)

# %% [markdown]
# # Part 2

# %%
lines_and_status=[] # 1 is nice, 0 is naughty

for line in lines:
    # conditions to satisfy:
    double_pair=False
    repeat_found =False

    for i, char in enumerate(line):
        
        if i<=2 and line[i-2] == char:
            repeat_found=True

        if i<len(line)-3:
            pair=line[i:i+2]
            index=line.find(pair)
            if index !=-1:
                if line[index+2:].find(pair) !=-1:
                    double_pair=True
                    found_pair=pair

    if double_pair and repeat_found:
        lines_and_status.append([line,1,found_pair])
    else:
        lines_and_status.append([line,0])

# %%
lines_and_status

# %%
nice_lines=[line for line in lines_and_status if line[1]==1]
len(nice_lines) # 458, 242 too high; 60 wrong

# %%
nice_lines

# %%
for line in nice_lines:
    index1=line[0].find(line[2])
    index2=line[0][index1+2:].find(line[2])+index1+2
    # if (line[2] != line[0][index1:index1+2]) or (line[2]!=line[0][index2:index2+2]):
    print(f"{line[0]}, pair:({index1},{index2}) {line[2]}; {line[0][index1:index1+2]}, {line[0][index2:index2+2]}")


