def longest(words):
    word_len=[]
    for x in words:
        word_len.append((len(x), x))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
longest_length, longest_word = longest(["abc", "defg", "hi"])
print("Longest word: ", longest_word)
print("Length of the longest word: ", longest_length)