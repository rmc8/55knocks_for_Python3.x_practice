doc: str = "i bought an apple .\ni ate it .\nit is delicious ."
lines: list = doc.splitlines()
counter: dict = {}
for line in lines:
    words: list = line.split()
    for word in words:
        counter[word] = counter.get(word, 0) + 1
print(counter)
