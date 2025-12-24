num = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
n = len(num)
mean = sum(num) / n
median = sorted(num)[n // 2]
counts = {x: num.count(x) for x in num}
max_count = max(counts.values())
if max_count == 1:
    mode = "No mode"
else:
    mode = [x for x, c in counts.items() if c == max_count]


frequency = {}
for i in num:
    frequency[i] = frequency.get(i, 0) + 1
max_freq = max(frequency.values())
if max_freq == 1:
    result = "No mode"
else:
    result = [k for k, v in frequency.items() if v == max_freq]

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Frequency:", frequency)
print("Result:", result)