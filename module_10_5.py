import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for i in file:
            file.readline()
            all_data.append(i)


time_line_start = time.time()
r = read_info(name='file 1.txt')
r2 = read_info(name='file 2.txt')
r3 = read_info(name='file 3.txt')
r4 = read_info(name='file 4.txt')
time_line_end = time.time()
sum_line_time = time_line_end - time_line_start
print(sum_line_time)

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    time_proc_start = time.time()
    with Pool() as p:
        p.map(read_info, filenames)
    time_proc_end = time.time()
    sum_proc_time = time_proc_end - time_proc_start
    print(sum_proc_time)
