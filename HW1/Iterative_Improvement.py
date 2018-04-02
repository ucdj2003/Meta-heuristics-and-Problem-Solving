import random
import time
import os

# shuffling
# def shuffling(arr, num_machine):
#     for i in range(num_machine):
#         random.choice(arr[i])
#         print(arr[i])    
#     return arr

# swap(arr[i][swapjob], arr[i][swapjob + 1])
def swapping(arr, job_order, num_machine, num_jobs, swapjob, intervaljobs):
    if intervaljobs == 0:
        return
    flag = 0
    for i in range(num_machine):
        if swapjob + intervaljobs >= num_jobs:  # over array gap
            break
        arr[i][swapjob + intervaljobs], arr[i][swapjob] =  arr[i][swapjob], arr[i][swapjob + intervaljobs]
        if flag == 0:  # do once
            job_order[swapjob], job_order[swapjob + intervaljobs] = job_order[swapjob + intervaljobs], job_order[swapjob]
            flag = 1
    return arr, job_order

def ii(file_name):
    # init var
    num_machine = None
    num_jobs = None
    best_score = 9999
    best_order = None
    worst_score = 0
    avg_score = 0
    swapjob = 0
    intervaljobs = 0
    iter_num = 10000

    # read tai.txt
    with open(file_name, 'rt', encoding='UTF-8') as fin:
        str1 = fin.readline()
        str1 = str1.split()
        num_jobs = int(str1[0])
        num_machine = int(str1[1])
        arr = [[0 for j in range(num_jobs)] for i in range(num_machine)]   # arr[machines][jobs]
        # read jobs
        for i in range(num_machine):
            str2 = fin.readline()
            str2 = str2.split()
            for j in range(num_jobs):
                arr[i][j] = int(str2[j])

    temp_order = []
    for i in range(num_jobs):
        temp_order.append(i)

    # print details
    print("read: " + file_name)    
    print("number of machines: " + str(num_machine))
    print("number of jobs: " + str(num_jobs))
    print("iterations: " + str(iter_num))

    for iter_count in range(0, iter_num):
        # read tai.txt
        with open(file_name, 'rt', encoding='UTF-8') as fin:
            str1 = fin.readline()
            str1 = str1.split()
            num_jobs = int(str1[0])
            num_machine = int(str1[1])
            arr = [[0 for j in range(num_jobs)] for i in range(num_machine)]   # arr[machines][jobs]
            # read jobs
            for i in range(num_machine):
                str2 = fin.readline()
                str2 = str2.split()
                for j in range(num_jobs):
                    arr[i][j] = int(str2[j])

        job_order = []
        # load previous order to job order
        for i in temp_order:
            job_order.append(i)

        # Meta-heuristics Algorithm
        if intervaljobs == num_jobs & swapjob == num_jobs:
            swapjob = 1
            intervaljobs = 1
        if intervaljobs == num_jobs:
            swapjob += 1
            intervaljobs = 1
        swapping(arr, job_order, num_machine, num_jobs, swapjob, intervaljobs) # swapjob(neiborhood function)
        # print(arr)
        intervaljobs += 1

        # shuffling(arr, num_machine)

        # DP(max span)
        ans = [[0 for j in range(num_jobs)] for i in range(num_machine)]
        ans[0][0] = arr[0][0]
        for i in range(1, num_machine):  # same jobs
            ans[i][0] = ans[i-1][0] + arr[i][1] 
        for j in range(1, num_jobs):  # same machine
            ans[0][j] = ans[0][j-1] + arr[0][j]
        for i in range(1, num_machine):
            for j in range(1, num_jobs):
                ans[i][j] = max(ans[i-1][j], ans[i][j-1]) + arr[i][j]

        # Local Optima VS Best Optima        
        score = ans[num_machine-1][num_jobs-1]
        # print("The %d round answer = %d" % ((iter_count+1), score))
        if score < best_score:
            best_score = score
            best_order = job_order
            # best_arr = arr
        if score > worst_score:
            worst_score = score
        avg_score += score
    avg_score = avg_score / iter_num

    print("Best Score = %d" % (best_score))
    print("Worst Score = %d" % (worst_score))
    print("Avg Score = %d" % (avg_score))
    print("Best Order is: ")
    print(best_order)
    # print("Best arr is: ")
    # print(best_arr)

# main
if __name__=="__main__":
    # load all data
    files = os.listdir("./HW1/data/")
    # every file do ii
    for i in files:
        start_time = time.time()
        ii("./HW1/data/" + i)
        execute_time = time.time() - start_time
        print("execute time: %.4fs\n" % (execute_time))
