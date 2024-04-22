data = '''
    test test test
test test test
        test test test
test test test
                test test test
test test test
'''
prefix = ">"
text_with_prefix = '\n'.join(prefix + " " + line.lstrip() for line in data.split('\n'))

print()
print(text_with_prefix)
print()
