import random

n = 200
a = 10
b = 70

rand_list = []

for _ in range(n):
    rand_val = random.randint(a, b)
    rand_list.append(rand_val)
    
rand_avg = sum(rand_list)/len(rand_list)

rand_diff_sqr = []

for i in rand_list:
    rand_diff_sqr.append(abs(i - rand_avg)**2)

rand_stdev = (sum(rand_diff_sqr)/len(rand_diff_sqr))**0.5

print("Avg: ", rand_avg)
print("Stdev: ", rand_stdev)