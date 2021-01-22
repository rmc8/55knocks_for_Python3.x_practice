def jaccard_index(A: set, B: set):
    divideend = len(A & B)
    divisor = len(A | B)
    return divideend / divisor


list1: list = [12, 23, 34, 45, 56, 67, 78, 89]
list2: list = [21, 32, 43, 45, 65, 67, 78, 98]

print(jaccard_index(set(list1), set(list2)))
