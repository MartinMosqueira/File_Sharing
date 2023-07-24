import threading
from offset import calculate_offset

# Crear un bloqueo global para sincronizar el acceso al archivo de salida
lock = threading.Lock()


def calculate_block_size(path_file, threads):
    block = calculate_offset(path_file, threads)
    return block[1] - block[0]


def write_file_block(file_path, file_seek, block_size):
    with open(file_path, "rb") as file:
        file.seek(file_seek)
        block = file.read(block_size)
    with lock:
        with open('copy/copy.jpeg', 'ab') as file_copy:
            file_copy.write(block)


def file_by_block_with_threads(file_path, block_size, thread):
    offsets = calculate_offset(file_path, thread)
    num_threads = min(thread, len(offsets))
    threads = []
    for offset in range(num_threads):
        group_offsets = offsets[offset::num_threads]
        thread = threading.Thread(target=process_offsets, args=(file_path, block_size, group_offsets))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def process_offsets(file_path, block_size, offsets):
    for offset in offsets:
        write_file_block(file_path, offset, block_size)
