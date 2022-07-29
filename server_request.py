#!/usr/bin/python3


q =[-1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1]

def countDroppedRequests(server):
    droppred_r = 0
    threads = 0
    for i in server:
        droppred_r =  droppred_r+ 1 if threads + i<0 else droppred_r
        threads = threads+ i if i >0 else threads- i*i
        if threads<0:
            threads =0
        print(threads,droppred_r)
    return droppred_r

print(countDroppedRequests(q))