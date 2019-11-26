s = input()
print('\n'.join(sorted([s[-i:] for i in range(1, len(s) + 1)])))