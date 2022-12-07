from typing import List

with open("d7.txt") as f:
    lines = [line.strip() for line in f.readlines()]


def find_total_size(lines: List[str]):
    TOTAL_SIZE = 70000000
    REQUIRED_SIZE = 30000000
    MAX_SIZE = 100000
    total_file_sizes = 0
    used_space = 0
    directories = []

    def recurse_directory(line_index: int, lines: List[str]):
        nonlocal total_file_sizes, used_space
        if line_index == len(lines):
            return 0, len(lines)
        
        total = 0
        while line_index < len(lines):
            current_line = lines[line_index]
            if current_line.startswith("dir"):
                line_index += 1
                continue

            if current_line == "$ cd ..":
                if total <= MAX_SIZE:
                    total_file_sizes += total
                directories.append(total)
                return total, line_index + 1
            
            if current_line.startswith("$ cd"):
                dir_total, line_index = recurse_directory(line_index + 2, lines)
                total += dir_total
                continue
            
            file_size = int(current_line.split()[0])
            total += file_size
            used_space += file_size
            line_index += 1
        
        if total <= MAX_SIZE:
            total_file_sizes += total
        directories.append(total)
        return total, line_index
            
    recurse_directory(2, lines)
    available_space = TOTAL_SIZE - used_space
    required_space = REQUIRED_SIZE - available_space
    directory_to_delete = None

    for directory_size in directories:
        if directory_size < required_space:
            continue
        
        directory_to_delete = directory_size if directory_to_delete is None else min(directory_to_delete, directory_size)

    return directory_to_delete

print(find_total_size(lines))