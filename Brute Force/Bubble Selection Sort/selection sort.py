import random
import time


# implementation of selection sort
# to sort a random array with 10,000 elements
# two metrics ("number of comparison" and "consumed time") for efficiency evaluation

random.seed(1)  # for reproducibility
def selection_sort(array):
    cnt = 0
    for i in range(len(array)-1):
        minimum = i
        for j in range(i+1, len(array)):
            if array[j] < array[minimum]:
                minimum = j
            cnt += 1
        array[minimum], array[i] = array[i], array[minimum]
    return cnt


time_in_total = 0
epoch = 10  # num of iteration
total_comparison = 0
for i in range(epoch):
    time_start = time.time()
    array = [random.randint(0,10000) for i in range(10000)]
    comparison = selection_sort(array)
    time_finish = time.time()
    total_comparison += comparison
    time_in_total += time_finish-time_start
    print("Epoch {}: \n  number of comparison: {}\n  time consumed: {:.2f} s".format(i+1, comparison, time_finish-time_start))
print("average number of comparison: %d" % (total_comparison/10))
print('average time consumed: {:.2f} s'.format(time_in_total/10))
