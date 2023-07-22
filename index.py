import threading
import os

# Crear un bloqueo global para sincronizar el acceso al archivo de salida
lock = threading.Lock()


def write_file_block(file_path, file_seek, block_size):
    with open(file_path, "rb") as file:
        file.seek(file_seek)
        block = file.read(block_size)
        with lock:
            with open("copy/copy.jpg", "ab") as file_copy:
                file_copy.write(block)


def file_by_block_with_threads(file_path, block_size=285736, threads=4):
    #file_size = os.path.getsize(file_path)
    block_offset = []
    for i in range(threads):
        block_offset.append(i*block_size)

    threads = []
    for offset in block_offset:
        thread = threading.Thread(target=write_file_block, args=(file_path, offset, block_size))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def main():
    file_path = "file/Fallout.jpg"
    file_by_block_with_threads(file_path)


if __name__ == "__main__":
    main()
