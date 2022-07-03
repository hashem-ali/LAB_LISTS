### Q1 ###
my_list = [5, 4, 17, 19, 30, 2, 7, 10, 45]
size = len(my_list)
result = 0

for elment in my_list:
    result = elment + result

print(result)

### Q2 ###
max = my_list[0]
for elment in my_list:
    if elment > max:
        max = elment

print(max)

### Q3 ###

new_list = [x for x in my_list if x % 2 == 0 ]

print(new_list)