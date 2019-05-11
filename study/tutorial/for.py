words=['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


# Loop over a slice copy of the entire list.
for w in words[:] :
    if len(w) >6:
        words.insert(0, w)
print(words)