import multiprocessing


def calculate_threads():
    numCores = multiprocessing.cpu_count()
    return numCores
