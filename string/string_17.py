def reverse(s):
    if len(s) % 4 == 0:
        return " ".join(reversed(s))
    return s
print(reverse("abcdefgh"))
print(reverse("abdef"))