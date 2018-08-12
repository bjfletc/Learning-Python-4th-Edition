'''
Because they are sequences, lists support all the sequence operations we discussed for
strings; the only difference is that the results are usually lists instead of strings. For
instance, given a three-item list:
'''

L = [123, 'spam', 1.23]
len(L)

print(L[0])

print(L[:-1])

print(L + [4, 5, 6])
