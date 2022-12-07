# %%
from os import chdir
chdir("Day7")
with open('test.txt') as file:
    lines = file.readlines()

# separate tokens and remove trailing whitespace
lines = [line.strip().split(" ") for line in lines]


# %%
# Construct classes to save our files and directories
class Directory():
    name: str
    size: int
    contents: dict

    def __init__(self, name: str, parent=None):
        self.name = name
        self.contents = {}
        self.parent = parent
        self.size = 0

    def __str__(self):
        return f"- {self.name} (dir)"

    def calculate_size(self):
        pass  # TODO implement method


class File():
    name: str
    size: int

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __str__(self):
        return f"- {self.name} (file, size={self.size})"


# %%
current_tree = ["/"]
current_dir = Directory("/")
root_dir = current_dir
contents = []

for i, line in enumerate(lines):
    if line[0] != "$":
        continue
    if line[1] == "cd":
        target = line[2]
        if target == "..":
            current_tree.pop()
            current_dir = current_dir.parent
        elif target == current_tree[-1]:
            pass
        else:
            current_tree.append(target)
            if target in current_dir.contents:
                current_dir = current_dir.contents[target]
            else:
                current_dir = Directory(target, current_dir)
    else:
        for j, new_line in enumerate(lines[i+1:]):
            if new_line[0] == "$" or j+1+1 == len(lines):
                contents = lines[i+1:j+i+1]
                break
        for dir_or_size, name in contents:
            if dir_or_size == "dir":
                if not name in current_dir.contents:
                    current_dir.contents[name] = Directory(name, current_dir)
            else:
                if not name in current_dir.contents:
                    current_dir.contents[name] = File(name, dir_or_size)


# %%
def recursive_folder_printer(dir: Directory, indent: int = 0, to_print=False):
    output = " "*indent + dir.__str__()+"\n"
    for item in dir.contents:
        item = dir.contents[item]
        if issubclass(type(item), Directory):
            output += recursive_folder_printer(item, indent+2)
        else:
            output += " "*(indent+2) + item.__str__()+"\n"
    if not to_print:
        return output
    else:
        print(output)


recursive_folder_printer(root_dir, to_print=True)


# %%
test_dir = root_dir.contents["a"].contents["e"]



