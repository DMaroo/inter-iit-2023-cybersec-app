#!/usr/bin/env python3

lookup = [158, 152, 106, 153, 44, 139, 54, 67, 169, 156, 159, 192, 243, 88, 96, 189, 225, 33, 79, 3, 248, 100, 145, 14, 76, 126, 141, 224, 64, 74, 86, 55, 220, 49, 150, 71, 187, 22, 40, 162]

def hash(a, b):
    return chr(ord('A') + (((a ^ b) + a) & (a + b)) % 26)

print(''.join([hash(lookup[i], lookup[i + 1]) for i in range(0, len(lookup), 2)]))
