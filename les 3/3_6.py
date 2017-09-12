s = str("Guido van Rossum heeft programmeertaal Python bedacht.")
for x in s:
    if x not in 'aeiou':
        print(x)