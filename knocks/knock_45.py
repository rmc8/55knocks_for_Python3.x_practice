li = [{"a": 6, "b": 7, "c": 6},
      {"a": 4, "b": 2, "c": 3},
      {"a": 1, "b": 5, "c": 8}]
print(sorted(li, key=lambda d: d["b"], reverse=True))
