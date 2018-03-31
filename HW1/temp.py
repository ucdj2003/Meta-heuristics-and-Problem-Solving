import random


# def shuffling(arr, num_machine):
#     for i in range(num_machine):
#         random.choice(arr[i])
#         print(arr[i])    
#     return arr

# swap(arr[i][swapjob], arr[i][swapjob + 1])
def swapping(arr, num_machine, num_jobs, swapjob, intervaljobs):
    if intervaljobs == 0:
        return
    for i in range(num_machine):
        if swapjob + intervaljobs >= num_jobs:  # over array gap
            break
        arr[i][swapjob + intervaljobs], arr[i][swapjob] =  arr[i][swapjob], arr[i][swapjob + intervaljobs]
    return arr

def ii():
    optimal_ans = 10000000
    swapjob = 0
    intervaljobs = 0
    for n in range(0, 10000):
        # Read tai.txt
        with open('Homework/tai20_5_1.txt', 'rt', encoding='UTF-8') as fin:
            str1 = fin.readline()
            str1 = str1.split()
            num_jobs = int(str1[0])
            num_machine = int(str1[1])
            arr = [[0 for j in range(num_jobs)] for i in range(num_machine)]   # arr[machines][jobs]
            # Read test number
            for i in range(num_machine):
                str2 = fin.readline()
                str2 = str2.split()
                for j in range(num_jobs):
                    arr[i][j] = int(str2[j])

        Meta-heuristics Algorithm
        if intervaljobs == num_jobs & swapjob == num_jobs:
            swapjob = 1
            intervaljobs = 1
        if intervaljobs == num_jobs:
            swapjob += 1
            intervaljobs = 1
        swapping(arr, num_machine, num_jobs, swapjob, intervaljobs) # swapjob(neiborhood function)
        print(arr)
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

        local_ans = ans[num_machine-1][num_jobs-1]
        print("The %d round answer = %d" % ((n+1), local_ans))
        if local_ans < optimal_ans:
            optimal_ans = local_ans

    print("Best Answer = %d" % (optimal_ans))

# main
if __name__=="__main__":
    ii()