import os
from psutil import virtual_memory


def calculate_offset(path_file, threads):
    block_offset = []
    file_size = os.path.getsize(path_file)
    memory_size = virtual_memory().available
    offset = file_size//threads
    if file_size > memory_size:
        while memory_size < (offset*threads):
            offset = offset//2
    for i in range(file_size//offset):
        block_offset.append(i*offset)
    return block_offset
