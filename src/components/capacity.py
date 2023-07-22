import multiprocessing


def number_cores():
    return multiprocessing.cpu_count()
