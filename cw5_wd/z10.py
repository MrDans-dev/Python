import itertools
x = 3
my_list = range(1, 11)
for k in [x]:
    for sublist in itertools.combinations(my_list, k):
        print(sublist)