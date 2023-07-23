import file as file


def main():
    file_path = "file.jpg"
    file.file_by_block_with_threads(file_path)


if __name__ == "__main__":
    main()
