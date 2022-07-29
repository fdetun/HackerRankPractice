#!/usr/bin/python3

with open('stin') as f:
    lines = f.read().splitlines()
print([int(i) for i in lines])