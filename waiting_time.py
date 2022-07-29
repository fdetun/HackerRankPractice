#!/usr/bin/python3

def waitingTime(tickets, p):
    a = [min(tickets[i], tickets[p]) if i<=p else min(tickets[i], tickets[p] - 1) for i in range(len(tickets))]
    return sum(a)

print(waitingTime([2, 6, 3, 4, 5], 2))