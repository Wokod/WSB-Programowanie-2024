data = input("Provide comma-separated words: ")
animals = [name.strip() for name in data.split('.')]
print(" ".join(sorted(list(set(animals)))))
