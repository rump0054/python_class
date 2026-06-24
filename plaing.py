output = None
print('Before:', output)
for itervar in [3, 41, 12, 9, 74, 15]:
    if output is None or itervar > output :
        output = itervar
print('After:', output)
