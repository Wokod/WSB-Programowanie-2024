def word_counter(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(word_counter("dzien pierwszy dzien drugi dzien trzeci czwarty weekend weekend weekend"))