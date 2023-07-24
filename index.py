import file as file
from capacity import calculate_threads


def main():
    file_path = "file.jpg"
    file.file_by_block_with_threads(file_path, file.calculate_block_size(file_path, calculate_threads()), calculate_threads())


if __name__ == "__main__":
    main()
