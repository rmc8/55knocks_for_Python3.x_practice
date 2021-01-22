dic: dict = {"two": 324, "four": 830, "three": 493, "one": 172, "five": 1024}
l: list = list(dic.items())
sorted_list = sorted(l, key=lambda li: li[1])
print([key for key, _ in sorted_list])
