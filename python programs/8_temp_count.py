city = ["Pune", "Mumbai"]
temp = ["32.3", "38.6"]

paired = list(zip(city, temp))
sorted_paired = sorted(paired, key=lambda x: float(x[1]), reverse=True)

for c, t in sorted_paired:
    print(c)
