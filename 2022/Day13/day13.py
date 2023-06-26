# %%
from os import chdir
chdir(r"D:\Documents\Code\Py\AdventOfCode\2022\Day13")

with open("test.txt") as file:
    lines=file.readlines()

# %%
lines=[line.strip() for line in lines]
packets=[[eval(lines[i]),eval(lines[i+1])] for i in range(0,len(lines),3)]
packets

# %%
def flatten_list(input:list)->list:
    output=[]
    for item in input:
        if type(item) is not list:
            output += [item]
        else:
            try:
                for sub_item in item
                    if type(sub_item) is list:
                        output+=flatten_list(item)
                    else:
                        output+=item
            except IndexError:
                output+=item
        

    return output

# %%
packets=[(flatten_list(left),flatten_list(right)) for left,right in packets]

# %%
results=[]
for left, right in packets:
    if len(right)==0:
        results.append(1) # 1 for right order
        continue
    elif len(left)==0:
        results.append(0)
        continue
    else:
        for i in range(max(len(left),len(right)))   :
            try:
                right_item=right[i]
            except IndexError:
                results.append(0)
                break
            try:
                left_item=left[i]
            except IndexError:
                results.append(1)
                break
            if left_item<right_item:
                results.append(0)
                break
            if left_item>right_item:
                results.append(1)
                break
    

# %%
for i in range(len(results)):
    print(f"Comparing {packets[i][0]} vs {packets[i][1]}, result: {results[i]}")


