import random
numbers = random.sample(range(1, 10000),1000)

grp1 = [n for n in numbers if n % 2 == 0]
grp2 = [n for n in numbers if n % 2 == 1]
grp3 = [n for n in numbers if n % 5 == 0]
print("Group 1 (Even numbers):", grp1)
print("Group 2 (Odd numbers):", grp2)
print("Group 3 (Numbers divisible by 5):", grp3)