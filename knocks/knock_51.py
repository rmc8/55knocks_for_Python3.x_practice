li1: list = list(range(1, 32))
li2: list = list(range(1, 13))
print(sum([elm1 % 10 == elm2 % 10 for elm1 in li1 for elm2 in li2]))
