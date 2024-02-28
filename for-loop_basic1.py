# Basic
for i in range(0, 151):
    print(i)

# Multiples of 5
for i in range(5, 1001, 5):
    print(i)

# counting the dojo way
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# Whoa that suckers huge
odd_integer = 0
for i in range(1, 500000, 2):
    odd_integer += i

print("the sum of odd integers is:", odd_integer)

# countdown by 4s
for i in range(2018, 0, -4):
    print(i)

# Flexible counter
low_num = 3
high_num = 50
mult_by = 7

for i in range(low_num, high_num + 1):

    if i % mult_by == 0:
        print(i)
