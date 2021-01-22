d: dict = {"apple": 10, "grape": 20, "orange": 30}
for fruit in ["apple", "pineapple"]:
    d[fruit] = d.get(fruit, -1)
print(d)
